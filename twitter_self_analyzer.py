# twitter self analyzer
import requests
import configparser
import google_spreadsheet_writer

def get_config():
    # https://tabeta-log.blogspot.com/2021/07/pythonconfigparser.html
    config = configparser.ConfigParser(interpolation=None)
    config.read('secrets.ini')

    id = config.get('twitter', 'id')
    api_key = config.get('twitter', 'api_key')
    api_secret = config.get('twitter', 'api_key')
    access_token = config.get('twitter', 'api_key_secret')
    bearer_token = config.get('twitter', 'bearer_token')

    return id, api_key, api_secret, access_token, bearer_token 


def count_followers():
    followers_count = 0
    while True:
        id, api_key, api_secret, access_token, bearer_token = get_config()
        url = 'https://api.twitter.com/2/users/' + id + '/followers'
        payload = {'max_results': '1000'}  # max 1000
        headers = {'Authorization': 'Bearer ' + bearer_token}
        res = requests.get(url, params=payload, headers=headers)
        json_res = res.json()

        followers_count += json_res['meta']['result_count']

        if ('next_token' in json_res['meta']):
            payload['pagination_token'] = json_res['meta']['next_token']
        else:
            break

    return followers_count 


def count_following():
    following_count = 0
    while True:
        id, api_key, api_secret, access_token, bearer_token = get_config()
        url = 'https://api.twitter.com/2/users/' + id + '/following'
        payload = {'max_results': '1000'}  # max 1000
        headers = {'Authorization': 'Bearer ' + bearer_token}
        res = requests.get(url, params=payload, headers=headers)
        json_res = res.json()

        following_count += json_res['meta']['result_count']

        if ('next_token' in json_res['meta']):
            payload['pagination_token'] = json_res['meta']['next_token']
        else:
            break

    return following_count 


def write_google_spreadsheet():
    follower_count = count_followers()
    following_count = count_following()
    google_spreadsheet_writer.write_for_twitter(follower_count, following_count)


if __name__ == '__main__':
    #print(count_followers())
    #print(count_following())
    write_google_spreadsheet()
# [END]

