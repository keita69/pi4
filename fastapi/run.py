from fastapi import FastAPI, Request, BackgroundTasks
import configparser
from fastapi import FastAPI, Request
from linebot import WebhookParser
from linebot.models import TextMessage
from aiolinebot import AioLineBotApi


def get_config():
    # https://tabeta-log.blogspot.com/2021/07/pythonconfigparser.html
    config = configparser.ConfigParser(interpolation=None)
    config.read('secrets.ini')

    channel_access_token = config.get('line', 'channel_access_token')
    chanel_secret = config.get('line', 'channel_secret')

    return channel_access_token, chanel_secret


# イベント処理（新規追加）
async def handle_events(events):
    for ev in events:
        try:
            await line_api.reply_message_async(
                ev.reply_token,
                TextMessage(text=f"You said: {ev.message.text}"))
        except Exception:
            # エラーログ書いたりする
            pass


# APIクライアントとパーサーをインスタンス化
cat, cs = get_config()
line_api = AioLineBotApi(channel_access_token=cat)
parser = WebhookParser(channel_secret=cs)

# FastAPIの起動
app = FastAPI()

@app.post("/messaging_api/handle_request")
async def handle_request(request: Request, background_tasks: BackgroundTasks): 
    # リクエストをパースしてイベントを取得（署名の検証あり）
    events = parser.parse(
        (await request.body()).decode("utf-8"),
        request.headers.get("X-Line-Signature", ""))

    # 各イベントを処理
    for ev in events:
        await line_api.reply_message_async(
            ev.reply_token,
            TextMessage(text=f"You said: {ev.message.text}"))

    # イベント処理をバックグラウンドタスクに渡す
    background_tasks.add_task(handle_events, events=events)

    # LINEサーバへHTTP応答を返す
    return "ok"


# ref
# https://qiita.com/uezo/items/7fa15f3d77b140190981
# https://qiita.com/sunaga70/items/6821772a9bcbdbbc2c03

