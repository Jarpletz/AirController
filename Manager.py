import time
import threading
import ParticleSensor
import TempSensor
#import SaveData
import Oled
import Relay

#TO ACCESS Manager Use this code:
#include Manager
# manager=Manager.manager
# if manager.useFan: #do stuff   


class Manager:
    def __init__(self, *args, **kwargs):
        self.ssd=Oled.display() #OLED
        self.sht=TempSensor.tempSensor() #Temp sensor
        self.pms=ParticleSensor.particleSensor() #Particle Sensor
        self.fan=Relay.relay() #Relay object

        #self.saver=SaveData.saveData()
        #self.saver.readData() #Data Saver class, Read data previously stored
        
        self.useFan= False #True if fan on, False if fan off
        self.overrideAmount=900 # time, in seconds, the override will last
        self.overrideLeft=0 #Time left, in seconds, during which the sensor data should be overridden for fan
        self.previousTime=time.time() #a way to keep track of the time passed per frame

        self.updateFrequency=900 #the amount of time, in seconds, between each time sensor data is measured. Saves data every other measurement (900 sec= 15 min)


    def updateSensors(self): #Updates data from temp and particle sensor using threading, saves data every other time
        self.sht.update()
        self.pms.update()
	#Update  Sensors
        #self.saver.uploadData(self) #Save Data
        self.updateFanSensor()
        time.sleep(self.updateFrequency) #delay


    def displayOledTempInfo(self): #Displays temp and humid info on the OLED
        self.ssd.clear()   #clear
        self.ssd.displayText("Temperature & Humidity",0,0,)  #Header
        self.ssd.displayText(self.sht.getTempString(),0,16)   #display temp
        self.ssd.displayText(self.sht.getHumidString(),0,32) #display Humidity
        self.ssd.show()    #show page

    def displayOledParticleInfo(self): #Displays Air Quality Data on the OLED
        self.ssd.clear() #clear oled
        if self.pms.goodOrBad() ==True:
                self.ssd.displayText("Air Quality: Poor",0,0)
        else:
                self.ssd.displayText("Air Quality: Excellent",0,0)  #Header and state
        if self.useFan:
                self.ssd.displayText("Fan: On",0,16)
        else:
                self.ssd.displayText("Fan: OFf",0,16)

        self.ssd.displayText(("# Part. 2.5um: "+str(self.pms.pm2_5)),0,35) #Display Particle Quantities
        self.ssd.displayText(("# Part. 10um: "+str(self.pms.pm10)),0,51)


        #Display pms data
        self.ssd.show()

    def runOled(self):# Function called with threading that alternates between showing the temp and showing the Particle data on the oled every 5 sec.
        while(1):
            self.displayOledTempInfo()
            print("Temp info")
            time.sleep(5)
            self.displayOledParticleInfo()
            print("Particle info")
            time.sleep(5)

    def countdownOverrideTimer(self):
        if self.overrideLeft<=0: return

        if time.time() >= self.previousTime +1:#if one second has passed
            self.overrideTime-=1
            self.previousTime=time.time()

    def updateFanOverride(self):#Override the current fan settings for overrideAmount seconds.
        self.overrideLeft=self.overrideAmount
        self.useFan=not self.useFan
        self.fan.run(self.useFan)


    def updateFanSensor(self): #uses PMS sensor to turn fan on or off. does not run if override is on.
        if self.overrideLeft>0: return

        badAir=not  self.pms.goodOrBad()

        if badAir == True:
            self.useFan=True
        else:
            self.useFan=False

        self.fan.run(self.useFan)

   



manager=Manager()
threading.Thread(target=manager.updateSensors).start()
threading.Thread(target=manager.runOled).start()

while 1:
    manager.countdownOverrideTimer()
