# -*- coding: utf-8 -*-                                                                                                                               
# Google Spreadsheet
# ref
# https://qiita.com/connvoi_tyou/items/7cd7ffd5a98f61855f5c
# https://www.kumilog.net/entry/2018/03/22/090000#%E3%82%B9%E3%83%97%E3%83%AC%E3%83%83%E3%83%89%E3%82%B7%E3%83%BC%E3%83%88%E3%81%AB%E3%83%87%E3%83%BC%E3%82%BF%E3%82%92%E6%9B%B8%E3%81%8D%E8%BE%BC%E3%82%80
# pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib
from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

# refarence
# https://qiita.com/Taroi_Japanista/items/ac51ca2f636f422cced6
import os
import datetime

import google_spreadsheet_writer
import line_notify
#import disp_oled
import bme280

def main():
    now = datetime.datetime.now() # 現在の日時を取得
    # --- BME280
    temperature, pressure, humidity = bme280.readData()

    max_range_temperature = 28.0
    min_range_temperature = 20.0

    max_range_humidity = 70.0
    min_range_humidity = 40.0

    writeCsv( now, humidity, temperature, max_range_temperature, min_range_temperature, max_range_humidity, min_range_humidity, pressure)

    google_spreadsheet_writer.write( now, humidity, temperature, max_range_temperature, min_range_temperature, max_range_humidity, min_range_humidity, pressure)

    line_notify.notify( now, humidity, temperature, max_range_temperature, min_range_temperature, max_range_humidity, min_range_humidity, pressure)

#   disp_oled.disp( now, temperature)

def writeCsv( now, humidity, temperature, max_range_temperature, min_range_temperature, max_range_humidity, min_range_humidity, pressure):
    file = open('sensor_log.csv', 'a+')  #書き込みモードでオープン  
    file.write('{0:%Y/%m/%d %H:%M:%S}, {1:3f}, {2:3f}, {3:3f}, {4:3f}, {5:3f}, {6:3f}, {7:3f}\n'.format(now, humidity, temperature, max_range_temperature, min_range_temperature, max_range_humidity, min_range_humidity, pressure))

if __name__ == '__main__':
    main()
# [END]
