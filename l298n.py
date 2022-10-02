# Python Script
# https://www.electronicshub.org/raspberry-pi-l298n-interface-tutorial-control-dc-motor-l298n-raspberry-pi/

import RPi.GPIO as GPIO   
import keyboard       
from time import sleep

in1 = 15
in2 = 14
in3 = 23
in4 = 24
ena = 18
enb = 25
temp1=1

GPIO.setmode(GPIO.BCM)

GPIO.setup(in1,GPIO.OUT)
GPIO.setup(in2,GPIO.OUT)
GPIO.setup(in3,GPIO.OUT)
GPIO.setup(in4,GPIO.OUT)
GPIO.setup(ena,GPIO.OUT)
GPIO.setup(enb,GPIO.OUT)

GPIO.output(in1,GPIO.LOW)
GPIO.output(in2,GPIO.LOW)
GPIO.output(in3,GPIO.LOW)
GPIO.output(in4,GPIO.LOW)

p1=GPIO.PWM(ena,1000)
p2=GPIO.PWM(enb,1000)

duty_cycle = 50

p1.start(duty_cycle)
p2.start(duty_cycle)

def move(direction):
    GPIO.output(ena, GPIO.HIGH)
    GPIO.output(enb, GPIO.HIGH)
    
    if(direction=="FWD"):
        print("forward")
        GPIO.output(in1, GPIO.LOW)
        GPIO.output(in2, GPIO.HIGH)
        GPIO.output(in3, GPIO.LOW)
        GPIO.output(in4, GPIO.HIGH)
 
    elif(direction=="BCKWD"):
        print("backward")
        GPIO.output(in1, GPIO.HIGH)
        GPIO.output(in2, GPIO.LOW)
        GPIO.output(in3, GPIO.HIGH)
        GPIO.output(in4, GPIO.LOW)       
    elif(direction=="LEFT"):
        print("left")
        GPIO.output(in1, GPIO.LOW)
        GPIO.output(in2, GPIO.HIGH)
        GPIO.output(in3, GPIO.LOW)
        GPIO.output(in4, GPIO.LOW)
    elif(direction=="RIGHT"):
        print("right")
        GPIO.output(in1, GPIO.LOW)
        GPIO.output(in2, GPIO.LOW)
        GPIO.output(in3, GPIO.LOW)
        GPIO.output(in4, GPIO.HIGH)
        
def change_duty_cycle(amount):
    tmp = duty_cycle + amount
    print(tmp)
    if(tmp >= 10 or tmp <= 100):
        duty_cycle = tmp
        p1.ChangeDutyCycle(duty_cycle)
        p2.ChangeDutyCycle(duty_cycle)
    
#     p1.ChangeDutyCycle(duty_cycle)
#     p2.ChangeDutyCycle(duty_cycle)
    

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
        elif(keyboard.is_pressed('p')):
            if(duty_cycle+10 <= 100):
                duty_cycle += 10
            p1.ChangeDutyCycle(duty_cycle)
            p2.ChangeDutyCycle(duty_cycle)
        elif(keyboard.is_pressed('o')):
            if(duty_cycle-10 >= 10):
                duty_cycle -= 10
            p1.ChangeDutyCycle(duty_cycle)
            p2.ChangeDutyCycle(duty_cycle)
    except:
        continue
    
    sleep(.1)
    GPIO.output(in1, GPIO.LOW)
    GPIO.output(in2, GPIO.LOW)
    GPIO.output(in3, GPIO.LOW)
    GPIO.output(in4, GPIO.LOW)
    GPIO.output(ena, GPIO.LOW)
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