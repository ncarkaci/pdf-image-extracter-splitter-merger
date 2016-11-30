#!/usr/bin/env python
#
# Split pdf files as a given pages
# 
# Author: Necmettin Çarkacı
# E-mail: necmettin [ . ] carkaci [ @ ] gmail [ . ] com
#
# Usage : extractJpegFromPdf.py -f <filename> -d <directory name> -all -pnums <comma separated number list >
# Sample Usage : pdfSplit.py -f testdir/test.pdf -pnums 7,12 3,4 2,6 

from lib.pyPDF2 import PdfFileWriter, PdfFileReader
from lib.pdfConvertLib import *
import argparse

##*****************************************************************************
# split pdf file as a given start and end page number
# int num int num --> pdf file
# param sourcefile is file to split execution
# param startPage is start page for splitter
# param endPage is end page for splitter
# result void because write splited file into same directory with splited+filename
#
##*****************************************************************************
def splitPdfFile(sourcefile, startPage, endPage):
	
    # read input file
	inputPdf = PdfFileReader(open(sourcefile, "rb"))

	# Check file is encrypted
	if inputPdf.isEncrypted: 
		print ("File is encrpted. Program is closed.")
		return 
    
	output = PdfFileWriter()
    
	for pageNo in range(startPage-1, endPage):    
		output.addPage(inputPdf.getPage(pageNo))
        
    # write page "output" to document-output.pdf
	outputPdf = sourcefile.split(".")[0] +"_"+str(startPage)+"_"+str(endPage)+".pdf" 
	with open (outputPdf, "wb") as outputStream:
		output.write(outputStream)
	outputStream.close()
	print ("Sipliting complete : ", outputPdf)

##******************************************************************************
# TEST FUNCTION
# splitPdfFile("testdir/test.pdf", 1, 2)
#
##******************************************************************************

##*****************************************************************************
#
# Extract all pages 
#
# String String --> void
# param inputFileName is pdf file which is extracted
# param outputPath is a directory which extraxted file  write in
# result void
# warn : if pdf file is not end as a standart format, sometimes give error for the file
#
##*****************************************************************************
def splitAllPagesFromPdfFile(sourcefile):
        
    # read input file
	inputPdf = PdfFileReader(open(sourcefile, "rb"))

	# Check file is encrypted
	if inputPdf.isEncrypted: 
		print ("File is encrpted. Program is closed.")
		return 
    
	for pageNo in range (inputPdf.getNumPages()):
		output = PdfFileWriter()
		output.addPage(inputPdf.getPage(pageNo))

		# write page "output" to document-output.pdf
		outputPdf = sourcefile.split(".")[0] +"_"+str(pageNo+1)+".pdf" 
		with open (outputPdf, "wb") as outputStream:
			output.write(outputStream)
		outputStream.close()
		print ("Sipliting complete : ", outputPdf)
        
	print ("All pages splited.")

##*****************************************************************************
# TEST FUNCTION
# splitAllPagesFromPdfFile("testdir/test.pdf")
##*****************************************************************************


##*****************************************************************************
# Get a directory and return pdf files which are has one page and produced other pdf's
##*****************************************************************************
def splitAllPdfFilesInDirectory(inputDirectory):
	allPdfFiles = findAllSpecifiedFiles(inputDirectory,"pdf")
    
	for file in allPdfFiles:
		splitAllPagesFromPdfFile(inputDirectory+os.sep+file)

##****************************************************************************** 
# TEST FUNCTION 
# splitAllPdfFilesInDirectory ("testdir")
##*****************************************************************************

if __name__ == '__main__':

	parser = argparse.ArgumentParser()
	parser.add_argument("-f", help = "filename")
	parser.add_argument("-d", help = "directory name")
	parser.add_argument("-all", action='store_true', help = "split all pages")
	parser.add_argument("-pnums", nargs = '*', help = "split page numbers")
	args = parser.parse_args()

	if args.f :
		if args.all  :
			splitAllPagesFromPdfFile(args.f)
		if args.pnums :								
			for pagePair in args.pnums :
				start, end = pagePair.split(",") 
				print (start, end)
				splitPdfFile(args.f, int(start), int(end))
	elif args.d :
		splitAllPdfFilesInDirectory (args.d)
	else :
		print ("Usage : extractJpegFromPdf.py -f <filename> -all -pnums <comma separated number list >")
		print ("Sample Usage : pdfSplit.py -f testdir/test.pdf -pnums 7,12 3,4 2,6")

