# -*- coding: utf-8 -*-
'''
Create Date: 2023/07/07
Author: @1chooo(Hugo ChunHo Lin)
Version: v0.0.1
'''

import os
import json
import pandas as pd
import numpy as np
from datetime import datetime
from flask import Flask, request, abort
from Monster.Drama import upload_drama
from Monster.Drama import check_monster_drama
from Monster.Drama import check_news_drama
from Monster.Drama import upload_teaching_drama
from Monster.Drama import check_rank_drama
from Monster.Drama import about_us_drama
from Monster.Drama import test_handler
from Monster.Drama import error_handler
from Monster.Utils import ConsoleLogger
from Monster.Utils import FileHandler
from linebot import LineBotApi
from linebot import WebhookHandler
from linebot.models import TextMessage
from linebot.models import ImageMessage
from linebot.models import VideoMessage
from linebot.models import AudioMessage
from linebot.models import TextSendMessage
from linebot.models.events import FollowEvent
from linebot.models.events import MessageEvent
from linebot.exceptions import LineBotApiError
from linebot.exceptions import InvalidSignatureError

app = Flask(__name__)

config_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '.', 'config')
config_path = os.path.join(config_dir, 'linebot.conf')
line_bot_config = json.load(open(config_path, 'r', encoding='utf8'))

CURRENT_DATE = datetime.today().strftime('%Y%m%d')

LINE_BOT_API = LineBotApi(line_bot_config['CHANNEL_ACCESS_TOKEN'])
HANDLER = WebhookHandler(line_bot_config['CHANNEL_SECRET'])
USER_LOG_PATH = os.path.join('.', 'log', CURRENT_DATE)

console_logger = ConsoleLogger(LINE_BOT_API, HANDLER, USER_LOG_PATH)
file_handler = FileHandler(LINE_BOT_API, USER_LOG_PATH, CURRENT_DATE)

file_handler.create_directory(USER_LOG_PATH)

READY_TO_GET_MONSTER_NAME = False

@app.route('/callback', methods=['POST'])
def callback() -> str:
    global USER_LOG_PATH

    signature = request.headers['X-Line-Signature'] # get X-Line-Signature header value
    body = request.get_data(as_text=True)   # get request body as text

    console_logger.store_user_event(body)

    try:        # handle webhook body
        HANDLER.handle(body, signature)
        
    except InvalidSignatureError:
        abort(400)

    return 'OK'

@HANDLER.add(FollowEvent)
def handle_user_profile(event: FollowEvent) -> None:
    global USER_LOG_PATH
    
    try:
        user_profile = LINE_BOT_API.get_profile(event.source.user_id)
    except LineBotApiError as e:    # Handling the fails when obtaining the user profile
        console_logger.line_bot_api_error_console(e)
        return

    console_logger.store_user_info(user_profile)

CLIENT_MONSTER_NAME = ''
@HANDLER.add(MessageEvent, message=TextMessage)
def handle_text_message(event: MessageEvent) -> None:
    global READY_TO_GET_MONSTER_NAME
    global CLIENT_MONSTER_NAME
    
    try:
        if (event.message.text) == 'Hi Test':
            test_handler.handle_test_text_message(event)
        elif (event.message.text) == '我想上傳回收物📸':
            upload_drama.handle_upload_welcome_message(event)
        elif (event.message.text) == '我想關心怪獸🔦':
            check_monster_drama.handle_check_monster_welcome_message(event)
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
                    '測試成功'
                ),
            ]

            LINE_BOT_API.reply_message(
                event.reply_token,
                reply_messages
            )
        elif (event.message.text) == '我想關心永續新知🌏':
            check_news_drama.handle_check_news_welcome_message(event)
        elif (event.message.text) == '我想學習如何上傳回收物📖':
            upload_teaching_drama.handle_upload_teaching_welcome_message(event)
        elif (event.message.text) == '我已經看懂了！我想知道更多小怪怪的資訊！':
            upload_teaching_drama.handle_upload_teaching_welcome_yes_message(event)
        elif (event.message.text) == '我想看最強怪獸👾':
            check_rank_drama.handle_check_rank_welcome_message(event)
        elif (event.message.text) == '我想更認識你們👋🏻':
            about_us_drama.handle_about_us_welcome_message(event)
        elif (event.message.text) == '我想更認識開發者——林群賀':
            about_us_drama.handle_about_us_ho_message(event)
        elif (event.message.text) == '我想更認識資料前處理——周姿吟':
            about_us_drama.handle_about_us_chou_message(event)
        elif (event.message.text) == '我想更認識專案企劃——葉霈恩':
            about_us_drama.handle_about_us_yeh_message(event)
        elif (event.message.text) == '我想更認識模型訓練——林源煜':
            about_us_drama.handle_about_us_aaron_message(event)
        elif (event.message.text) == '我想認識成員——黃品誠':
            about_us_drama.handle_about_us_huang_message(event)
        else:
            error_handler.handle_unknown_text_message(event)

    except Exception as e:
        console_logger.text_exception_console(e)
        error_handler.handle_invalid_text_message(event)

@HANDLER.add(MessageEvent, message=ImageMessage)
def handle_image_message(event: MessageEvent) -> None:
    global USER_LOG_PATH

    test_handler.handle_test_image_message(event)

    try:    # Download the image
        file_handler.download_file(event, 'imgs', '.jpg')

    except LineBotApiError as e:
        console_logger.image_exception_console(e)
        error_handler.handle_invalid_image_message(event)

@HANDLER.add(MessageEvent, message=VideoMessage)
def handle_video_message(event: MessageEvent) -> None:
    global USER_LOG_PATH

    test_handler.handle_test_video_message(event)

    try:    # Download the audio
        file_handler.download_file(event, 'video', '.mp4')

    except LineBotApiError as e:
        console_logger.image_exception_console(e)
        error_handler.handle_invalid_video_message(event)

@HANDLER.add(MessageEvent, message=AudioMessage)
def handle_audio_message(event: MessageEvent) -> None:
    global USER_LOG_PATH

    test_handler.handle_test_audio_message(event)

    try:    # Download the audio
        file_handler.download_file(event, 'audio', '.mp3')

    except LineBotApiError as e:
        console_logger.audio_exception_console(e)
        error_handler.handle_invalid_audio_message(event)

def start_flask() -> None:
    app.run(port=5002)

def main() -> None:
    start_flask()

if __name__ == '__main__':
    main()
