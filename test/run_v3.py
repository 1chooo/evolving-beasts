# -*- coding: utf-8 -*-
'''
Create Date: 2023/07/09
Author: @1chooo(Hugo ChunHo Lin)
Version: v0.0.1
'''

import os
import json
from Monster import Utils
from Monster import Drama
from datetime import datetime
from flask import Flask, request, abort
from linebot.v3 import WebhookHandler
from linebot.v3.messaging import Configuration
from linebot.v3.messaging import ApiClient
from linebot.v3.messaging import MessagingApi
from linebot.v3.messaging import ReplyMessageRequest
from linebot.v3.messaging import TextMessage
from linebot.v3.messaging import MessagingApiBlob
from linebot.v3.messaging import MessagingApiBlob
from linebot.v3.webhooks import MessageEvent
from linebot.v3.webhooks import TextMessageContent
from linebot.v3.exceptions import InvalidSignatureError

app = Flask(__name__)

config_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '.', 'config')
config_path = os.path.join(config_dir, 'linebot.conf')
line_bot_config = json.load(open(config_path, 'r', encoding='utf8'))

configuration = Configuration(access_token=line_bot_config['CHANNEL_ACCESS_TOKEN'])
handler = WebhookHandler(line_bot_config['CHANNEL_SECRET'])

@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        app.logger.info("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessageContent)
def handle_message(event):
    with ApiClient(configuration) as api_client:
        line_bot_api = MessagingApi(api_client)
        line_bot_api.reply_message_with_http_info(
            ReplyMessageRequest(
                reply_token=event.reply_token,
                messages=[TextMessage(text=event.message.text)]
            )
        )

if __name__ == "__main__":
    app.run()