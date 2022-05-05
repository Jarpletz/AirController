# SPDX-FileCopyrightText: Copyright (c) 2020 Bryan Siepert for Adafruit Industries
#
# SPDX-License-Identifier: MIT
import time
import board
import adafruit_shtc3


class tempSensor:
    def __init__(self, *args, **kwargs):
        i2c = board.I2C()  # uses board.SCL and board.SDA
        self.sht = adafruit_shtc3.SHTC3(i2c)

    def update(self):#update the temp data
        self.temperature, self.humidity = sht.measurements
        self.temperature=(self.temperature*1.8)+32 #CONVERTS TEMP TO F

    def getTempString(self):#Returns the temp. (in F) as string with formatting text
        tempStr=("Temperature: %0.1f F" % self.temperature)
        return tempStr

    def getHumidString(self):#Returns the humidity as string with formatting text
        humidStr=("Humidity: %0.1f %%" % self.humidity)
        return humidStr

#EXAMPLE:
sensor=tempSensor()
while 1:
    sensor.update() #update Data
    print(sensor.getTempString()) #print Temp with formatting
    print(sensor.getHumidString()) #print Humidity with formatting
    print(" ")
    time.sleep(1) 






