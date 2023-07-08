# -*- coding: utf-8 -*-
'''
Create Date: 2023/07/07
Author: @1chooo(Hugo ChunHo Lin)
Version: v0.0.1
'''

import linebot
import linebot.models
import json
import os
import datetime

config_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'config')
config_path = os.path.join(config_dir, 'linebot.conf')
line_bot_config = json.load(open(config_path, 'r', encoding='utf8'))

LINE_BOT_API = linebot.LineBotApi(line_bot_config["CHANNEL_ACCESS_TOKEN"])
HANDLER = linebot.WebhookHandler(line_bot_config["CHANNEL_SECRET"])



def handle_unknown_text_message(event) -> None:
    reply_message = []

    message1 = linebot.models.TextSendMessage(
        text='這句話我們還不認識，或許有一天我們會學起來！')
    reply_message.append(message1)

    LINE_BOT_API.reply_message(
        event.reply_token,
        reply_message
    )

def handle_invalid_text_message(event) -> None:
    LINE_BOT_API.reply_message(
        event.reply_token, 
        linebot.models.TextSendMessage('''我們目前還不能辨識您的這則訊息\n或許可以試試看別的內容哦～''')
    )

def handle_test_image_message(event) -> None:

    LINE_BOT_API.reply_message(
        event.reply_token,
        linebot.models.TextSendMessage(
            text='Image has been Uploaded ' + 
            event.message.id + 
            '\non ' +
            str(datetime.datetime.now().strftime('%Y/%m/%d %H:%M:%S'))
        )
    )

def handle_test_audio_message(event) -> None:

    LINE_BOT_API.reply_message(
        event.reply_token,
        linebot.models.TextSendMessage(
            text='Audio has been Uploaded ' + 
            event.message.id + 
            '\non ' +
            str(datetime.datetime.now().strftime('%Y/%m/%d %H:%M:%S'))
        )
    )

def handle_test_text_message(event) -> None:
    reply_message = []
    message1 = linebot.models.TextSendMessage(
        text='Monster HiHi! Test 1')
    reply_message.append(message1)
    message2 = linebot.models.TextSendMessage(
        text='HiHi! Test 2')
    reply_message.append(message2)
    message3 = linebot.models.TextSendMessage(
        text='HiHi! Test 3')
    reply_message.append(message3)
    
    LINE_BOT_API.reply_message(
        event.reply_token,
        reply_message
    )

class TestFunc:
    
    def __init__(self):
        config_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'config')
        config_path = os.path.join(config_dir, 'linebot.conf')
        line_bot_config = json.load(open(config_path, 'r', encoding='utf8'))
        
        self.LINE_BOT_API = linebot.LineBotApi(line_bot_config["CHANNEL_ACCESS_TOKEN"])
        self.HANDLER = linebot.WebhookHandler(line_bot_config["CHANNEL_SECRET"])

    def handle_test_image_message(self, event):
        self.LINE_BOT_API.reply_message(
            event.reply_token,
            linebot.models.TextSendMessage(
                text='Image has been Uploaded ' +
                event.message.id +
                '\non ' +
                str(datetime.datetime.now().strftime('%Y/%m/%d %H:%M:%S'))
            )
        )

    def handle_test_audio_message(self, event):
        self.LINE_BOT_API.reply_message(
            event.reply_token,
            linebot.models.TextSendMessage(
                text='Audio has been Uploaded ' +
                event.message.id +
                '\non ' +
                str(datetime.datetime.now().strftime('%Y/%m/%d %H:%M:%S'))
            )
        )

    def handle_test_text_message(self, event) -> None:
        reply_message = []
        message1 = linebot.models.TextSendMessage(
            text='Monster HiHi! Test 1')
        reply_message.append(message1)
        message2 = linebot.models.TextSendMessage(
            text='HiHi! Test 2')
        reply_message.append(message2)
        message3 = linebot.models.TextSendMessage(
            text='HiHi! Test 3')
        reply_message.append(message3)
        
        self.LINE_BOT_API.reply_message(
            event.reply_token,
            reply_message
        )

