#!/usr/bin/env python
#
# Library for file and directory operations.
#
# Author: Necmettin Çarkacı
# E-mail: necmettin [ . ] carkaci [ @ ] gmail [ . ] com
#
#Usage : 

import os

#******************************************************************************
#
# Getting all files from specific directory as file extension
#
# String String --> List
# param path is directory path
# param extension is file extension
# result specific file list as file extension
#******************************************************************************
def findAllSpecifiedFiles(path, extension):
    allSpecificFilesList = []
    allFiles = os.listdir(path);
    for filename in allFiles:
        ext = os.path.splitext(filename)[1][1:]
        if (extension == ext): allSpecificFilesList.append(filename)
    
    print  (allSpecificFilesList)
    return allSpecificFilesList
#*******************************************************************************
#
# TEST FUNCTION
# findAllSpecifiedFiles("../testdir","pdf")
# ['test_1_2.pdf', 'test.pdf']  
#******************************************************************************
