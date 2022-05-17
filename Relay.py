import time
import RPi.GPIO as GPIO
import Manager

class relay:
    def run(OnOff):
        if OnOff==True:
                GPIO.output(pin, GPIO.HIGH)
                time.sleep(1)
        else:
                GPIO.output(pin. GPIO.LOW)
                time.sleep(1)
    def __init_(self, OnOff):
        self.pin=37
        self.GPIO.setmode(GPIO.BOARD)
        self.GPIO.setup(pin, GPIO.OUT)
