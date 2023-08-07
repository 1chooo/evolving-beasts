# -*- coding: utf-8 -*-
'''
Create Date: 2023/07/07
Author: @1chooo(Hugo ChunHo Lin)
Version: v0.0.1
'''

import os
import json
from pyimgur import Imgur
from datetime import datetime
from flask import Flask, request, abort
from swagger_ui import api_doc
from Monster.Drama import text_message_handler_map
from Monster.Drama import upload_drama
from Monster.Drama import check_monster_drama
from Monster.Drama import unknown_handler
from Monster.Drama import error_handler
from Monster.Utils import console_logger
from Monster.Utils import file_handler
from linebot import LineBotApi
from linebot import WebhookHandler
from linebot.models import TextMessage
from linebot.models import ImageMessage
from linebot.models import VideoMessage
from linebot.models import AudioMessage
from linebot.models.events import FollowEvent
from linebot.models.events import MessageEvent
from linebot.exceptions import LineBotApiError
from linebot.exceptions import InvalidSignatureError

app = Flask(__name__)

config_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '.', 'config')
line_bot_config_path = os.path.join(config_dir, 'linebot.conf')
line_bot_config = json.load(open(line_bot_config_path, 'r', encoding='utf8'))
imgur_config_path = os.path.join(config_dir, 'imgur.conf')
imgur_config = json.load(open(imgur_config_path, 'r', encoding='utf8'))

CURRENT_DATE = datetime.today().strftime('%Y%m%d')
LINE_BOT_API = LineBotApi(line_bot_config['CHANNEL_ACCESS_TOKEN'])
HANDLER = WebhookHandler(line_bot_config['CHANNEL_SECRET'])
IMGUR_CLIENT = Imgur(imgur_config["client_id"], imgur_config["client_secret"])
USER_LOG_PATH = os.path.join('.', 'log', CURRENT_DATE)

file_handler.create_directory(USER_LOG_PATH)

@app.route('/callback', methods=['POST'])
def callback() -> str:

    signature = request.headers['X-Line-Signature'] # get X-Line-Signature header value
    body = request.get_data(as_text=True)   # get request body as text

    console_logger.store_user_event(body, USER_LOG_PATH)

    try:        # handle webhook body
        HANDLER.handle(body, signature)
        
    except InvalidSignatureError:
        abort(400)

    return 'OK'

@HANDLER.add(FollowEvent)
def handle_user_profile(event: FollowEvent) -> None:
    
    try:
        user_profile = LINE_BOT_API.get_profile(event.source.user_id)
    except LineBotApiError as e:    # Handling the fails when obtaining the user profile
        console_logger.line_bot_api_error_console(e)
        return

    console_logger.store_user_info(user_profile, USER_LOG_PATH)

@HANDLER.add(MessageEvent, message=TextMessage)
def handle_text_message(event: MessageEvent) -> None:
    try:
        message_text = event.message.text
        
        if message_text in text_message_handler_map: # Check if the message text exists in the dictionary and call the corresponding handler function
            text_message_handler = text_message_handler_map[message_text]
            text_message_handler(event)
        elif check_monster_drama.ready_to_get_monster_name_or_not():
            check_monster_drama.handle_check_monster_rename_monster_test(event) # Ready rename
        elif check_monster_drama.ready_to_get_monster_name_or_not() \
            and upload_drama.ready_to_get_image_or_not():
            check_monster_drama.handle_check_monster_rename_monster_test(event) # Ready upload
        else:
            unknown_handler.handle_unknown_text_message(event)

    except Exception as e:
        console_logger.text_exception_console(e)
        error_handler.handle_invalid_text_message(event)

@HANDLER.add(MessageEvent, message=ImageMessage)
def handle_image_message(event: MessageEvent) -> None:
    try:    
        if upload_drama.ready_to_get_image_or_not():
            upload_drama.handle_upload_get_image(event)
        else:
            unknown_handler.handle_unknown_image_message(event)
        file_handler.download_file(event, 'imgs', '.jpg', USER_LOG_PATH)   # Download the image

    except LineBotApiError as e:
        console_logger.image_exception_console(e)
        error_handler.handle_invalid_image_message(event)

@HANDLER.add(MessageEvent, message=VideoMessage)
def handle_video_message(event: MessageEvent) -> None:
    try:    
        unknown_handler.handle_unknown_video_message(event)
        file_handler.download_file(event, 'video', '.mp4', USER_LOG_PATH)  # Download the audio

    except LineBotApiError as e:
        console_logger.image_exception_console(e)
        error_handler.handle_invalid_video_message(event)

@HANDLER.add(MessageEvent, message=AudioMessage)
def handle_audio_message(event: MessageEvent) -> None:
    try:    
        unknown_handler.handle_unknown_audio_message(event)
        file_handler.download_file(event, 'audio', '.mp3', USER_LOG_PATH)      # Download the audio

    except LineBotApiError as e:
        console_logger.audio_exception_console(e)
        error_handler.handle_invalid_audio_message(event)

def start_flask() -> None:
    app.run(port=5002)

def main() -> None:
    start_flask()

if __name__ == '__main__':
    main()
