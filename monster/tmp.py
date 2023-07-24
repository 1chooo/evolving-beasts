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

'''
'''

from Drama import AboutUsDrama
from Drama import TestHandler
from Drama import ErrorHandler
from Utils import ConsoleLogger
from Utils import FileHandler

config_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '.', 'config')
config_path = os.path.join(config_dir, 'linebot.conf')
line_bot_config = json.load(open(config_path, 'r', encoding='utf8'))

CURRENT_DATE = datetime.today().strftime('%Y%m%d')

LINE_BOT_API = LineBotApi(line_bot_config['CHANNEL_ACCESS_TOKEN'])
HANDLER = WebhookHandler(line_bot_config['CHANNEL_SECRET'])
USER_LOG_PATH = os.path.join('.', 'log', CURRENT_DATE)

about_us_drama = AboutUsDrama(LINE_BOT_API, HANDLER)
test_handler = TestHandler(LINE_BOT_API, HANDLER)
error_handler = ErrorHandler(LINE_BOT_API, HANDLER)
console_logger = ConsoleLogger(LINE_BOT_API, HANDLER, USER_LOG_PATH)
file_handler = FileHandler(LINE_BOT_API, USER_LOG_PATH, CURRENT_DATE)

print("Received text:", event.message.text)

message_handlers = {
    
    'Hi Test': test_handler.handle_test_text_message,
    '我想上傳回收物📸': test_handler.handle_test_text_message,
    '我想關心怪獸🔦': test_handler.handle_test_text_message,
    '我想關心永續新知🌏': test_handler.handle_test_text_message,
    '我想學習如何上傳回收物📖': test_handler.handle_test_text_message,
    '我想看最強怪獸👾': test_handler.handle_test_text_message,
    '我想更認識你們👋🏻': about_us_drama.handle_about_us_message,
    '我想認識成員——林群賀': about_us_drama.handle_about_us_test,
    '我想認識成員——葉霈恩': about_us_drama.handle_about_us_test,
    '我想認識成員——黃品誠': about_us_drama.handle_about_us_test,
    '我想認識成員——林源煜': about_us_drama.handle_about_us_test,
    '我想認識成員——周姿吟': about_us_drama.handle_about_us_test,
}

# 獲取訊息文字
message_text = event.message.text

# 根據訊息文字選擇相應的處理函式，若找不到則使用預設的錯誤處理函式
message_handler = message_handlers.get(message_text, error_handler.handle_unknown_text_message)

        # 呼叫相應的處理函式處理訊息
message_handler(event)

if (event.message.text) == 'Hi Test':
    test_handler.handle_test_text_message(event)
elif (event.message.text) == '我想上傳回收物📸':
    test_handler.handle_test_text_message(event)
elif (event.message.text) == '我想關心怪獸🔦':
    test_handler.handle_test_text_message(event)
elif (event.message.text) == '我想關心永續新知🌏':
    test_handler.handle_test_text_message(event)
elif (event.message.text) == '我想學習如何上傳回收物📖':
    test_handler.handle_test_text_message(event)
elif (event.message.text) == '我想看最強怪獸👾':
    test_handler.handle_test_text_message(event)
elif (event.message.text) == '我想更認識你們👋🏻':
    about_us_drama.handle_about_us_message(event)
elif (event.message.text) == '我想認識成員——林群賀':
    about_us_drama.handle_about_us_test(event)
else:
    error_handler.handle_unknown_text_message(event)

message_text = event.message.text
        message_handler = message_handlers.get(
            message_text, # Retrieve the corresponding message handler function from the dictionary,
            error_handler.handle_unknown_text_message # error handler if not found
        )

        message_handler(event)  # Call the corresponding message handler function to process the message

elif READY_TO_GET_MONSTER_NAME == True:
    print('準備讓用戶重新命名小怪怪')
    CLIENT_MONSTER_NAME = event.message.text
    READY_TO_GET_MONSTER_NAME = False
    print(f'已將用戶怪獸名稱重新命名為{CLIENT_MONSTER_NAME}')

    reply_messages = [
        TextSendMessage(
            '已成功收到怪獸命名\n您的怪獸名稱是「' + CLIENT_MONSTER_NAME + '」！'
        ),
        TextSendMessage(
        '測試成功'),
    ]

    LINE_BOT_API.reply_message(
        event.reply_token,
        reply_messages)


def handle_message(event):
    message_text = event.message.text

    # Define a dictionary to map message texts to handler functions
    message_handler_map = {
        'Hi Test': test_handler.handle_test_text_message,
        '我想上傳回收物📸': upload_drama.handle_upload_welcome_message,
        '我想關心怪獸🔦': check_monster_drama.handle_check_monster_welcome_message,
        '我想關心永續新知🌏': check_news_drama.handle_check_news_welcome_message,
        '我想學習如何上傳回收物📖': upload_teaching_drama.handle_upload_teaching_welcome_message,
        '我已經看懂了！我想知道更多小怪怪的資訊！': upload_teaching_drama.handle_upload_teaching_welcome_yes_message,
        '我想看最強怪獸👾': check_rank_drama.handle_check_rank_welcome_message,
        '我想更認識你們👋🏻': about_us_drama.handle_about_us_welcome_message,
        '我想更認識開發者——林群賀': about_us_drama.handle_about_us_ho_message,
        '我想更認識資料前處理——周姿吟': about_us_drama.handle_about_us_chou_message,
        '我想更認識專案企劃——葉霈恩': about_us_drama.handle_about_us_yeh_message,
        '我想更認識模型訓練——林源煜': about_us_drama.handle_about_us_aaron_message,
        '我想認識成員——黃品誠': about_us_drama.handle_about_us_huang_message,
    }

    # Check if the message text exists in the dictionary and call the corresponding handler function
    if message_text in message_handler_map:
        handler_function = message_handler_map[message_text]
        handler_function(event)
    elif READY_TO_GET_MONSTER_NAME:
        print('準備讓用戶重新命名小怪怪')
        CLIENT_MONSTER_NAME = event.message.text
        READY_TO_GET_MONSTER_NAME = False
        print(f'已將用戶怪獸名稱重新命名為{CLIENT_MONSTER_NAME}')

        reply_messages = [
            TextSendMessage(
                '已成功收到怪獸命名\n您的怪獸名稱是「' + CLIENT_MONSTER_NAME + '」！'
            ),
            TextSendMessage(
                '測試成功'
            ),
        ]

        LINE_BOT_API.reply_message(
            event.reply_token,
            reply_messages
        )
    else:
        error_handler.handle_unknown_text_message(event)


ImageSendMessage(
    original_content_url = "https://www.notebookcheck.net/fileadmin/_processed_/b/1/csm_teaser_87a40a99d2.jpg",
    preview_image_url = "https://www.notebookcheck.net/fileadmin/_processed_/b/1/csm_teaser_87a40a99d2.jpg",
),

ImageSendMessage(
    original_content_url = "https://store.storeimages.cdn-apple.com/8756/as-images.apple.com/is/refurb-mbp16touch-silver-gallery-2019?wid=1144&hei=1144&fmt=jpeg&qlt=90&.v=1582233083340",
    preview_image_url = "https://store.storeimages.cdn-apple.com/8756/as-images.apple.com/is/refurb-mbp16touch-silver-gallery-2019?wid=1144&hei=1144&fmt=jpeg&qlt=90&.v=1582233083340",
),

TemplateSendMessage(
    alt_text='Buttons template',
    template=ButtonsTemplate(
        title='Hello',
        text='第一次見面嗎',
        actions=[
            MessageTemplateAction(
                label='是，第一次見面',
                text='是',
            ),
            MessageTemplateAction(
                label='已經見過了',
                text='見過了',
            ),
        ]
    )
)
