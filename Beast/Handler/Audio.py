# -*- coding: utf-8 -*-
'''
Create Date: 2023/08/13
Author: @1chooo(Hugo ChunHo Lin)
Version: v0.0.2
'''

import os
import json
from pyimgur import Imgur
from datetime import datetime
from flask import Flask, request, abort
from flasgger import Swagger
from flasgger import LazyString
from flasgger import LazyJSONEncoder
from flasgger import swag_from
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

def audio_handler(event: MessageEvent, USER_LOG_PATH: str) -> None:
    try:    
        unknown_handler.handle_unknown_audio_message(event)
        file_handler.download_file(event, 'audio', '.mp3', USER_LOG_PATH)      # Download the audio

    except LineBotApiError as e:
        console_logger.audio_exception_console(e)
        error_handler.handle_invalid_audio_message(event)