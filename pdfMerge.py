#!/usr/bin/env python
#
# Merge pdf file list
# 
# Author: Necmettin Çarkacı
# E-mail: necmettin [ . ] carkaci [ @ ] gmail [ . ] com
#
# Usage : pdfMerge.py -f  < comma separated file list> -d <directory path>
# Sample Usage : pdfMerge.py -f  test1.pdf, test2.pdf, test3.pdf -d testdir/ 

from lib.pdfConvertLib import *
import argparse, os

try :
	from lib.pyPDF2 import merger, PdfFileReader, PdfFileMerger
except :
	
	

def mergePdfFiles(pdfFileList):
	
	merger = PdfFileMerger()
	
	for filename in pdfFileList:
	    merger.append(PdfFileReader(open(filename, 'rb')))

	merger.write("mergedPdf.pdf")
	print ("Merge complted. Merge file : mergedPdf.pdf")

##*****************************************************************************
# Get a directory and return merge pdf files
##*****************************************************************************
def mergeAllPdfFilesInDirectory(inputDirectory):
	allPdfFiles = findAllSpecifiedFiles(inputDirectory,"pdf")
    
	for file in allPdfFiles:
		mergePdfFiles(inputDirectory+os.sep+file)

##****************************************************************************** 
# TEST FUNCTION 
# mergeAllPdfFilesInDirectory ("testdir")
##*****************************************************************************

if __name__ == '__main__':

	parser = argparse.ArgumentParser()
	parser.add_argument("-f", nargs = '*', help = "file list")
	parser.add_argument("-d", help = "directory list")
	args = parser.parse_args()

	if args.f :
		mergePdfFiles(args.f)
	elif args.d :
		mergeAllPdfFilesInDirectory(args.d)
	else :
		print ( "Usage : pdfMerge.py -f  < comma separated file list> -d <directory path>" )
		print ( "Sample Usage : pdfMerge.py -f  test1.pdf, test2.pdf, test3.pdf -d testdir/" )


