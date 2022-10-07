import tweepy
import configparser
import time
import random
from pprint import pprint

# https://di-acc2.com/system/rpa/9690/
def get_config():
    # https://tabeta-log.blogspot.com/2021/07/pythonconfigparser.html
    config = configparser.ConfigParser(interpolation=None)
    config.read('secrets.ini')

    id = config.get('twitter', 'id')
    api_key = config.get('twitter', 'api_key')
    api_secret = config.get('twitter', 'api_key_secret')
    access_token = config.get('twitter', 'access_token')
    access_token_secret = config.get('twitter', 'access_token_secret')
    bearer_token = config.get('twitter', 'bearer_token')

    return id, api_key, api_secret, access_token, access_token_secret, bearer_token


# クライアント関数を作成
def ClientInfo():
    id, api_key, api_secret, access_token, access_token_secret, bearer_token = get_config()
    client = tweepy.Client(bearer_token    = bearer_token,
                           consumer_key    = api_key,
                           consumer_secret = api_secret,
                           access_token    = access_token,
                           access_token_secret = access_token_secret,
                          )
    
    return client

# ★必要情報入力
search    = "#プログラミング初心者"  # 検索対象
tweet_max = 10          # 取得したいツイート数(10〜100で設定可能)

# 関数
def GetRandomSearchWord():
    words = [
        "#プログラミング初心者",
        "#駆け出しエンジニアと繋がりたい",
        "#プログラミング初心者と繋がりたい",
        "#エンジニアと繋がりたい",
        "#プログラミング独学"]
    return words[random.randint(0,len(words))]

def SearchTweets(search,tweet_max):    
    # 直近のツイート取得
    tweets = ClientInfo().search_recent_tweets(query = GetRandomSearchWord(), max_results = tweet_max)

    # 取得したデータ加工
    results     = []
    tweets_data = tweets.data

    # tweet検索結果取得
    if tweets_data != None:
        for tweet in tweets_data:
            obj = {}
            obj["tweet_id"] = tweet.id      # Tweet_ID
            obj["text"] = tweet.text  # Tweet Content
            results.append(obj)
    else:
        results.append('')
        
    # 結果出力
    return results


# 関数情報
def LikeTweet(tweet_id):
    favo = ClientInfo().like(tweet_id)
    return favo

results = SearchTweets(search,tweet_max)
# 関数実行・出力
# pprint(results)

# いいね
for result in results:
    # ランダム秒待つ(10～30秒の間で待機する)
    time.sleep(random.randint(10,30))
    pprint(LikeTweet(result["tweet_id"]))
random.randint(10,30)
