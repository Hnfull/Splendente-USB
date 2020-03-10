# -*- coding: utf-8 -*-

# https://github.com/Hnfull/Splendente-USB

#---------------------------------------------------------- [Lib] -----------------------------------------------------------#

import os
import shutil
import glob

#--------------------------------------------------- [Function(s)/Class] ----------------------------------------------------#

class Copy:

    def Format(self, extension, usbDirectory, targetDirectory, size, depth):
        for name in extension:
            src = sorted(glob.glob(depth.format(targetDirectory, name)))
            for value in src:
                if os.path.getsize(value) > 0 and os.path.getsize(value) < size:
                    try:
                        shutil.copy(value, "{}".format(usbDirectory))
                    except Exception:
                        pass
    

    def SmallDepth(self, extension, usbDirectory, targetDirectory, size):
        Copy.Format(self, extension, usbDirectory, targetDirectory, size, "{}\\{}")

    
    def MediumDepth(self, extension, usbDirectory, targetDirectory, size):
        Copy.Format(self, extension, usbDirectory, targetDirectory, size, "{}\\{}")
        Copy.Format(self, extension, usbDirectory, targetDirectory, size, "{}\\*\\{}")

    
    def HighDepth(self, extension, usbDirectory, targetDirectory, size):
        Copy.Format(self, extension, usbDirectory, targetDirectory, size, "{}\\{}")
        Copy.Format(self, extension, usbDirectory, targetDirectory, size, "{}\\*\\{}")
        Copy.Format(self, extension, usbDirectory, targetDirectory, size, "{}\\*\\*\\{}")
