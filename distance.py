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

def initialization():	
    GPIO.setup(ECHO,GPIO.IN)
    GPIO.setup(TRIG,GPIO.OUT)

def distance():
    while True:
        time.sleep(2)
        GPIO.output(TRIG,GPIO.HIGH)
        time.sleep (0.000010)
        GPIO.output(TRIG,GPIO.LOW)
        while GPIO.input(ECHO) == 0:
            pulse_start = time.time()
        while GPIO.input(ECHO) == 1:
            pulse_end = time.time()
        pulse = pulse_end - pulse_start
        distance = pulse/2 * 34300  # 343m/s Speed of Sound
        distance = round(distance,0)
        print (distance, 'cm   ' , end="\r")

initialization()
distance()
