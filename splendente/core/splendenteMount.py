# -*- coding: utf-8 -*-

#---------------------------------------------------------- [Lib] -----------------------------------------------------------#

import wmi
import win32api
import win32con

#--------------------------------------------------------- [Global] ---------------------------------------------------------#

SEARCH_WIN_MOUNT = wmi.WMI()

#--------------------------------------------------- [Function(s)/Class] ----------------------------------------------------#

# -- Search other partitions mounted on target and add in list -- #
class TargetMount():

    def __init__(self):
        self.targetPartitionsMountList = []

    def SearchPartitionsMount(self):
        for mountPoint in SEARCH_WIN_MOUNT.Win32_LogicalDisk():
            if mountPoint.VolumeName == "RECOVERY" or mountPoint.VolumeName == "USB_DATA" or mountPoint.DeviceID == "C:" or mountPoint.Description == "Disque CD-ROM":
                continue
            else:
                self.targetPartitionsMountList.append(mountPoint.DeviceID + "\\")

        return self.targetPartitionsMountList[:]
    
    
# -- Search other partitions mounted on target and add in list for created folders on USB key -- #
class UsbMount():

    def __init__(self):
        self.usbPartitionMountDirectories = []

    # --- Search letter ID of partition labeled USB_DATA (USB key) --- #
    def SearchUsbMountLetter(self):    
        for mountPoint in SEARCH_WIN_MOUNT.Win32_LogicalDisk():
            if mountPoint.VolumeName == "USB_DATA":
                return mountPoint.DeviceID
            else:
                continue

    def SearchPartitionsMount(self):
        for mountPoint in SEARCH_WIN_MOUNT.Win32_LogicalDisk():
            if mountPoint.VolumeName == "RECOVERY" or mountPoint.VolumeName == "USB_DATA" or mountPoint.DeviceID == "C:" or mountPoint.Description == "Disque CD-ROM":
                continue
            else:
                mountPoint = mountPoint.DeviceID.replace(':', '')
                self.usbPartitionMountDirectories.append(mountPoint)

        return self.usbPartitionMountDirectories[:]
