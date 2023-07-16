# -*- coding: utf-8 -*-
'''
Create Date: 2023/07/07
Author: @1chooo(Hugo ChunHo Lin)
Version: v0.0.1
'''

import os
import json
from Monster import Utils
from Monster import Drama
from Monster.Drama import HandleTest
from datetime import datetime
from flask import Flask, request, abort
from linebot import LineBotApi
from linebot import WebhookHandler
from linebot.exceptions import LineBotApiError
from linebot.exceptions import InvalidSignatureError
from linebot.models import TextMessage
from linebot.models import ImageMessage
from linebot.models import VideoMessage
from linebot.models import AudioMessage
from linebot.models.events import FollowEvent
from linebot.models.events import MessageEvent

app = Flask(__name__)

config_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '.', 'config')
config_path = os.path.join(config_dir, 'linebot.conf')
line_bot_config = json.load(open(config_path, 'r', encoding='utf8'))

CURRENT_DATE = datetime.today().strftime('%Y%m%d')

LINE_BOT_API = LineBotApi(line_bot_config['CHANNEL_ACCESS_TOKEN'])
HANDLER = WebhookHandler(line_bot_config['CHANNEL_SECRET'])
USER_LOG_PATH = os.path.join('.', 'log', CURRENT_DATE)

Utils.check_dir(USER_LOG_PATH)
handle_test = HandleTest(LINE_BOT_API, HANDLER)

@app.route('/callback', methods=['POST'])
def callback() -> str:

    global USER_LOG_PATH

    signature = request.headers['X-Line-Signature'] # get X-Line-Signature header value
    body = request.get_data(as_text=True)   # get request body as text

    Utils.store_user_event(USER_LOG_PATH, body)

    try:        # handle webhook body
        HANDLER.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'

@HANDLER.add(FollowEvent)
def handle_user_profile(event) -> None:
    
    global USER_LOG_PATH
    
    try:
        user_profile = LINE_BOT_API.get_profile(event.source.user_id)
    except LineBotApiError as e:    # Handling the fails when obtaining the user profile
        Utils.line_bot_api_error_console(e)
        return

    Utils.store_user_info(USER_LOG_PATH, user_profile)
        
@HANDLER.add(MessageEvent, message=TextMessage)
def handle_text_message(event) -> None:

    try:
        if (event.message.text) == 'Hi Test':
            handle_test.handle_test_text_message(event)
        else:
            Drama.handle_unknown_text_message(event)

    except Exception as e:
        Utils.text_exception_console(e)
        Drama.handle_invalid_text_message(event)

@HANDLER.add(MessageEvent, message=ImageMessage)
def handle_image_message(event) -> None:

    global USER_LOG_PATH

    handle_test.handle_test_image_message(event)

    try:    # Download the image
        Utils.download_file(
            LINE_BOT_API, USER_LOG_PATH, event, 
            'imgs', '.jpg', CURRENT_DATE
        )

    except LineBotApiError as e:
        Utils.image_exception_console(e)

@HANDLER.add(MessageEvent, message=VideoMessage)
def handle_video_message(event) -> None:

    global USER_LOG_PATH

    handle_test.handle_test_video_message(event)

    try:    # Download the audio
        Utils.download_file(
            LINE_BOT_API, USER_LOG_PATH, event, 
            'video', '.mp4', CURRENT_DATE
        )

    except LineBotApiError as e:
        Utils.image_exception_console(e)

@HANDLER.add(MessageEvent, message=AudioMessage)
def handle_audio_message(event) -> None:

    global USER_LOG_PATH

    handle_test.handle_test_audio_message(event)

    try:    # Download the audio
        Utils.download_file(
            LINE_BOT_API, USER_LOG_PATH, event, 
            'audio', '.mp3', CURRENT_DATE
        )

    except LineBotApiError as e:
        Utils.audio_exception_console(e)

def start_flask() -> None:
    app.run(port=5002)

def main() -> None:
    start_flask()

if __name__ == '__main__':
    main()
