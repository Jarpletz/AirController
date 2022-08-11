import os
import json
from collections import namedtuple
from json import JSONEncoder
import time

class saveData:
    def __init__(self, *args, **kwargs):
        self.times=[]  #list of times the data was taken
        self.temps=[]  #list of temp values
        self.humids=[] #list of humidity values

        self.filePath='ClimateData.json'  #the path of the save file

        self.readData()

    def save(self):#saves all temp data to file at path
        jsonStr=json.dumps(self.__dict__)
        f=open(self.filePath,"w")
        f.write(jsonStr)
        f.close()
        print("Saving Data")
	
    def customDecoder(dataDict):
        return namedtuple('X',dataDict.keys())(*dataDict.values())

    def readData(self): #Reads all climate data from file at path
        if os.path.exists(self.filePath) == False:
               return
        with open(self.filePath,'r') as f:
            self = json.loads(str(f),object_hook=self.customDecoder)
            
    def uploadData(self, Manager): #add current climate data to list and save
        self.times.append(time.ctime())
        self.temps.append(Manager.sht.temperature)
        self.humids.append(Manager.sht.humidity)

        self.save()



