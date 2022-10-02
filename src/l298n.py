import RPi.GPIO as GPIO   
import keyboard
from twilio.rest import Client   
import os   
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

def send_txt():
    os.system(f"python send_text.py")
    os.system(f"python play_sound.py")

################
##### MAIN #####
################
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
        elif(keyboard.is_pressed('y')):
            send_txt()
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