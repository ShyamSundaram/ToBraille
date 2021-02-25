import PyPDF2

obj=open('test.pdf','rb')
pdf=PyPDF2.PdfFileReader(obj)
print(pdf.getPage(0).extractText())
obj.close()