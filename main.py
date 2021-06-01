import pdf_image
import text_recognition
#import pdf_to_text
import pdf_to_braille
import speech_to_text
import os

def from_image(imgname):
    #os.system('python text_recognition.py --east frozen_east_text_detection.pb --image '+imgname)
    t=text_recognition.main(imgname)
    print(t)
    res=""
    for i in t:
        res=res+" "+i
    return res.lower()

def from_pdf(pdfname):
    #t=pdf_image.to_image(pdfname)
    t=pdf_to_braille.toText(pdfname)
    print(t)
    return t
    #pdf_to_text.pdf_to_braille(pdfname)
    #print(t)

def from_speech():
    tex=speech_to_text.get_speech_text()
    return tex

#from_image('unnamed320.jpg')
#from_pdf(r"E:\Academics\VIT\Project\Microprocessor\Code\test2.pdf")