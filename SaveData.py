import os
import json
import time

class saveData:
    def __init__(self, *args, **kwargs):
        self.times=[]  #list of times the data was taken
        self.temps=[]  #list of temp values
        self.humids=[] #list of humidity values

        self.filePath='ClimateData.json'  #the path of the save file

        self.readData()

    def save(self):#saves all temp data to file at path
        with open(self.filePath, 'w') as outfile:
           json.dumps(self.__dict__, outfile)
        
    def readData(self): #Reads all climate data from file at path
        if os.path.exists(self.filePath) == False:
               return
        with open(self.filePath,'r') as f:
            self = json.loads(f)

    def uploadData(self, Manager): #add current climate data to list and save
        self.times.append(time.ctime())
        self.temps.append(Manager.sht.temperature)
        self.humids.append(Manager.sht.humidity)

        self.save()


