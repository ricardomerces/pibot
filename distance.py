#  This program use a Ultrasonic Module HC-SR04
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
TRIGGER = 31

def Initialization():	
    GPIO.setup(ECHO,GPIO.OUT)
    GPIO.setup(TRIGGER,GPIO.IN)

def distance():
    GPIO.output(ECHO,GPIO.HIGH)
    time.sleep (0.000010)
    GPIO.output(ECHO,GPIO.LOW)
    while GPIO.input(TRIGGER) == 0:
        TriggerStart = time.time()
    while GPIO.input(TRIGGER) == 1:
        TriggerEnd = time.time()
    Trigger = TriggerEnd - TriggerStart
    Distance = Trigger / 0.000058
    Distance = round(Distance,2)
    print (Distance, 'cm')

Initialization()
while True:
    time.sleep(1)
    distance()
