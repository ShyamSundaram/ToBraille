# from pyfirmata import Arduino, util
# import time

# board = Arduino('COM3')


# board.digital[13].write(0)
import serial #for Serial communication
import time   #for delay functions
import pdf_to_braille
import main
#  DIN connects to pin 12
#  CLK connects to pin 11
#  CS connects to pin 10 

arduino = serial.Serial('COM3',9600) #Create Serial port object called arduinoSerialData
time.sleep(2) #wait for 2 secounds for the communication to get established

print(arduino.readline()) #read the serial data and print it as line
print ("Start")
print("1. PDF\n2. Image\n3. Speech ")
ch=int(input("Choice: "))

if(ch==1):
    filen=input()
    var=main.from_pdf(filen)#pdf_to_braille.toText(filen)#('test2.pdf')#input()
elif (ch==2):
    filen=input()
    var=main.from_image(filen)
elif (ch==3):
    var=main.from_speech()
print(var)
arduino.write(bytes(var,'utf-8'))

# for i in var:
#     arduino.write(bytes(i,'utf-8'))
#     time.sleep(2)
#     print(i)
 
# while 1:      #Do this in loop
#     var = input() #get input from user
#     arduino.write(bytes(var,'utf-8'))
#     if (var == 'y'): #if the value is 1
#         #arduino.write(b'1') #send 1
#         print ("LED turned ON")
#         time.sleep(1)
    
#     if (var == 'n'): #if the value is 0
#         #arduino.write(b'0') #send 0
#         print ("LED turned OFF")
#         time.sleep(1)