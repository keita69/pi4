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
# import disp_oled
import bme280
import mh_z19b
import sensor_class

def main():

    now = datetime.datetime.now()  # 現在の日時を取得
    # --- BME280
    temperature, pressure, humidity = bme280.readData()
    co2 = mh_z19b.getCo2()
    #co2 = 0

    sensor = sensor_class.Sensor(now, humidity, temperature, pressure, co2)
    sensor.dump()

    writeCsv(sensor)
    line_notify.notify(sensor)
    line_notify.notify_for_co2(sensor)
    # TODO : if error , notify by line message.
    google_spreadsheet_writer.write(sensor)

#   disp_oled.disp( now, temperature)


def writeCsv(s:sensor_class.Sensor):
    file = open('sensor_log.csv', 'a+')  # 書き込みモードでオープン
    file.write('{0:%Y/%m/%d %H:%M:%S}, {1:3f}, {2:3f}, {3:3f}, {4:3f}, {5:3f}, {6:3f}, {7:3f}, {8:3f}\n'.format(s.now, s.humidity,
               s.temperature, s.max_range_temperature, s.min_range_temperature, s.max_range_humidity, s.min_range_humidity, s.pressure, s.co2))


if __name__ == '__main__':
    main()
# [END]
