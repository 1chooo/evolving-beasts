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

    def handle_test_image_message(self, event):
        self.LINE_BOT_API.reply_message(
            event.reply_token,
            TextSendMessage(
                text='Image has been Uploaded ' +
                event.message.id +
                '\non ' +
                str(datetime.now().strftime('%Y/%m/%d %H:%M:%S'))
            )
        )

    def handle_test_audio_message(self, event):
        self.LINE_BOT_API.reply_message(
            event.reply_token,
            TextSendMessage(
                text='Audio has been Uploaded ' +
                event.message.id +
                '\non ' +
                str(datetime.now().strftime('%Y/%m/%d %H:%M:%S'))
            )
        )

    def handle_test_text_message(self, event) -> None:
        reply_message = []
        message1 = TextSendMessage(
            text='Monster HiHi! Test 1')
        reply_message.append(message1)
        message2 = TextSendMessage(
            text='HiHi! Test 2')
        reply_message.append(message2)
        message3 = TextSendMessage(
            text='HiHi! Test 3')
        reply_message.append(message3)
        
        self.LINE_BOT_API.reply_message(
            event.reply_token,
            reply_message
        )

# 在外部設置 LINE Bot API 相關變數
config_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'config')
config_path = os.path.join(config_dir, 'linebot.conf')
line_bot_config = json.load(open(config_path, 'r', encoding='utf8'))

LINE_BOT_API = LineBotApi(line_bot_config["CHANNEL_ACCESS_TOKEN"])
HANDLER = WebhookHandler(line_bot_config["CHANNEL_SECRET"])

# 創建 TestFunc 類別的實例並傳入外部變數
test_func = TestFunc(LINE_BOT_API, HANDLER)
