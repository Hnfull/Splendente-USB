# -*- coding: utf-8 -*-

# https://github.com/Hnfull/Splendente-USB

#---------------------------------------------------------- [Lib] -----------------------------------------------------------#

import datetime

#--------------------------------------------------- [Function(s)/Class] ----------------------------------------------------#

def Date():
    return datetime.datetime.now().strftime("%y-%m-%d-%H-%M-%S")


def SmallSize():
    return 1000000 # 1MB


def MediumSize():
    return 5000000 # 5MB


def HighSize():
    return 20000000 # 20MB


def BigSize():
    return 150000000 # 150MB