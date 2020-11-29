import requests
import configparser
 

def notify( now, humidity, temperature, max_range_temperature, min_range_temperature, max_range_humidity, min_range_humidity):
    config = configparser.ConfigParser()
    config.read('secrets.ini')
     
    access_token = config.get('line', 'access_token') 
    
    url = "https://notify-api.line.me/api/notify"
    headers = {'Authorization': 'Bearer ' + access_token}

    is_line_noify, message =  checkLineNotify( now, humidity, temperature, max_range_temperature, min_range_temperature, max_range_humidity, min_range_humidity)

    if is_line_notify :
        payload = {'message': message}
        r = requests.post(url, headers=headers, params=payload,)





def checkLineNotify( now, humidity, temperature, max_range_temperature, min_range_temperature, max_range_humidity, min_range_humidity):

    message = 'good condition!'
    is_line_notyfy = True

    if min_range_temperature <= temperature <= max_range_temperature :
        message = "GOOD CONDITION!"
        is_line_notify = False

    if min_range_temperature > temperature :
        message = 'TOO COOL!! [ {0} c] [{1} %]'.format(temperature, humidity)
    elif temperature > max_range_temperature :
        message = 'TOO HOT!! [ {0} c][ {1} %]'.format(temperature, humidity)

    path_w = 'line_notify_write_last_time.txt'

    lastTime = ''
    with open(path_w) as f:
        lastTime = f.read()

    
    #TODO if 15分以内であれば通知しない




    if is_line_notify :
        nowstr = now.strftime('%Y-%m-%d %H:%M:%S')
        with open(path_w, mode='w') as f:
            f.write(nowstr)

    return is_line_notify, message
