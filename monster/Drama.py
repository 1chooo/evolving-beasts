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

class ErrorHandler:
    def __init__(self, line_bot_api, handler):
        self.LINE_BOT_API = line_bot_api
        self.HANDLER = handler

    def handle_unknown_text_message(self, event: MessageEvent) -> None:
        reply_message = []

        message1 = TextSendMessage(
            text='這句話我們還不認識，或許有一天我們會學起來！')
        reply_message.append(message1)

        self.LINE_BOT_API.reply_message(
            event.reply_token,
            reply_message
        )

    def handle_invalid_text_message(self, event: MessageEvent) -> None:
        self.LINE_BOT_API.reply_message(
            event.reply_token, 
            TextSendMessage(
                '我們目前還不能辨識您的這則文字訊息\n或許可以試試看別的內容哦～'
            )
        )
    
    def handle_invalid_image_message(self, event: MessageEvent) -> None:
        self.LINE_BOT_API.reply_message(
            event.reply_token, 
            TextSendMessage(
                '我們目前還不能辨識您的這則圖片訊息\n或許可以試試看別的內容哦～'
            )
        )

    def handle_invalid_video_message(self, event: MessageEvent) -> None:
        self.LINE_BOT_API.reply_message(
            event.reply_token, 
            TextSendMessage(
                '我們目前還不能辨識您的這則影片訊息\n或許可以試試看別的內容哦～'
            )
        )

    def handle_invalid_audio_message(self, event: MessageEvent) -> None:
        self.LINE_BOT_API.reply_message(
            event.reply_token, 
            TextSendMessage(
                '我們目前還不能辨識您的這則語音訊息\n或許可以試試看別的內容哦～'
            )
        )

class TestHandler:
    
    def __init__(self, line_bot_api: LineBotApi, handler: WebhookHandler):
        self.LINE_BOT_API = line_bot_api
        self.HANDLER = handler

    def handle_test_image_message(self, event: MessageEvent) -> None:
        message_elements = [
            f"Image has been Uploaded\n{event.message.id}\non",
            str(datetime.now().strftime('%Y/%m/%d %H:%M:%S'))
        ]

        text = '\n'.join(message_elements)

        LINE_BOT_API.reply_message(
            event.reply_token,
            TextSendMessage(text=text)
        )
    
    def handle_test_video_message(self, event: MessageEvent) -> None:
        message_elements = [
            f"Video has been Uploaded\n{event.message.id}\non",
            str(datetime.now().strftime('%Y/%m/%d %H:%M:%S'))
        ]

        text = '\n'.join(message_elements)

        LINE_BOT_API.reply_message(
            event.reply_token,
            TextSendMessage(text=text)
        )

    def handle_test_audio_message(self, event: MessageEvent) -> None:
        message_elements = [
            f"Audio has been Uploaded\n{event.message.id}\non",
            str(datetime.now().strftime('%Y/%m/%d %H:%M:%S'))
        ]

        text = '\n'.join(message_elements)

        LINE_BOT_API.reply_message(
            event.reply_token,
            TextSendMessage(text=text)
        )

    def handle_test_text_message(self, event: MessageEvent) -> None:
        reply_messages = [
            TextSendMessage(text='Monster HiHi! Test 1'),
            TextSendMessage(text='HiHi! Test 2'),
            TextSendMessage(text='HiHi! Test 3')
        ]
                
        LINE_BOT_API.reply_message(
            event.reply_token,
            reply_messages
        )

class AboutUsDrama:
    
    def __init__(self, line_bot_api: LineBotApi, handler: WebhookHandler):
        self.LINE_BOT_API = line_bot_api
        self.HANDLER = handler

    def handle_about_us_test(self, event: MessageEvent) -> None:
        reply_messages = [
            TextSendMessage(text='看來你想多認識我們呢！'),
            TextSendMessage(text='再給我們一段時間，我們即將譜出專屬於我們的樂章🎶'),
            TextSendMessage(text='近請期待～')
        ]
                
        LINE_BOT_API.reply_message(
            event.reply_token,
            reply_messages
        )