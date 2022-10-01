# Python Script
# https://www.electronicshub.org/raspberry-pi-l298n-interface-tutorial-control-dc-motor-l298n-raspberry-pi/

import RPi.GPIO as GPIO   
import keyboard       
from time import sleep

in4 = 24
in3 = 23
enb = 25
temp1=1

# GPIO.setwarnings(False)

GPIO.setmode(GPIO.BCM)
GPIO.setup(in4,GPIO.OUT)
GPIO.setup(in3,GPIO.OUT)
GPIO.setup(enb,GPIO.OUT)
GPIO.output(in4,GPIO.LOW)
GPIO.output(in3,GPIO.LOW)
# p=GPIO.PWM(enb,1000)

def move(direction):
    GPIO.output(enb, GPIO.HIGH)
    if(direction=="FWD"):
        print("forward")
        GPIO.output(in4, GPIO.HIGH)
        GPIO.output(in3, GPIO.LOW)
    elif(direction=="BCKWD"):
        print("backward")
        GPIO.output(in4, GPIO.LOW)
        GPIO.output(in3, GPIO.HIGH)
    elif(direction=="LEFT"):
        print("left")
    elif(direction=="RIGHT"):
        print("right")

while(1):
    try:
        if(keyboard.is_pressed('esc')):
            print("Exiting program...")
            break
        elif(keyboard.is_pressed('w')):
            move("FWD")
        elif(keyboard.is_pressed('s')):
            move("BCKWD")
        elif(keyboard.is_pressed('a')):
            move("LEFT")
        elif(keyboard.is_pressed('d')):
            move("RIGHT")
    except:
        continue
    sleep(.1)
    GPIO.output(in4, GPIO.LOW)
    GPIO.output(in3, GPIO.LOW)
    GPIO.output(enb, GPIO.LOW)

    
GPIO.cleanup()

# p.start(25)
# print("\n")
# print("The default speed & direction of motor is LOW & Forward.....")
# print("r-run s-stop f-forward b-backward l-low m-medium h-high e-exit")
# print("\n")    

# while(1):

#     x=raw_input()
    
#     if x=='r':
#         print("run")
#         if(temp1==1):
#          GPIO.output(in4,GPIO.HIGH)
#          GPIO.output(in3,GPIO.LOW)
#          print("forward")
#          x='z'
#         else:
#          GPIO.output(in4,GPIO.LOW)
#          GPIO.output(in3,GPIO.HIGH)
#          print("backward")
#          x='z'


#     elif x=='s':
#         print("stop")
#         GPIO.output(in4,GPIO.LOW)
#         GPIO.output(in3,GPIO.LOW)
#         x='z'

#     elif x=='f':
#         print("forward")
#         GPIO.output(in4,GPIO.HIGH)
#         GPIO.output(in3,GPIO.LOW)
#         temp1=1
#         x='z'

#     elif x=='b':
#         print("backward")
#         GPIO.output(in4,GPIO.LOW)
#         GPIO.output(in3,GPIO.HIGH)
#         temp1=0
#         x='z'

#     elif x=='l':
#         print("low")
#         p.ChangeDutyCycle(25)
#         x='z'

#     elif x=='m':
#         print("medium")
#         p.ChangeDutyCycle(50)
#         x='z'

#     elif x=='h':
#         print("high")
#         p.ChangeDutyCycle(75)
#         x='z'
     
    
#     elif x=='e':
#         GPIO.cleanup()
#         print("GPIO Clean up")
#         break
    
#     else:
#         print("<<<  wrong data  >>>")
#         print("please enbter the defined data to continue.....")