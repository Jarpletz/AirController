import time
import RPi.GPIO as GPIO

class relay:
     def __init_(self):
        self.pin=37
        self.GPIO.setmode(GPIO.BOARD)
        self.GPIO.setup(self.pin, self.GPIO.OUT)

     def run(self,OnOff):
        if OnOff==False:
                self.GPIO.output(self.pin, self.GPIO.HIGH)
                #time.sleep(1)
        else:
                self.GPIO.output(self.pin. self.GPIO.LOW)
                #time.sleep(1)
   
