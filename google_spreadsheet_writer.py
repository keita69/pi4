# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# [START sheets_quickstart]
from __future__ import print_function
import pickle
import os.path
import sensor_class
import datetime
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

# The ID and range of a sample spreadsheet.
# SPREADSHEET_ID = '1fd3vQUKMGdUDyzuTNviPYf6x8GvGA77V6eaJ-jE0oAo'
spreadsheetId = '1Ji2PrvuhPHWHu0K-fGaxgCvqSV8vd2AkqJDYCPcrjkA'
# RANGE_NAME = 'A1:C1'
# ValueInputOption = 'USER_ENTERED'


def isOver1440Rows():
    range_ = "'温度と湿度'!A1441:A1441"
    request = getService().spreadsheets().values().get(
        spreadsheetId=spreadsheetId, range=range_)
    response = request.execute()
    if 'values' in response:
        # not value of A1441:A1441
        # print("isOver1440 is True")
        # print(response)
        return True
    else:
        # print("isOver1440 is False")
        # print(response)
        return False


def deleteFirstAndSecondRows():
    # https://developers.google.com/sheets/api/samples/rowcolumn
    # print("deleteFirstAndSecondRows start ")

    # XXXXXXXXXX
    sheetName = '温度と湿度'
    rangeName = 'A:H'
    ValueInputOption = 'USER_ENTERED'
    body = {
        "requests": [
            {
                "deleteDimension": {
                    "range": {
                        "sheetId": 0,  # gid of google spreadsheet url
                        "dimension": "ROWS",
                        "startIndex": 1,
                        "endIndex": 3
                    }
                }
            },
        ],
    }
    response = getService().spreadsheets().batchUpdate(
        spreadsheetId=spreadsheetId, body=body).execute()


def getService():
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
    return service


def write(s:sensor_class.Sensor):

    if isOver1440Rows():
        deleteFirstAndSecondRows()

    nowstr = s.now.strftime('%Y-%m-%d %H:%M:%S')

    # XXXXXXXXXX
    sheetName = '温度と湿度'
    rangeName = 'A:I'
    ValueInputOption = 'USER_ENTERED'
    body = {
        'values': [[nowstr, s.humidity, s.temperature, s.max_range_temperature, s.min_range_temperature, s.max_range_humidity, s.min_range_humidity, s.pressure, s.co2, s.max_range_co2]],
    }
    result = getService().spreadsheets().values().append(
        spreadsheetId=spreadsheetId, range=sheetName + "!" + rangeName,
        valueInputOption=ValueInputOption, body=body).execute()

#    # Call the Sheets API
#    sheet = service.spreadsheets()
#    result = sheet.values().get(spreadsheetId=SPREADSHEET_ID,
#                                range=RANGE_NAME).execute()
#    values = result.get('values', [])
#
#    if not values:
#        print('No data found.')
#    else:
#        print('Name, Major:')
#        for row in values:
#            # Print columns A and E, which correspond to indices 0 and 4.
#            print('%s, %s' % (row[0], row[4]))



def write_for_twitter(follower_count, following_count):

    today = datetime.date.today()
    yyyymmdd = today.strftime('%Y%m%d')

    sheetName = 'twitter分析'
    rangeName = 'A:C'
    ValueInputOption = 'USER_ENTERED'
    body = {
        'values': [[yyyymmdd, follower_count, following_count]],
    }
    result = getService().spreadsheets().values().append(
        spreadsheetId=spreadsheetId, range=sheetName + "!" + rangeName,
        valueInputOption=ValueInputOption, body=body).execute()


# if __name__ == '__main__':
    # deleteFirstAndSecondRows()
    # isOver1440Rows()

# [END sheets_quickstart]
