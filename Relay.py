import time
import RPi.GPIO as GPIO

class relay:
     def __init__(self):
        self.pin=37
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.pin, GPIO.OUT)

        if OnOff==False:
                GPIO.output(self.pin, GPIO.HIGH)
                print("Relay HIGH")
                #time.sleep(1)
        else:
                GPIO.output(self.pin, GPIO.LOW)
                print("Relay LOW")
                #time.sleep(1)
   
