# -*- coding: utf-8 -*-

#---------------------------------------------------------- [Lib] -----------------------------------------------------------#

import os
import shutil
import glob

#--------------------------------------------------- [Function(s)/Class] ----------------------------------------------------#

class Copy:

    def SmallDepth(extension, usbDirectory, targetDirectory, size):
        for ext in extension:
            src = sorted(glob.glob("{0}\\{1}".format(targetDirectory, ext)))
            for value in src:
                if os.path.getsize(value) > 0 and os.path.getsize(value) < size:
                    try:
                        shutil.copy(value, "{0}".format(usbDirectory))
                    except Exception as e:
                        pass

    def MediumDepth(extension, usbDirectory, targetDirectory, size):
        for ext in extension:    
            src = sorted(glob.glob("{0}\\{1}".format(targetDirectory, ext)))
            for value in src:
                if os.path.getsize(value) > 0 and os.path.getsize(value) < size:
                    try:
                        shutil.copy(value, "{0}".format(usbDirectory))
                    except Exception as e:
                        pass

        for ext in extension:
            src = sorted(glob.glob("{0}\\*\\{1}".format(targetDirectory, ext)))
            for value in src:
                if os.path.getsize(value) > 0 and os.path.getsize(value) < size:
                    try:
                        shutil.copy(value, "{0}".format(usbDirectory))
                    except Exception as e:
                        pass

    def HighDepth(extension, usbDirectory, targetDirectory, size):
        for ext in extension:
            src = sorted(glob.glob("{0}\\{1}".format(targetDirectory,  ext)))
            for value in src:
                if os.path.getsize(value) > 0 and os.path.getsize(value) < size:
                    try:
                        shutil.copy(value, "{0}".format(usbDirectory))
                    except Exception as e:
                        pass 

        for ext in extension:
            src = sorted(glob.glob("{0}\\*\\{1}".format(targetDirectory, ext)))
            for value in src:
                if os.path.getsize(value) > 0 and os.path.getsize(value) < size:
                    try:
                        shutil.copy(value, "{0}".format(usbDirectory))
                    except Exception as e:
                        pass

        for ext in extension:
            src = sorted(glob.glob("{0}\\*\\*\\{1}".format(targetDirectory, ext)))
            for value in src:
                if os.path.getsize(value) > 0 and os.path.getsize(value) < size:
                    try:
                        shutil.copy(value, "{0}".format(usbDirectory))
                    except Exception as e:
                        pass



