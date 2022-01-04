import requests
import configparser


def getAccessToken(key):

    config = configparser.ConfigParser()
    config.read('secrets.ini')

    access_token = config.get(key, 'access_token')
    return access_token


def checkLineNotify(now, humidity, temperature, max_range_temperature, min_range_temperature, max_range_humidity, min_range_humidity, pressure, co2):

    message = 'good condition!'
    is_line_notify = True

    if min_range_temperature > temperature:
        message = 'TOO COOL!! \n[{0} c] [{1} %] [{2} hPa] [{3} ppm]'.format('{:.1f}'.format(
            temperature), '{:.1f}'.format(humidity), '{:.1f}'.format(pressure), '{:.1f}'.format(co2))
    elif temperature > max_range_temperature:
        message = 'TOO HOT!! \n[{0} c] [{1} %] [{2} hPa] [{3} ppm]'.format('{:.1f}'.format(
            temperature), '{:.1f}'.format(humidity), '{:.1f}'.format(pressure), '{:.1f}'.format(co2))
    else:
        message = "GOOD CONDITION! \n[{0} c] [{1} %] [{2} hPa]".format('{:.1f}'.format(
            temperature), '{:.1f}'.format(humidity), '{:.1f}'.format(pressure))
        is_line_notify = False

    return is_line_notify, message


def notify(now, humidity, temperature, max_range_temperature, min_range_temperature, max_range_humidity, min_range_humidity, pressure, co2):

    url = "https://notify-api.line.me/api/notify"
    headers = {'Authorization': 'Bearer ' + getAccessToken('line')}

    judge, message = checkLineNotify(now, humidity, temperature, max_range_temperature,
                                     min_range_temperature, max_range_humidity, min_range_humidity, pressure, co2)

    if judge:
        payload = {'message': message}
        r = requests.post(url, headers=headers, params=payload,)


def notify_for_co2(now, co2):
    message = None
    max_limit = 1000

    if co2 > max_limit:
        message = 'Please ventulate !! \n[CO2: {0} ppm (> {1} ppm)]'.format(co2, max_limit)
    else:
        return

    url = "https://notify-api.line.me/api/notify"
    headers = {'Authorization': 'Bearer ' + getAccessToken('co2')}

    payload = {'message': message}
    r = requests.post(url, headers=headers, params=payload,)

