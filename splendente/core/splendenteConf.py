# -*- coding: utf-8 -*-

#---------------------------------------------------------- [Lib] -----------------------------------------------------------#

import configparser

#--------------------------------------------------------- [Global] ---------------------------------------------------------#

CONF = configparser.ConfigParser()

#--------------------------------------------------- [Function(s)/Class] ----------------------------------------------------#
    
class Conf():

    def Databases(confFile):
        CONF.read(confFile)
        databases = CONF.get('EXTENSION', 'Databases')
        parseDatabases = databases.split(",")
        return parseDatabases

    def Docs(confFile):
        CONF.read(confFile)
        docs = CONF.get('EXTENSION', 'Docs')
        parseDocs = docs.split(",")
        return parseDocs

    def Pictures(confFile):
        CONF.read(confFile)
        pictures = CONF.get('EXTENSION', 'Pictures')
        parsePictures = pictures.split(",")
        return parsePictures

    def Compress(confFile):
        CONF.read(confFile)
        compress = CONF.get('EXTENSION', 'Compress')
        parseCompress = compress.split(",")
        return parseCompress

    def Programs(confFile):
        CONF.read(confFile)
        programs = CONF.get('EXTENSION', 'Programs')
        parsePrograms = programs.split(",")
        return parsePrograms

    def Emails(confFile):
        CONF.read(confFile)
        emails = CONF.get('EXTENSION', 'Emails')
        parseEmails = emails.split(",")
        return parseEmails

    def FirefoxBrowser(confFile):
        CONF.read(confFile)
        firefoxBrowser = CONF.get('EXTENSION', 'FirefoxBrowser')
        parseFirefoxBrowser = firefoxBrowser.split(",")
        return parseFirefoxBrowser

    def ChromeBrowser(confFile):
        CONF.read(confFile)
        chromeBrowser = CONF.get('EXTENSION', 'ChromeBrowser')
        parseChromeBrowser = chromeBrowser.split(",")
        return parseChromeBrowser

    def Directories(confFile):
        CONF.read(confFile)
        directories = CONF.get('PATH', 'Directories')
        parseDirectories = directories.split(",")
        return parseDirectories

