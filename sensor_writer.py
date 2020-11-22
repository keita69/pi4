# -*- coding: utf-8 -*-                                                                                                                               
# refarence
# https://qiita.com/Taroi_Japanista/items/ac51ca2f636f422cced6
import os
import Adafruit_DHT
import datetime

# Google Spreadsheet
# ref
# https://qiita.com/connvoi_tyou/items/7cd7ffd5a98f61855f5c
# pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib
from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

def main():
    now = datetime.datetime.now() # 現在の日時を取得
    humidity, temperature = getHumidiyTEmperatureFromDHT22()

    max_range_temperature = 28.0
    min_range_temperature = 20.0

    max_range_humidity = 70.0
    min_range_humidity = 40.0

    writeCsv( now, humidity, temperature, max_range_temperature, min_range_temperature, max_range_humidity, min_range_humidity)
    
    writeGoogleSpreadSheet( now, humidity, temperature, max_range_temperature, min_range_temperature, max_range_humidity, min_range_humidity)

def getHumidiyTEmperatureFromDHT22():
    sensor = Adafruit_DHT.DHT22
    pin = 4
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
    return(humidity, temperature)


def writeCsv( now, humidity, temperature, max_range_temperature, min_range_temperature, max_range_humidity, min_range_humidity):
    file = open('sensor_log.csv', 'a+')  #書き込みモードでオープン  
    file.write('{0:%Y/%m/%d %H:%M:%S}, {1:3f}, {2:3f}, {3:3f}, {4:3f}, {5:3f}, {6:3f}\n'.format(now, humidity, temperature, max_range_temperature, min_range_temperature, max_range_humidity, min_range_humidity))

def writeGoogleSpreadSheet( now, humidity, temperature, max_range_temperature, min_range_temperature, max_range_humidity, min_range_humidity):
    print("TODO:WIRTE GOOGOLE SPREADSHEET")

    # If modifying these scopes, delete the file token.pickle.
    SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

    # The ID and range of a sample spreadsheet.
    SPREADSHEET_ID = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
     
    """Shows basic usage of the Sheets API.
    Prints values from a sample spreadsheet.
    """
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

        service = build('sheets', 'v4', credentials=creds)

        # XXXXXXXXXX
        sheetName = '温度と湿度'
        rangeName = 'A:G'
        ValueInputOption = 'USER_ENTERED'
        body = {
            'values': [[now, humidity, temperature, max_range_temperature, min_range_temperature, max_range_humidity, min_range_humidity]],
        }
        result = service.spreadsheets().values().append(
            spreadsheetId=SPREADSHEET_ID, range=sheetName + "!" + rangeName,
            valueInputOption=ValueInputOption, body=body).execute()
        # TODO add judge result

if __name__ == '__main__':
    main()
# [END]
