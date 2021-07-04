import PyPDF2
import sys

file1 = open(sys.argv[1], 'rb')
file2 = open(sys.argv[2], 'rb')

reader1 = PyPDF2.PdfFileReader(file1)
reader2 = PyPDF2.PdfFileReader(file2)

writer = PyPDF2.PdfFileWriter()

for pageNum in range(reader1.numPages):
    page = reader1.getPage(pageNum)
    writer.addPage(page)
    
for pageNum in range(reader2.numPages):
    page = reader2.getPage(pageNum)
    writer.addPage(page)
    
outputFile = open('combine.pdf', 'wb')
writer.write(outputFile)

outputFile.close()
file1.close()
file2.close()