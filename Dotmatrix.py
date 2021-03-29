# from pyfirmata import Arduino, util
# import time

# board = Arduino('COM3')

# board.digital[13].write(0)
import serial #for Serial communication
import time   #for delay functions
 
arduino = serial.Serial('COM3',9600) #Create Serial port object called arduinoSerialData
time.sleep(2) #wait for 2 secounds for the communication to get established

print(arduino.readline()) #read the serial data and print it as line
print ("Start")

var=input()

for i in var:
    arduino.write(bytes(i,'utf-8'))
    time.sleep(1)
    print(i)
 
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