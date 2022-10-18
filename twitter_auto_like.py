import tweepy
import configparser
import time
import re
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
tweet_max = 15          # 取得したいツイート数(10〜100で設定可能)

#-------------------------------------------------------------------------------- 
# 関数
#-------------------------------------------------------------------------------- 

# 検索キーワードをランダム抽出
def GetRandomSearchWord():
    words = [
        "#プログラミング初心者",
        "#駆け出しエンジニアと繋がりたい",
        "#プログラミング初心者と繋がりたい",
        "#エンジニアと繋がりたい",
        "#プログラミング独学"]
    return words[random.randint(0,len(words))-1]

# 対象外キーワード正規表現取得
def GetIgnoreWordRe():
    iw = "面接|イベント|おは戦|未経験|合格|会|催|公式|稼|アカデミ|スクール|school|塾|相互|無料|突破|Qiitaの良記事|リプ|DM|転職"
    return iw

# ツイートidからユーザ情報を取得
def GetTweet(tweet_id):
    # メソッド実行
    GetTwt = ClientInfo().get_tweet(id=int(tweet_id), expansions=["author_id"], user_fields=["username"])

    # 結果加工
    twt_result = {}
    twt_result["tweet_id"] = tweet_id
    twt_result["user_id"]  = GetTwt.includes["users"][0].id
    twt_result["username"] = GetTwt.includes["users"][0].username
    twt_result["text"]     = GetTwt.data
    twt_result["url"]      = "https://twitter.com/" + GetTwt.includes["users"][0].username + "/status/" + str(tweet_id)


    # 結果出力
    return twt_result


# ツイート検索
def SearchTweets(tweet_max):    
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

# いいね
def LikeTweet(tweet_id):
    favo = ClientInfo().like(tweet_id)
    return favo



#-------------------------------------------------------------------------------- 
# Main
#-------------------------------------------------------------------------------- 
userList = []

# 検索
results = SearchTweets(tweet_max)

# いいね
for result in results:
    # ランダム秒待つ(10～30秒の間で待機する)
    time.sleep(random.randint(10,30))

    tweet_id = result["tweet_id"]
    tweet_text = result["text"]

    user_id = GetTweet(tweet_id)["user_id"]

    if len(re.findall(GetIgnoreWordRe(), tweet_text)) > 0:
        #print("--[ IGNORE ]-----------")
        #print(user_id)
        #print(tweet_text)
        continue

    if not (user_id in userList):
        userList.append(user_id)
        print("--[ LIKE ]-----------")
        print(user_id)
        print(tweet_text)
        pprint(LikeTweet(tweet_id))
