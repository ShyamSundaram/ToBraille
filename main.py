import pdf_image
import text_recognition
import os

def from_image(imgname):
    #os.system('python text_recognition.py --east frozen_east_text_detection.pb --image '+imgname)
    t=text_recognition.main(imgname)
    print(t)

def from_pdf(pdfname):
    t=pdf_image.to_image(pdfname)
    print(t)

from_image('unnamed320.jpg')
#from_pdf('test2.pdf')