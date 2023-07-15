# -*- coding: utf-8 -*-
'''
Create Date: 2023/07/07
Author: @1chooo(Hugo ChunHo Lin)
Version: v0.0.1
'''

import json
import os
from datetime import datetime
from linebot import LineBotApi
from linebot import WebhookHandler
from linebot.exceptions import LineBotApiError
from linebot.exceptions import InvalidSignatureError
from linebot.models import TextMessage
from linebot.models import ImageMessage
from linebot.models import VideoMessage
from linebot.models import AudioMessage
from linebot.models import TextSendMessage
from linebot.models.events import FollowEvent
from linebot.models.events import MessageEvent

config_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'config')
config_path = os.path.join(config_dir, 'linebot.conf')
line_bot_config = json.load(open(config_path, 'r', encoding='utf8'))

LINE_BOT_API = LineBotApi(line_bot_config["CHANNEL_ACCESS_TOKEN"])
HANDLER = WebhookHandler(line_bot_config["CHANNEL_SECRET"])

def handle_unknown_text_message(event) -> None:
    reply_message = []

    message1 = TextSendMessage(
        text='這句話我們還不認識，或許有一天我們會學起來！')
    reply_message.append(message1)

    LINE_BOT_API.reply_message(
        event.reply_token,
        reply_message
    )

def handle_invalid_text_message(event) -> None:
    LINE_BOT_API.reply_message(
        event.reply_token, 
        TextSendMessage(
            '我們目前還不能辨識您的這則訊息\n或許可以試試看別的內容哦～'
        )
    )

def handle_test_image_message(event) -> None:

    message_elements = [
        f"Image has been Uploaded\n{event.message.id}\non",
        str(datetime.now().strftime('%Y/%m/%d %H:%M:%S'))
    ]

    text = '\n'.join(message_elements)

    LINE_BOT_API.reply_message(
        event.reply_token,
        TextSendMessage(text=text)
    )

def handle_test_video_message(event) -> None:

    message_elements = [
        f"Video has been Uploaded\n{event.message.id}\non",
        str(datetime.now().strftime('%Y/%m/%d %H:%M:%S'))
    ]

    text = '\n'.join(message_elements)

    LINE_BOT_API.reply_message(
        event.reply_token,
        TextSendMessage(text=text)
    )

def handle_test_audio_message(event) -> None:

    message_elements = [
        f"Audio has been Uploaded\n{event.message.id}\non",
        str(datetime.now().strftime('%Y/%m/%d %H:%M:%S'))
    ]

    text = '\n'.join(message_elements)

    LINE_BOT_API.reply_message(
        event.reply_token,
        TextSendMessage(text=text)
    )

def handle_test_text_message(event) -> None:
    reply_messages = [
        TextSendMessage(text='Monster HiHi! Test 1'),
        TextSendMessage(text='HiHi! Test 2'),
        TextSendMessage(text='HiHi! Test 3')
    ]
            
    LINE_BOT_API.reply_message(
        event.reply_token,
        reply_messages
    )
