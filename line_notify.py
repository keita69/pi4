import requests
import configparser
 

def checkLineNotify( now, humidity, temperature, max_range_temperature, min_range_temperature, max_range_humidity, min_range_humidity):

    message = 'good condition!'
    is_line_notify = True

    if min_range_temperature <= temperature <= max_range_temperature :
        message = "GOOD CONDITION! \n[{0} c] [{1} %]".format('{:.1f}'.format(temperature), '{:.1f}'.format(humidity))
        is_line_notify = False

    if min_range_temperature > temperature :
        message = 'TOO COOL!! \n[{0} c] [{1} %]'.format('{:.1f}'.format(temperature), '{:.1f}'.format(humidity))
    elif temperature > max_range_temperature :
        message = 'TOO HOT!! \n[{0} c] [{1} %]'.format('{:.1f}'.format(temperature), '{:.1f}'.format(humidity))

    path_w = 'line_notify_write_last_time.txt'

    lastTime = ''
    with open(path_w) as f:
        lastTime = f.read()

    
    #TODO if 15分以内であれば通知しない

    #is_line_notify = True
    print('{0} [{1} c] [{2} %]'.format(now, '{:.1f}'.format(temperature), humidity))
    print('{0} [{1} c] [{2} %] [{3}]'.format(now, temperature, humidity, is_line_notify))

    if is_line_notify :
        nowstr = now.strftime('%Y-%m-%d %H:%M:%S')
        with open(path_w, mode='w') as f:
            f.write(nowstr)

    return is_line_notify, message



def notify( now, humidity, temperature, max_range_temperature, min_range_temperature, max_range_humidity, min_range_humidity):
    config = configparser.ConfigParser()
    config.read('secrets.ini')
     
    access_token = config.get('line', 'access_token') 
    
    url = "https://notify-api.line.me/api/notify"
    headers = {'Authorization': 'Bearer ' + access_token}

    judge, message =  checkLineNotify( now, humidity, temperature, max_range_temperature, min_range_temperature, max_range_humidity, min_range_humidity)

    print('{0} [{1} c] [{2} %] [{3}]'.format(now, temperature, humidity, judge))

    if judge :
        payload = {'message': message}
        r = requests.post(url, headers=headers, params=payload,)

