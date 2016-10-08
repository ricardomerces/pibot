#  This program use a Ultrasonic Module HC-SR04
#
#
#  Use BOARD NUMBER !
#  ------------------
#
#  TRIGGER --> Pin 31
#  ECHO    --> Pin 29
#

import RPi.GPIO as GPIO		
import time			

GPIO.setmode(GPIO.BOARD)	
GPIO.setwarnings(False)		

ECHO = 29
TRIG = 31

def Initialization():	
    GPIO.setup(ECHO,GPIO.IN)
    GPIO.setup(TRIG,GPIO.OUT)

def distance():
    GPIO.output(TRIG,GPIO.HIGH)
    time.sleep (0.000010)
    GPIO.output(TRIG,GPIO.LOW)
    while GPIO.input(ECHO) == 0:
        TriggerStart = time.time()
    while GPIO.input(ECHO) == 1:
        TriggerEnd = time.time()
    Trigger = TriggerEnd - TriggerStart
    Distance = Trigger * 17150
    Distance = round(Distance,0)
    print (Distance, 'cm' , end="\r")

Initialization()
while True:
    time.sleep(2)
    distance()
