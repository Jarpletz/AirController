import time
import threading
import ParticleSensor
import TempSensor
import Oled

#TO ACCESS Manager Use this code:
#include Manager
# manager=Manager.manager
# if manager.useFan: #do stuff

class Manager:
    def __init__(self, *args, **kwargs):
        self.ssd=Oled.display() #OLED
        self.sht=TempSensor.tempSensor() #Temp sensor
        self.pms=ParticleSensor.particleSensor() #Particle Sensor
        
        self.useFan= False


    def updateSensors(self): #Updates data from temp and particle sensor
        self.sht.update()
        self.pms.update()


    def displayOledTempInfo(self): #Displays temp and humid info on the OLED
        self.ssd.clear()   #clear
        self.ssd.displayText("Temperature & Humidity",0,0,)  #Header
        self.ssd.displayText(self.sht.getTempString(),0,16)   #display temp
        self.ssd.displayText(self.sht.getHumidString(),0,32) #display Humidity
        self.ssd.show()    #show page

    def displayOledParticleInfo(self): #Displays Air Quality Data on the OLED
        self.ssd.clear() #clear oled
        self.ssd.displayText("Air Quality: Excellent",0,0)  #Header and state
        if self.useFan:
            self.ssd.displayText("Fan: On",0,16)
        else:
            self.ssd.displayText("Fan: OFf",0,16)
        #Display pms data
        self.ssd.show()

    def runOled(self):# Function called with threading that alternates between showing the temp and showing the Particle data on the oled every 5 sec.
        while(1):
            self.updateSensors()
            self.displayOledTempInfo()
            print("Temp info")
            time.sleep(5)
            self.displayOledParticleInfo()
            print("Particle info")
            time.sleep(5)


        

        
       
manager=Manager()
oledFunction= threading.Thread(target=manager.runOled, args=())
oledFunction.start()

