# -*- coding: utf-8 -*-

#---------------------------------------------------------- [Lib] -----------------------------------------------------------#

import os
import shutil
import glob

from core.splendenteError import Error 

#--------------------------------------------------- [Function(s)/Class] ----------------------------------------------------#

class Copy:

    def __init__(self):
        self.error = Error()

    def Format(self, extension, usbDirectory, targetDirectory, size, depth):
        for name in extension:
            src = sorted(glob.glob(depth.format(targetDirectory, name)))
            for value in src:
                if os.path.getsize(value) > 0 and os.path.getsize(value) < size:
                    try:
                        shutil.copy(value, "{0}".format(usbDirectory))
                    except self.error:
                        pass
    
    def SmallDepth(self, extension, usbDirectory, targetDirectory, size):
        Copy.Format(self, extension, usbDirectory, targetDirectory, size, "{0}\\{1}")

    def MediumDepth(self, extension, usbDirectory, targetDirectory, size):
        Copy.Format(self, extension, usbDirectory, targetDirectory, size, "{0}\\{1}")
        Copy.Format(self, extension, usbDirectory, targetDirectory, size, "{0}\\*\\{1}")

    def HighDepth(self, extension, usbDirectory, targetDirectory, size):
        Copy.Format(self, extension, usbDirectory, targetDirectory, size, "{0}\\{1}")
        Copy.Format(self, extension, usbDirectory, targetDirectory, size, "{0}\\*\\{1}")
        Copy.Format(self, extension, usbDirectory, targetDirectory, size, "{0}\\*\\*\\{1}")
