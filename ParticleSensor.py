from pms7003 import Pms7003Sensor, PmsSensorException
import time
"""
if __name__ == '__main__':
while True:
        try:
            info=sensor.read()
            print(info)
            #"pm1_0cf1","pm2_5cf1""pm10cf1""pm1_0""pm2_5""pm10""n0_3""n0_5"n1_0"n2_5"n5_0""n10"
            print(info["pm1_0cf1"])
        except PmsSensorException:
            print('Connection problem')

    sensor.close()
"""

class particleSensor:
    def __init__(self, *args, **kwargs):
        self.sensor = Pms7003Sensor('/dev/serial0') #initialize sensor object

    def update(self):
        try:
            self.info=self.sensor.read() #update info
            #"pm1_0cf1","pm2_5cf1""pm10cf1""pm1_0""pm2_5""pm10""n0_3""n0_5"n1_0"n2_5"n5_0""n10"
            #print(info["pm1_0cf1"])



        except PmsSensorException:
            print('WARNING: PMS7003 Connection problem')

#EXAMPLE
sensor =particleSensor()
while 1:
    sensor.update()
    print(sensor.info)
    time.sleep(1)