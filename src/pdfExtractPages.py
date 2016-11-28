# The pdf file converting project. In the project pdf file split and convert another pdf file or jpeg file.
# For my wife : )

__author__="User"
__date__ ="$25.Eyl.2014 16:50:59$"

# For pdf operation it use python pure pdf library
# url : https://github.com/mstamy2/PyPDF2
from lib.pyPDF2 import PdfFileWriter, PdfFileReader
from lib.pdfConvertLib import *
import os


##*****************************************************************************
# Extract all pages 
# String String --> void
# param inputFileName is pdf file which is extracted
# param outputPath is a directory which extraxted file  write in
# result void
# warn : if pdf file is not end as a standart format, sometimes give error for the file
##*****************************************************************************
def extractAllPagesFromPdfFile(inputFileName, outputPath):
    
    # cretae output folder
    if not os.path.exists(outputPath): os.makedirs(outputPath)
    
    # read input file
    inputFile  = PdfFileReader(file(inputFileName, "rb"))
    print inputFile.getDocumentInfo()
    # Check file is encrypted
    if inputFile.isEncrypted: 
        print "File is encrpted. Program is closed."
        return 
    
    for pageNo in range (inputFile.getNumPages()):
        output = PdfFileWriter()
        output.addPage(inputFile.getPage(pageNo))
        
        # write page "output" to document-output.pdf
        path, filename = os.path.split(inputFileName)
        outputStream = file(outputPath+filename.split(".")[0] +"_"+str(pageNo)+".pdf", "wb")
        output.write(outputStream)
        outputStream.close()
        print "Create : "+outputPath+filename.split(".")[0] +"_"+str(pageNo)+".pdf"
    print "Extraction complete"
#TEST FUNCTION
# extractAllPagesFromPdfFile("testdir/strateji.pdf","testdir/output/")
##*****************************************************************************


##*****************************************************************************
# Get a directory and return pdf files which are has one page and produced other pdf's
def extractAllPdfFiles (inputDirectory, outputDirectory):
    allPdfFiles = findAllSpecifiedFiles(inputDirectory,"pdf")
    
    for file in allPdfFiles:
        extractAllPagesFromPdfFile(inputDirectory+os.sep+file,outputDirectory)

# TEST FUNCTION 
extractAllPdfFiles ("testdir", "testdir/output/")
##*****************************************************************************

