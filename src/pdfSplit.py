#! /usr/bin/python

# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__="User"
__date__ ="$30.Eyl.2014 09:56:21$"

from lib.pyPDF2 import PdfFileWriter, PdfFileReader

##*****************************************************************************
# split pdf file as a given start and end page number
# int num int num --> pdf file
# param sourcefile is file to split execution
# param startPage is start page for splitter
# param endPage is end page for splitter
# result void because write splited file into same directory with splited+filename
def splitPdfFile(sourcefile, startPage, endPage):
    # read input file
    inputFile  = PdfFileReader(file(sourcefile, "rb"))

    # Check file is encrypted
    if inputFile.isEncrypted: 
        print "File is encrpted. Program is closed."
        return 
    
    #pageNo = startPage  
    output = PdfFileWriter()
    
    for pageNo in range(startPage-1,endPage):    
        output.addPage(inputFile.getPage(pageNo))
        
    
    # write page "output" to document-output.pdf
    outputStream = file(sourcefile.split(".")[0] +"_"+str(startPage)+"_"+str(endPage)+".pdf", "wb")
    output.write(outputStream)
    outputStream.close()
    print "Sipliting complete"

#TEST FUNCTION
splitPdfFile("testdir/test.pdf", 1, 2)
##*****************************************************************************