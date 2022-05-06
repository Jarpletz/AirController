import time
import ParticleSensor
import TempSensor
import Oled

class Manager:
    def __init__(self, *args, **kwargs):
        self.ssd=Oled.display() #OLED
        self.sht=TempSensor.tempSensor() #Temp sensor
        self.pms=ParticleSensor.particleSensor() #Particle Sensor
        
        self.useFan= False


    def updateSensors(self): #Updates data from temp and particle sensor
        self.sht.update()
        self.pms.update()


    def displayOledTempInfo(self):
        self.ssd.clear()   #clear
        self.ssd.displayText("Temperature & Humidity",0,0,)  #Header
        self.ssd.displayText(self.sht.getTempString(),0,9)   #display temp
        self.ssd.displayText(self.sht.getHumidString(),0,18) #display Humidity
        self.ssd.show()    #show page

    def displayOledParticleInfo(self):
        self.ssd.clear() #clear
        self.ssd.displayText("Air Quality: Excellent",0,0)  #Header and state
        self.ssd
        
       
