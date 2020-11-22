# -*- coding: utf-8 -*-                                                                                                                               

import os
import Adafruit_DHT
import datetime

now = datetime.datetime.now() # 現在の日時を取得                                                                                                      

sensor = Adafruit_DHT.DHT22
pin = 4

humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

max_range_temperature = 28.0
min_range_temperature = 20.0

max_range_humidity = 70.0
min_range_humidity = 40.0

file = open('sensor_log.csv', 'a+')  #書き込みモードでオープン                                                                           
file.write('{0:%Y/%m/%d %H:%M:%S}, {1:3f}, {2:3f}, {3:3f}, {4:3f}, {5:3f}, {6:3f}\n'.format(now, humidity, temperature, max_range_temperature, min_range_temperature, max_range_humidity, min_range_humidity))

