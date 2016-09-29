#  This program use a L298N Dual Motor Controller(module)
#
#  Use BOARD NUMBER !
#  ------------------
#
#  RIGHT MOTOR FORWARD--> Pin 16
#  RIGHT MOTOR REVERSE--> Pin 18
#  LEFT  MOTOR FORWARD--> Pin 13
#  LEFT  MOTOR REVERSE--> Pin 15
#

import RPi.GPIO as GPIO		#import GPIO Library
import time			#import time Library
import getch			#import single-char input Library

GPIO.setmode(GPIO.BOARD)	#GPIO -board number 
GPIO.setwarnings(False)		#Disable messages

def Initialization():		#set pins as output	
  GPIO.setup(13,GPIO.OUT)	
  GPIO.setup(15,GPIO.OUT)		
  GPIO.setup(16,GPIO.OUT)	
  GPIO.setup(18,GPIO.OUT)

def MoveStop():			#stop ALL
  GPIO.output(13,GPIO.LOW)	
  GPIO.output(15,GPIO.LOW)	
  GPIO.output(16,GPIO.LOW)
  GPIO.output(18,GPIO.LOW)	

def MoveFoward():		#Move Forward
  GPIO.output(16,GPIO.HIGH)		
  GPIO.output(13,GPIO.HIGH)		
  time.sleep(0.4)
  GPIO.output(16,GPIO.LOW)		
  GPIO.output(13,GPIO.LOW)		
      
def MoveReverse():		#Move Reverse
  GPIO.output(18,GPIO.HIGH)		
  GPIO.output(15,GPIO.HIGH)		
  time.sleep(0.4)
  GPIO.output(18,GPIO.LOW)	
  GPIO.output(15,GPIO.LOW)

def MoveRight():		#Move Right
  GPIO.output(13,GPIO.HIGH)
  time.sleep(0.2)
  GPIO.output(13,GPIO.LOW)

def MoveLeft():			#Move Left
  GPIO.output(16,GPIO.HIGH)		
  time.sleep(0.2)
  GPIO.output(16,GPIO.LOW)	

Initialization()

print("""\

|------------------|
|    CONTROLS:     |
|   __      __     |
|   \ \ /\ / /     |
|    \ V  V /      |
|     \_/\_/       |
|               _  |
|  __ _ ___  __| | |
| / _` / __|/ _` | |
| |(_| \__ \ (_| | |
| \__,_|___/\__,_| |
|                  |
| o --> stop ALL   |
| q --> quit       |
|------------------|

""")


while True:
  InputKEY= getch.getch()
  if InputKEY == 'w':
    MoveFoward()
  elif InputKEY == 's':
    MoveReverse()
  elif InputKEY == 'd':
    MoveRight()
  elif InputKEY == 'a':
    MoveLeft()
  elif InputKEY == 'o':
    MoveStop()
  elif InputKEY == 'q':
    break
