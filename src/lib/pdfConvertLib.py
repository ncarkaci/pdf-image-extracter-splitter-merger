#! /usr/bin/python

# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__="User"
__date__ ="$01.Eki.2014 14:58:11$"

import os

#******************************************************************************
# Getting all files from specific directory as file extension
# String String --> List
# param path is directory path
# param extension is file extension
# result specific file list as file extension
def findAllSpecifiedFiles(path, extension):
    allSpecificFilesList = []
    allFiles = os.listdir(path);
    for filename in allFiles:
        ext = os.path.splitext(filename)[1][1:]
        if (extension == ext): allSpecificFilesList.append(filename)
    
    print  allSpecificFilesList
    return allSpecificFilesList
# TEST FUNCTION
# findAllSpecifiedFiles("../testdir","pdf")
# ['Practical Malware Analysis.pdf', 'strateji.pdf']    
#******************************************************************************
