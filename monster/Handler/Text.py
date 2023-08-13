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

def text_handler(event: MessageEvent) -> None:
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