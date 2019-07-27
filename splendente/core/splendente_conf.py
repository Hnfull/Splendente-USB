# -*- coding: utf-8 -*-

#---------------------------------------------------------- [Lib] -----------------------------------------------------------#

import configparser

#--------------------------------------------------- [Function(s)/Class] ----------------------------------------------------#
    
class Conf():

    def __init__(self):
        self.conf = configparser.ConfigParser()


    def Databases(self, confFile):
        self.conf.read(confFile)
        databases = self.conf.get('EXTENSION', 'Databases')
        parseDatabases = databases.split(",")
        return parseDatabases


    def Docs(self, confFile):
        self.conf.read(confFile)
        docs = self.conf.get('EXTENSION', 'Docs')
        parseDocs = docs.split(",")
        return parseDocs


    def Pictures(self, confFile):
        self.conf.read(confFile)
        pictures = self.conf.get('EXTENSION', 'Pictures')
        parsePictures = pictures.split(",")
        return parsePictures


    def Compress(self, confFile):
        self.conf.read(confFile)
        compress = self.conf.get('EXTENSION', 'Compress')
        parseCompress = compress.split(",")
        return parseCompress


    def Programs(self, confFile):
        self.conf.read(confFile)
        programs = self.conf.get('EXTENSION', 'Programs')
        parsePrograms = programs.split(",")
        return parsePrograms


    def Emails(self, confFile):
        self.conf.read(confFile)
        emails = self.conf.get('EXTENSION', 'Emails')
        parseEmails = emails.split(",")
        return parseEmails


    def FirefoxBrowser(self, confFile):
        self.conf.read(confFile)
        firefoxBrowser = self.conf.get('EXTENSION', 'FirefoxBrowser')
        parseFirefoxBrowser = firefoxBrowser.split(",")
        return parseFirefoxBrowser


    def ChromeBrowser(self, confFile):
        self.conf.read(confFile)
        chromeBrowser = self.conf.get('EXTENSION', 'ChromeBrowser')
        parseChromeBrowser = chromeBrowser.split(",")
        return parseChromeBrowser


    def Directories(self, confFile):
        self.conf.read(confFile)
        directories = self.conf.get('PATH', 'Directories')
        parseDirectories = directories.split(",")
        return parseDirectories

