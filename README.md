# pi4
## Q1
```
root@pi4:/home/pi/git/pi4# bash start_sensor.sh
Traceback (most recent call last):
  File "/home/pi/git/pi4/sensor_writer.py", line 10, in <module>
    from googleapiclient.discovery import build
ModuleNotFoundError: No module named 'googleapiclient'
^C

```
## A1
```
sudo pip install --upgrade google-api-python-client

```

## Q2
```
pi@pi4:~/git/pi4 $ sudo bash start_sensor.sh &
[2] 8630
pi@pi4:~/git/pi4 $ Traceback (most recent call last):
  File "/home/pi/git/pi4/sensor_writer.py", line 11, in <module>
    from google_auth_oauthlib.flow import InstalledAppFlow
ModuleNotFoundError: No module named 'google_auth_oauthlib'
```
## A2
```
sudo pip install --upgrade google-auth-oauthlib
```
## Q3
```
pi@pi4:~/git/pi4 $ sudo bash start_sensor.sh
Traceback (most recent call last):
  File "/home/pi/git/pi4/sensor_writer.py", line 22, in <module>
    import bme280
  File "/home/pi/git/pi4/bme280.py", line 9, in <module>
    bus = smbus.SMBus(bus_number)
FileNotFoundError: [Errno 2] No such file or directory
^C
```
## A3
- bme280 設定
https://dev.classmethod.jp/articles/raspberrypi-and-bme280/#toc-9

## Q4
```

pi@pi4:~/git/pi4 $ sudo bash start_sensor.sh
Imotatemp : 12.91  ℃‘
pressure : 1021.64 hPa
hum :  42.42 ％
Traceback (most recent call last):
  File "/home/pi/git/pi4/sensor_writer.py", line 48, in <module>
    main()
  File "/home/pi/git/pi4/sensor_writer.py", line 37, in main
    google_spreadsheet_writer.write( now, humidity, temperature, max_range_temperature, min_range_temperature, max_range_humidity, min_range_humidity, pressure)
  File "/home/pi/git/pi4/google_spreadsheet_writer.py", line 100, in write
    if isOver1440Rows() :
  File "/home/pi/git/pi4/google_spreadsheet_writer.py", line 35, in isOver1440Rows
    request = getService().spreadsheets().values().get(spreadsheetId=spreadsheetId, range=range_)
  File "/home/pi/git/pi4/google_spreadsheet_writer.py", line 87, in getService
    flow = InstalledAppFlow.from_client_secrets_file(
  File "/usr/local/lib/python3.9/dist-packages/google_auth_oauthlib/flow.py", line 201, in from_client_secrets_file
    with open(client_secrets_file, "r") as json_file:
FileNotFoundError: [Errno 2] No such file or directory: 'credentials.json'
```
## A4
pcに保存してるcredentials.json をサーバにupload

## Q5
```
Please visit this URL to authorize this application: https://accounts.google.com/o/oauth2/auth?response_type=code&client_id=191255197849-3jeej2ctc0chketvep2csjstdq59dvbb.apps.googleusercontent.com&redirect_uri=http%3A%2F%2Flocalhost%3A57669%2F&scope=https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fspreadsheets&state=LykYgGvClC0GBxeLgBh230lzqreuac&access_type=offline
```

## A5
rasberry pi のブラウザでリンクを踏み、画面に従い認証行う。

## Q6
```
pi@pi4:~/git/pi4 $ sudo bash start_sensor.sh
temp : 13.05  ℃‘
pressure : 1021.75 hPa
hum :  42.22 ％
isOver1440 is False
{'range': "'温度と湿度'!A1441", 'majorDimension': 'ROWS'}
Traceback (most recent call last):
  File "/home/pi/git/pi4/sensor_writer.py", line 48, in <module>
    main()
  File "/home/pi/git/pi4/sensor_writer.py", line 39, in main
    line_notify.notify( now, humidity, temperature, max_range_temperature, min_range_temperature, max_range_humidity, min_range_humidity, pressure)
  File "/home/pi/git/pi4/line_notify.py", line 44, in notify
    access_token = config.get('line', 'access_token')
  File "/usr/lib/python3.9/configparser.py", line 781, in get
    d = self._unify_values(section, vars)
  File "/usr/lib/python3.9/configparser.py", line 1149, in _unify_values
    raise NoSectionError(section) from None
configparser.NoSectionError: No section: 'line'


```

## A6
pcに保存してるsecrets.ini をサーバにupload

## Q7
```

pi@pi4:~/git/pi4 $ sudo bash start_sensor.sh
temp : 13.14  ℃‘
pressure : 1022.00 hPa
hum :  42.28 ％
isOver1440 is True
{'range': "'温度と湿度'!A1441", 'majorDimension': 'ROWS', 'values': [['01/01 17:39']]}
deleteFirstAndSecondRows start
Traceback (most recent call last):
  File "/home/pi/git/pi4/sensor_writer.py", line 48, in <module>
    main()
  File "/home/pi/git/pi4/sensor_writer.py", line 39, in main
    line_notify.notify( now, humidity, temperature, max_range_temperature, min_range_temperature, max_range_humidity, min_range_humidity, pressure)
  File "/home/pi/git/pi4/line_notify.py", line 49, in notify
    judge, message =  checkLineNotify( now, humidity, temperature, max_range_temperature, min_range_temperature, max_range_humidity, min_range_humidity, pressure)
  File "/home/pi/git/pi4/line_notify.py", line 22, in checkLineNotify
    with open(path_w) as f:
FileNotFoundError: [Errno 2] No such file or directory: 'line_notify_write_last_time.txt'
```

## A7
```
touch line_notify_write_last_time.txt
```

# oled ディスプレイ 温度表示 
https://101010.fun/iot/raspi-oled.html
https://jimaru.blog/electronic-work/pip3-install-rpi-gpio/

```
sudo apt-get update
sudo apt-get install i2c-tools
sudo pip3 install adafruit-circuitpython-ssd1306
sudo pip3 install rpi.gpio
sudo apt install python3-pip
sudo apt install python3-rpi.gpio
sudo pip3 install adafruit-circuitpython-ssd1306
sudo pip3 install adafruit-blinka
sudo pip3 install pillow
sudo apt-get update
sudo apt-get install libopenjp2-7
sudo apt install libtiff5
sudo apt-get install fonts-noto-cjkroot@pi4:/home/pi/git/pi4# bash start_sensor.sh
ls /usr/share/fonts/opentype/noto/
```

# MH-Z19B CO2濃度定
https://dev.classmethod.jp/articles/raspberry-pi-4-b-mh-z19b-co2/

# Python Lint  
https://qiita.com/genbu-jp/items/723b619013dc86008acc
https://qiita.com/psychoroid/items/2c2acc06c900d2c0c8cb

# 電子工作初心者がRaspberry Pi Zeroに温湿度気圧センサBME280を接続してみた
https://dev.classmethod.jp/articles/raspberrypi-and-bme280/

# credentials.json 作成
https://console.cloud.google.com/apis/credentials?project=humsensor-1606088383596
