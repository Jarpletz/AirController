import time
import ParticleSensor
import TempSensor
import Oled

class Manager:
    def __init__(self, *args, **kwargs):
        self.ssd=Oled.display() #OLED
        self.sht=TempSensor.tempSensor() #Temp sensor
        self.pms=ParticleSensor.particleSensor() #Particle Sensor

    def updateSensors(self): #Updates data from temp and particle sensor
        self.sht.update()
        self.pms.update()

       
