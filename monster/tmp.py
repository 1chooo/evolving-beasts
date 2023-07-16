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
