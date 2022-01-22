import requests
import configparser
import sensor_class


def getAccessToken(section):

    config = configparser.ConfigParser()
    config.read('secrets.ini')

    access_token = config.get(section, 'access_token')
    return access_token


def checkLineNotify(s : sensor_class.Sensor):
    message = 'good condition!'
    is_line_notify = True

    if s.min_range_temperature > s.temperature:
        message = 'TOO COOL!! \n[{0} c] [{1} %] [{2} hPa] [{3} ppm]'.format('{:.1f}'.format(
            s.temperature), '{:.1f}'.format(s.humidity), '{:.1f}'.format(s.pressure), '{:.1f}'.format(s.co2))
    elif s.temperature > s.max_range_temperature:
        message = 'TOO HOT!! \n[{0} c] [{1} %] [{2} hPa] [{3} ppm]'.format('{:.1f}'.format(
            s.temperature), '{:.1f}'.format(s.humidity), '{:.1f}'.format(s.pressure), '{:.1f}'.format(s.co2))
    else:
        message = "GOOD CONDITION! \n[{0} c] [{1} %] [{2} hPa]".format('{:.1f}'.format(
            s.temperature), '{:.1f}'.format(s.humidity), '{:.1f}'.format(s.pressure))
        is_line_notify = False

    return is_line_notify, message


def notify(s : sensor_class.Sensor):
    url = "https://notify-api.line.me/api/notify"
    headers = {'Authorization': 'Bearer ' + getAccessToken('line')}

    judge, message = checkLineNotify(s)

    if judge:
        payload = {'message': message}
        r = requests.post(url, headers=headers, params=payload,)


def notify_for_co2(s : sensor_class.Sensor):
    message = None

    if s.co2 > s.max_range_co2:
        message = 'Please ventulate !! \n[CO2: {0} ppm (> {1} ppm)]'.format(s.co2, s.max_range_co2)
    else:
        return

    url = "https://notify-api.line.me/api/notify"
    headers = {'Authorization': 'Bearer ' + getAccessToken('co2')}

    payload = {'message': message}
    r = requests.post(url, headers=headers, params=payload,)

