# -*- coding: utf-8 -*-

#---------------------------------------------------------- [Lib] -----------------------------------------------------------#

import configparser

#--------------------------------------------------------- [Global] ---------------------------------------------------------#

conf = configparser.ConfigParser()

#--------------------------------------------------- [Function(s)/Class] ----------------------------------------------------#
    
class ExtConf():

    def Databases(confFile):
        conf.read(confFile)
        databases = conf.get('EXTENSION', 'Databases')
        parseDatabases = databases.split(",")
        return parseDatabases

    def Docs(confFile):
        conf.read(confFile)
        docs = conf.get('EXTENSION', 'Docs')
        parseDocs = docs.split(",")
        return parseDocs

    def Pictures(confFile):
        conf.read(confFile)
        pictures = conf.get('EXTENSION', 'Pictures')
        parsePictures = pictures.split(",")
        return parsePictures

    def Compress(confFile):
        conf.read(confFile)
        compress = conf.get('EXTENSION', 'Compress')
        parseCompress = compress.split(",")
        return parseCompress

    def Programs(confFile):
        conf.read(confFile)
        programs = conf.get('EXTENSION', 'Programs')
        parsePrograms = programs.split(",")
        return parsePrograms

    def Emails(confFile):
        conf.read(confFile)
        emails = conf.get('EXTENSION', 'Emails')
        parseEmails = emails.split(",")
        return parseEmails

    def FirefoxBrowser(confFile):
        conf.read(confFile)
        firefoxBrowser = conf.get('EXTENSION', 'FirefoxBrowser')
        parseFirefoxBrowser = firefoxBrowser.split(",")
        return parseFirefoxBrowser

    def ChromeBrowser(confFile):
        conf.read(confFile)
        chromeBrowser = conf.get('EXTENSION', 'ChromeBrowser')
        parseChromeBrowser = chromeBrowser.split(",")
        return parseChromeBrowser


class DirsConf:

    def Directories(confFile):
        conf.read(confFile)
        directories = conf.get('PATH', 'Directories')
        parseDirectories = directories.split(",")
        return parseDirectories

