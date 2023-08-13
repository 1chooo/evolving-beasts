# -*- coding: utf-8 -*-
'''
Create Date: 2023/08/13
Author: @1chooo(Hugo ChunHo Lin)
Version: v0.0.2
'''

import json
from pyimgur import Imgur
from datetime import datetime
from flask import Flask, request, abort
from flasgger import Swagger
from flasgger import LazyString
from flasgger import LazyJSONEncoder
from flasgger import swag_from
from Monster.Utils import console_logger
from Monster.Utils import file_handler
from linebot import LineBotApi
from Monster.Handler.Text import text_handler
from Monster.Handler.Image import image_handler
from Monster.Handler.Video import video_handler
from Monster.Handler.Audio import audio_handler
from Monster.Handler.Follow import follow_handler
from linebot import WebhookHandler
from linebot.models import TextMessage
from linebot.models import ImageMessage
from linebot.models import VideoMessage
from linebot.models import AudioMessage
from linebot.models.events import FollowEvent
from linebot.models.events import MessageEvent
from linebot.exceptions import LineBotApiError
from linebot.exceptions import InvalidSignatureError
from os.path import join
from os.path import dirname
from os.path import abspath

app = Flask(__name__)

config_dir = join(dirname(abspath(__file__)), '..', '..', 'config')
line_bot_config_path = join(config_dir, 'linebot.conf')
line_bot_config = json.load(open(line_bot_config_path, 'r', encoding='utf8'))
imgur_config_path = join(config_dir, 'imgur.conf')
imgur_config = json.load(open(imgur_config_path, 'r', encoding='utf8'))

CURRENT_DATE = datetime.today().strftime('%Y%m%d')
LINE_BOT_API = LineBotApi(line_bot_config['CHANNEL_ACCESS_TOKEN'])
HANDLER = WebhookHandler(line_bot_config['CHANNEL_SECRET'])
IMGUR_CLIENT = Imgur(imgur_config["client_id"], imgur_config["client_secret"])
USER_LOG_PATH = join(dirname(abspath(__file__)), '..', '..', 'config', CURRENT_DATE)
file_handler.create_directory(USER_LOG_PATH)

@app.route('/callback', methods=['POST'])
def callback() -> str:
    try:
        signature = request.headers['X-Line-Signature']
        body = request.get_data(as_text=True)

        # Log the callback payload and signature
        console_logger.store_user_event(body, USER_LOG_PATH)

        HANDLER.handle(body, signature)

        # Print a success message (you can log this message instead)
        print("Callback processed successfully")

    except InvalidSignatureError:
        # Log the error for debugging purposes
        console_logger.store_user_event("InvalidSignatureError: Failed to verify the signature", USER_LOG_PATH)
        print("InvalidSignatureError: Failed to verify the signature")
        abort(400)

    except Exception as e:
        # Log the error for debugging purposes
        console_logger.store_user_event(f"Error during callback processing: {str(e)}", USER_LOG_PATH)
        print(f"Error during callback processing: {str(e)}")
        return 'Error', 500

    return 'OK'

@HANDLER.add(FollowEvent)
def handle_user_profile(event: FollowEvent) -> None:
    follow_handler(event, LINE_BOT_API, USER_LOG_PATH)

@HANDLER.add(MessageEvent, message=TextMessage)
def handle_text_message(event: MessageEvent) -> None:
    text_handler(event)

@HANDLER.add(MessageEvent, message=ImageMessage)
def handle_image_message(event: MessageEvent) -> None:
    image_handler(event, USER_LOG_PATH)

@HANDLER.add(MessageEvent, message=VideoMessage)
def handle_video_message(event: MessageEvent) -> None:
    video_handler(event, USER_LOG_PATH)

@HANDLER.add(MessageEvent, message=AudioMessage)
def handle_audio_message(event: MessageEvent) -> None:
    audio_handler(event, USER_LOG_PATH)

def start_flask() -> None:
    app.run(port=5002)
