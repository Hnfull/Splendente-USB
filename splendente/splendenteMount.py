# -*- coding: utf-8 -*-

#---------------------------------------------------------- [Lib] -----------------------------------------------------------#

import wmi
import win32api
import win32con

#--------------------------------------------------------- [Global] ---------------------------------------------------------#

searchWinMount = wmi.WMI()

#--------------------------------------------------- [Function(s)/Class] ----------------------------------------------------#

# -- Search other partitions mounted on target and add in list -- #
class TargetMount():

    def SearchPartitionsMount():
        targetPartitionsMountList = []

        for mountPoint in searchWinMount.Win32_LogicalDisk():
            if mountPoint.VolumeName == "RECOVERY" or mountPoint.VolumeName == "USB_DATA" or mountPoint.DeviceID == "C:" or mountPoint.Description == "Disque CD-ROM":
                continue
            else:
                targetPartitionsMountList.append(mountPoint.DeviceID + "\\")

        return targetPartitionsMountList[:]
    

# -- Search other partitions mounted on target and add in list for created folders on USB key -- #
class UsbMount():

    # --- Search letter ID of partition labeled USB_DATA (USB key) --- #
    def SearchUsbMountLetter():    
        for mountPoint in searchWinMount.Win32_LogicalDisk():
            if mountPoint.VolumeName == "USB_DATA":
                return mountPoint.DeviceID
            else:
                continue

    def SearchPartitionsMount():
        usbPartitionMountDirectories = []

        for mountPoint in searchWinMount.Win32_LogicalDisk():
            if mountPoint.VolumeName == "RECOVERY" or mountPoint.VolumeName == "USB_DATA" or mountPoint.DeviceID == "C:" or mountPoint.Description == "Disque CD-ROM":
                continue
            else:
                mountPoint = mountPoint.DeviceID.replace(':', '')
                usbPartitionMountDirectories.append(mountPoint)

        return usbPartitionMountDirectories[:]
