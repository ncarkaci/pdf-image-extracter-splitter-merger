#! /usr/bin/python

# Extract jpeg file from pdf file.

__author__="User"
__date__ ="$01.Eki.2014 15:07:15$"

from lib.pdfConvertLib import *
import sys

##******************************************************************************
# Extract jpeg file from pdf. It used below url
# url : http://nedbatchelder.com/blog/200712/extracting_jpgs_from_pdfs.html
# String --> Void
# param filename is source pdf file
# result pdf void because result file written in same directory 
# warn : It is execute iterativly. Think about this.
##*****************************************************************************
def extractJPEGfilesFromPdf(filename):
    
    pdfFile = file(filename, "rb").read()

    # the starting and ending bytes of a JPEG image.
    # http://en.wikipedia.org/wiki/JPEG#Syntax_and_structure
    startBytesofJPEG = "\xff\xd8"
    startfix = 0
    endBytesofJPEG   = "\xff\xd9"
    endfix   = 2
    
    i = 0
    numberofJPEG = 0 # First time for jpeg number
    
    while True:
        istream = pdfFile.find("stream", i)
        if istream < 0:
            break
        istart = pdfFile.find(startBytesofJPEG, istream, istream+20)
        if istart < 0:
            i = istream+20
            continue
        iend = pdfFile.find("endstream", istart)
        if iend < 0:
            raise Exception("Didn't find end of stream!")
        iend = pdfFile.find(endBytesofJPEG, iend-20)
        if iend < 0:
            raise Exception("Didn't find end of JPG!")
     
        istart += startfix
        iend += endfix
        print "JPG %d from %d to %d" % (numberofJPEG, istart, iend)
        jpg = pdfFile[istart:iend]
        jpgfile = file(filename+"_jpg_%d.jpg" % numberofJPEG, "wb")
        jpgfile.write(jpg)
        jpgfile.close()
        print "Create : "+filename+"_jpg_%d.jpg" % numberofJPEG
     
        numberofJPEG += 1
        i = iend
##******************************************************************************        
# TEST FUNTIONS
# extractJPEGfilesFromPdf("testdir/Adam_Smith_-_Milletlerin_Zenginli.pdf")
#*******************************************************************************


##******************************************************************************
# Extract jpeg from pdf files which stay in specific directory
#
#
#*******************************************************************************
def extractJpegFileFromPdfsIndir(directoryPath):
    allPdfFiles = findAllSpecifiedFiles(directoryPath,"pdf")
    
    for file in allPdfFiles:
        extractJPEGfilesFromPdf(directoryPath+os.sep+file)
##******************************************************************************
##TEST FUNCTION
extractJpegFileFromPdfsIndir("testdir")