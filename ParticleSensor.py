from pms7003 import Pms7003Sensor, PmsSensorException
#import time

class particleSensor:
    def __init__(self, *args, **kwargs):
        self.sensor = Pms7003Sensor('/dev/serial0') #initialize sensor object
        self.pm2_5=0
        self.pm10=0

    def update(self):
        try:
            self.info=self.sensor.read() #update info
            #"pm1_0cf1","pm2_5cf1""pm10cf1""pm1_0""pm2_5""pm10""n0_3""n0_5"n1_0"n2_5"n5_0""n10"
            #print(info["pm1_0cf1"])

            self.pm2_5=self.info["pm2_5"] 
            self.pm10=self.info["pm10"]

        except PmsSensorException: print('WARNING: PMS7003 Connection problem')

    def goodOrBad(self):
        if self.pm2_5<14 and self.pm2_5>4:
            stateOfAir2_5 = True
        else:
            stateOfAir2_5 = False
        if self.pm10 <= 50:
            stateOfAir10 = True
        else:
            stateOfAir10 = False
        print (stateOfAir10)
        print (StateOfAir2_5)
object= particleSensor()
object.update(object)
object.goodOrBad(object)
#EXAMPLE sensor =particleSensor() while#    sensor.update()
#    print(sensor.info)
#    time.sleep(1)
