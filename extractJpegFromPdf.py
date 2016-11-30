#!/usr/bin/env python
#
# Extract jpeg files from pdf files into directory.
# Use jpeg and png start end byte. It search document step by step with simple and dirty techniques.
# Author: Necmettin Çarkacı
# E-mail: necmettin [ . ] carkaci [ @ ] gmail [ . ] com
#
# Usage : extractJpegFromPdf.py -f <filename> -d <directoryPath>


from lib.pdfConvertLib import *
import sys, argparse

##******************************************************************************
#
# Extract jpeg file from pdf. It used below url
# url : http://nedbatchelder.com/blog/200712/extracting_jpgs_from_pdfs.html
#
# String --> Void
# param filename is source pdf file
# result pdf void because result file written in same directory 
# warn : It is execute iterativly. Think about this.
#
##*****************************************************************************
def extractJPEGfilesFromPdf(filename):

	with open(filename, "rb") as file:
		pdf = file.read()

	# the starting and ending bytes of a JPEG image.
	# http://en.wikipedia.org/wiki/JPEG#Syntax_and_structure
	startBytesofJPEG = b"\xff\xd8"
	startfix = 0
	endBytesofJPEG = b"\xff\xd9"
	endfix = 2
	i = 0

	numberofJPEG = 0 # First time for jpeg number

	while True:
		istream = pdf.find(b"stream", i)
		if istream < 0:
		    break
		istart = pdf.find(startBytesofJPEG, istream, istream + 20)
		if istart < 0:
		    i = istream + 20
		    continue
		iend = pdf.find(b"endstream", istart)
		if iend < 0:
		    raise Exception("Didn't find end of stream!")
		iend = pdf.find(endBytesofJPEG, iend - 20)
		if iend < 0:
		    raise Exception("Didn't find end of JPG!")

		istart += startfix
		iend += endfix
		print("JPG %d from %d to %d" % (numberofJPEG, istart, iend))
		jpg = pdf[istart:iend]

		# write jpeg file		
		with open("jpg_%d.jpg" % numberofJPEG, "wb") as jpgfile:
		    jpgfile.write(jpg)

		numberofJPEG += 1
		i = iend    

##******************************************************************************        
# TEST FUNCTIONS
# extractJPEGfilesFromPdf("testdir/test.pdf")
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
# TEST FUNCTION
# extractJpegFileFromPdfsIndir("testdir")
#*******************************************************************************

if __name__ == '__main__':

	parser = argparse.ArgumentParser()
	parser.add_argument("-f", help="filename")
	parser.add_argument("-d", help="directory path")
	args = parser.parse_args()

	if args.d :
		 extractJpegFileFromPdfsIndir(args.d)
	elif args.f :
		extractJPEGfilesFromPdf(args.f)
	else :
		print ("Usage : extractJpegFromPdf.py -f <filename> -d <directoryPath>")

