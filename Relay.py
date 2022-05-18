import time
import RPi.GPIO as GPIO

class relay:
     def __init__(self):
        self.pin=37
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.pin, GPIO.OUT)

     def run(self,OnOff):
        if OnOff==False:
                #GPIO.output(self.pin, GPIO.HIGH)
                print(self.pin)
                #time.sleep(1)
        else:
                GPIO.output(self.pin, GPIO.LOW)
                #time.sleep(1)
   
