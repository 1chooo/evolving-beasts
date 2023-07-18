# -*- coding: utf-8 -*-
'''
Create Date: 2023/07/15
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

class TestFunc:
    
    def __init__(self, line_bot_api, handler):
        self.LINE_BOT_API = line_bot_api
        self.HANDLER = handler

    def handle_test_image_message(self, event) -> None:

        message_elements = [
            f"Image has been Uploaded\n{event.message.id}\non",
            str(datetime.now().strftime('%Y/%m/%d %H:%M:%S'))
        ]

        text = '\n'.join(message_elements)

        LINE_BOT_API.reply_message(
            event.reply_token,
            TextSendMessage(text=text)
        )
    
    def handle_test_video_message(self, event) -> None:

        message_elements = [
            f"Video has been Uploaded\n{event.message.id}\non",
            str(datetime.now().strftime('%Y/%m/%d %H:%M:%S'))
        ]

        text = '\n'.join(message_elements)

        LINE_BOT_API.reply_message(
            event.reply_token,
            TextSendMessage(text=text)
        )

    def handle_test_audio_message(self, event) -> None:

        message_elements = [
            f"Audio has been Uploaded\n{event.message.id}\non",
            str(datetime.now().strftime('%Y/%m/%d %H:%M:%S'))
        ]

        text = '\n'.join(message_elements)

        LINE_BOT_API.reply_message(
            event.reply_token,
            TextSendMessage(text=text)
        )

    def handle_test_text_message(self, event) -> None:
        reply_messages = [
            TextSendMessage(text='Monster HiHi! Test 1'),
            TextSendMessage(text='HiHi! Test 2'),
            TextSendMessage(text='HiHi! Test 3')
        ]
                
        LINE_BOT_API.reply_message(
            event.reply_token,
            reply_messages
        )

# 在外部設置 LINE Bot API 相關變數
config_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'config')
config_path = os.path.join(config_dir, 'linebot.conf')
line_bot_config = json.load(open(config_path, 'r', encoding='utf8'))

LINE_BOT_API = LineBotApi(line_bot_config["CHANNEL_ACCESS_TOKEN"])
HANDLER = WebhookHandler(line_bot_config["CHANNEL_SECRET"])

# 創建 TestFunc 類別的實例並傳入外部變數
test_func = TestFunc(LINE_BOT_API, HANDLER)

def line_bot_api_error_console(e: Exception) -> None:
    print(f'LineBotApiError: {str(e)}')

def user_info_console(user_profile) -> None:
    print(json.dumps(vars(user_profile)))

def user_info_exception_console(e: Exception) -> None:
    print(f'Error in getting user info: {str(e)}')

def store_user_info(USER_LOG_PATH: str, user_profile) -> None:
    file_path = os.path.join(USER_LOG_PATH, 'users-info.log')

    with open(file_path, 'a') as myfile:
        try:
            user_info_console(user_profile)
            myfile.write(json.dumps(vars(user_profile), sort_keys=True))
            myfile.write('\n')
        except Exception as e:      # Handling the fails when writing a file
            user_info_exception_console(e)

def user_event_exception_console(e: Exception) -> None:
    print(f'Error in getting user event: {str(e)}')

def store_user_event(USER_LOG_PATH: str, body: str) -> None:
    file_path = os.path.join(USER_LOG_PATH, 'users-event.log')
    
    with open(file_path, 'a') as output_file:
        try:
            output_file.write(body)
            output_file.write('\n')
        except Exception as e:      # Handling the fails when writing a file
            user_event_exception_console(e)

def text_exception_console(e: LineBotApiError) -> None:
    print(f'Error occurred: {str(e)}')

def image_exception_console(e: LineBotApiError) -> None:
    print(f'Unable to get Image message content: {str(e)}')

def video_exception_console(e: LineBotApiError) -> None:
    print(f'Unable to get Video message content: {str(e)}')

def audio_exception_console(e: LineBotApiError) -> None:
    print(f'Unable to get Audio message content: {str(e)}')

class ExceptionConsole:
    def __init__(self, line_bot_api, handler):
        self.LINE_BOT_API = line_bot_api
        self.HANDLER = handler

    def text_exception_console(self, e: LineBotApiError) -> None:
        print(f'Error occurred: {str(e)}')

    def image_exception_console(self, e: LineBotApiError) -> None:
        print(f'Unable to get Image message content: {str(e)}')

    def video_exception_console(self, e: LineBotApiError) -> None:
        print(f'Unable to get Video message content: {str(e)}')

    def audio_exception_console(self, e: LineBotApiError) -> None:
        print(f'Unable to get Audio message content: {str(e)}')

def handle_unknown_text_message(event: MessageEvent) -> None:
    reply_message = []

    message1 = TextSendMessage(
        text='這句話我們還不認識，或許有一天我們會學起來！')
    reply_message.append(message1)

    LINE_BOT_API.reply_message(
        event.reply_token,
        reply_message
    )

def handle_invalid_text_message(event: MessageEvent) -> None:
    LINE_BOT_API.reply_message(
        event.reply_token, 
        TextSendMessage(
            '我們目前還不能辨識您的這則訊息\n或許可以試試看別的內容哦～'
        )
    )

config_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'config')
config_path = os.path.join(config_dir, 'linebot.conf')
line_bot_config = json.load(open(config_path, 'r', encoding='utf8'))

LINE_BOT_API = LineBotApi(line_bot_config["CHANNEL_ACCESS_TOKEN"])
HANDLER = WebhookHandler(line_bot_config["CHANNEL_SECRET"])

def check_dir(file_path: str) -> None:
    if not os.path.isdir(file_path):
        os.mkdir(file_path, mode=0o777)
        print(file_path, 'has been created successfully.')

    return None

def get_output_path(
        file_path: str, CURRENT_DATE: str, id, file_type: str) -> str:
    filename = f"{CURRENT_DATE}_{id}{file_type}"
    output_path = os.path.join(file_path, filename)
    
    return output_path

def download_file(
        LINE_BOT_API: LineBotApi, USER_LOG_PATH: str, event, type: str, file_type: str, CURRENT_DATE: str) -> None:
    message_content = LINE_BOT_API.get_message_content(event.message.id)

    file_path = os.path.join(USER_LOG_PATH, type)
    check_dir(file_path)

    output_path = get_output_path(file_path, CURRENT_DATE, event.message.id, file_type)

    with open(output_path, 'wb') as fd:
        for chunk in message_content.iter_content():
            fd.write(chunk)