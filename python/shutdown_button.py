import RPi.GPIO as GPIO  ##  library that lets you control the Pi's GPIO pins
import os  ##  allows us to talk to the system like in the terminal
from sys import exit  ##  allows us to use "exit"
from time import sleep  ##  allows us to use "sleep"

GPIO.setwarnings(False)  ##  disables messages about GPIO pins already being in use
GPIO.setmode(GPIO.BOARD)  ##  indicates which pin numbering configuration to use
 
GPIO.setup(16, GPIO.IN)  ##  tells it that pin 16 (button) will be giving input
GPIO.setup(18, GPIO.IN)  ##  tells it that pin 18 (button) will be giving input
GPIO.setup(7, GPIO.OUT)  ##  tells it that pin 7 (LED) will be outputting
GPIO.output(7, GPIO.HIGH)  ##  sets pin 7 (LED) to "HIGH" or off


##  this while loop constantly looks for button input (presses)
while True:
    ##  if no power button press
    if (GPIO.input(16) == False):
             print "button off. flash led"
             GPIO.output(7,True) ##  switch on pin 7 (LED)
             sleep(0.5) ##  wait for 0.5 second
             GPIO.output(7,False) ##  switch off pin 7 (LED)
             sleep(1) ##  wait for 1 second
 
    ##  when button is pressed
    else:
             print "button pressed. shutting down"
             GPIO.output(7,True)
             sleep(0.2) 
             GPIO.output(7,False)
             sleep(0.2)
             GPIO.output(7,True)
             sleep(0.2)
             GPIO.output(7,False)
             sleep(3)
             GPIO.output(7,GPIO.HIGH)  ##  turn pin 7 (LED) off
              ##  script to be called
             os.system("sudo shutdown -h now")  ##  shuts down Pi

    ##  if no reset button press
    if (GPIO.input(18) == False):
             print "reset button off. flash led"
             GPIO.output(7,True) ##  switch on pin 7 (LED)
             sleep(0.5) ##  wait for 0.5 second
             GPIO.output(7,False) ##  switch off pin 7 (LED)
             sleep(1) ##  wait for 1 second
 
    ##  when button is pressed
    else:
             print "reset button pressed. shutting down"
             GPIO.output(7,True)
             sleep(0.1) 
             GPIO.output(7,False)
             sleep(0.1)
             GPIO.output(7,True)
             sleep(0.1)
             GPIO.output(7,False)
             sleep(0.1)
             GPIO.output(7,True)
             sleep(0.1)
             GPIO.output(7,False)
             sleep(3)
             GPIO.output(7,GPIO.HIGH)  ##  turn pin 7 (LED) off
              ##  script to be called
             os.system("sudo restart -h now")  ##  restarts Pi

exit()  ##  terminates this script

