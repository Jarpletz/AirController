import time
import RPi.GPIO as GPIO

class relay:
     def __init__(self):
        self.pin=6
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pin, GPIO.OUT)
     def run(self,OnOff):
        if OnOff==True:
                GPIO.output(self.pin, GPIO.HIGH)
                print("Relay HIGH")
                #time.sleep(1)
        else:
                GPIO.output(self.pin, GPIO.LOW)
                print("Relay LOW")
                #time.sleep(1)
   
