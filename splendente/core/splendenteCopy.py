# -*- coding: utf-8 -*-

#---------------------------------------------------------- [Lib] -----------------------------------------------------------#

import os
import shutil
import glob

#--------------------------------------------------- [Function(s)/Class] ----------------------------------------------------#

class Copy:

    def Format(extension, usbDirectory, targetDirectory, size, depth):
        for name in extension:
            src = sorted(glob.glob(depth.format(targetDirectory, name)))
            for value in src:
                if os.path.getsize(value) > 0 and os.path.getsize(value) < size:
                    try:
                        shutil.copy(value, "{0}".format(usbDirectory))
                    except Exception as e:
                        pass
                else:
                    continue
    
    def SmallDepth(extension, usbDirectory, targetDirectory, size):
        Copy.Format(extension, usbDirectory, targetDirectory, size, "{0}\\{1}")

    def MediumDepth(extension, usbDirectory, targetDirectory, size):
        Copy.Format(extension, usbDirectory, targetDirectory, size, "{0}\\{1}")
        Copy.Format(extension, usbDirectory, targetDirectory, size, "{0}\\*\\{1}")

    def HighDepth(extension, usbDirectory, targetDirectory, size):
        Copy.Format(extension, usbDirectory, targetDirectory, size, "{0}\\{1}")
        Copy.Format(extension, usbDirectory, targetDirectory, size, "{0}\\*\\{1}")
        Copy.Format(extension, usbDirectory, targetDirectory, size, "{0}\\*\\*\\{1}")
