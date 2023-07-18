# -*- coding: utf-8 -*-
'''
Create Date: 2023/07/07
Author: @1chooo(Hugo ChunHo Lin)
Version: v0.0.1
'''

import os
import json
from datetime import datetime
from linebot import LineBotApi
from linebot import WebhookHandler
from linebot.models import TextSendMessage
from linebot.models import ImageSendMessage
from linebot.models import ImageCarouselTemplate
from linebot.models import ImageCarouselColumn
from linebot.models import TemplateSendMessage
from linebot.models import MessageTemplateAction
from linebot.models import PostbackAction
from linebot.models import MessageAction
from linebot.models import URIAction
from linebot.models import QuickReplyButton
from linebot.models import LocationAction
from linebot.models import DatetimePickerAction
from linebot.models import RichMenuSwitchAction
from linebot.models import CarouselColumn
from linebot.models.template import CarouselTemplate
from linebot.models.template import ButtonsTemplate
from linebot.models.template import ConfirmTemplate
from linebot.models.events import MessageEvent

class ErrorHandler:
    def __init__(self, line_bot_api: LineBotApi, handler: WebhookHandler):
        self.LINE_BOT_API = line_bot_api
        self.HANDLER = handler

    def handle_unknown_text_message(self, event: MessageEvent) -> None:
        reply_messages = [
            TextSendMessage(text='這句話怪獸還不認識誒，或許有一天我們會幫助怪熟學起來！'),
        ]
                
        self.LINE_BOT_API.reply_message(
            event.reply_token,
            reply_messages
        )

    def handle_invalid_text_message(self, event: MessageEvent) -> None:
        reply_messages = [
            TextSendMessage(text='我們目前還不能辨識您的這則文字訊息\n或許可以試試看別的內容哦～'),
        ]
                
        self.LINE_BOT_API.reply_message(
            event.reply_token,
            reply_messages
        )
    
    def handle_invalid_image_message(self, event: MessageEvent) -> None:
        reply_messages = [
            TextSendMessage(text='我們目前還不能辨識您的這則圖片訊息\n或許可以試試看別的內容哦～'),
        ]
                
        self.LINE_BOT_API.reply_message(
            event.reply_token,
            reply_messages
        )

    def handle_invalid_video_message(self, event: MessageEvent) -> None:
        reply_messages = [
            TextSendMessage(text='我們目前還不能辨識您的這則影片訊息\n或許可以試試看別的內容哦～'),
        ]
                
        self.LINE_BOT_API.reply_message(
            event.reply_token,
            reply_messages
        )

    def handle_invalid_audio_message(self, event: MessageEvent) -> None:
        reply_messages = [
            TextSendMessage(text='我們目前還不能辨識您的這則語音訊息\n或許可以試試看別的內容哦～'),
        ]
                
        self.LINE_BOT_API.reply_message(
            event.reply_token,
            reply_messages
        )

class TestHandler:
    
    def __init__(self, line_bot_api: LineBotApi, handler: WebhookHandler):
        self.LINE_BOT_API = line_bot_api
        self.HANDLER = handler

    def handle_test_image_message(self, event: MessageEvent) -> None:
        reply_messages = [
            TextSendMessage(
                text=f"Image has been Uploaded\n"
                     f"{event.message.id}\n"
                     f"on\n"
                     f"{str(datetime.now().strftime('%Y/%m/%d %H:%M:%S'))}"
            )
        ]

        self.LINE_BOT_API.reply_message(
            event.reply_token,
            reply_messages
        )
    
    def handle_test_video_message(self, event: MessageEvent) -> None:
        reply_messages = [
            TextSendMessage(
                text=f"Video has been Uploaded\n"
                     f"{event.message.id}\n"
                     f"on\n"
                     f"{str(datetime.now().strftime('%Y/%m/%d %H:%M:%S'))}"
            )
        ]

        self.LINE_BOT_API.reply_message(
            event.reply_token,
            reply_messages
        )

    def handle_test_audio_message(self, event: MessageEvent) -> None:
        reply_messages = [
            TextSendMessage(
                text=f"Audio has been Uploaded\n"
                     f"{event.message.id}\n"
                     f"on\n"
                     f"{str(datetime.now().strftime('%Y/%m/%d %H:%M:%S'))}"
            )
        ]

        self.LINE_BOT_API.reply_message(
            event.reply_token,
            reply_messages
        )

    def handle_test_text_message(self, event: MessageEvent) -> None:
        reply_messages = [
            TextSendMessage(text='Monster HiHi! Test 1'),
            TextSendMessage(text='HiHi! Test 2'),
            TextSendMessage(text='HiHi! Test 3')
        ]
                
        self.LINE_BOT_API.reply_message(
            event.reply_token,
            reply_messages
        )

class AboutUsDrama:
    
    def __init__(self, line_bot_api: LineBotApi, handler: WebhookHandler):
        self.LINE_BOT_API = line_bot_api
        self.HANDLER = handler

    def handle_about_us_test(self, event: MessageEvent) -> None:
        reply_messages = [
            TextSendMessage(text='看來你想多認識我們呢！'),
            TextSendMessage(text='再給我們一段時間，我們即將譜出專屬於我們的樂章🎶'),
            TextSendMessage(text='近請期待～'),
            ImageSendMessage(
                original_content_url = "https://hackmd.io/_uploads/H1mI3GVq3.jpg",
                preview_image_url = "https://hackmd.io/_uploads/H1mI3GVq3.jpg",
            ),
            TemplateSendMessage(
                alt_text='ImageCarousel template',
                template=ImageCarouselTemplate(
                    columns=[
                        ImageCarouselColumn(
                            image_url='https://upload.wikimedia.org/wikipedia/en/a/a6/Pok%C3%A9mon_Pikachu_art.png',
                            action=MessageAction(
                                label='皮卡丘',
                                text='皮卡丘'
                            )
                        ),
                        ImageCarouselColumn(
                            image_url='https://upload.wikimedia.org/wikipedia/en/5/59/Pok%C3%A9mon_Squirtle_art.png',
                            action=MessageAction(
                                label='傑尼龜',
                                text='傑尼龜'
                            )
                        ),
                        ImageCarouselColumn(
                            image_url='https://upload.wikimedia.org/wikipedia/en/5/59/Pok%C3%A9mon_Squirtle_art.png',
                            action=MessageAction(
                                label='傑尼龜',
                                text='傑尼龜'
                            )
                        ),
                        ImageCarouselColumn(
                            image_url='https://upload.wikimedia.org/wikipedia/en/5/59/Pok%C3%A9mon_Squirtle_art.png',
                            action=MessageAction(
                                label='傑尼龜',
                                text='傑尼龜'
                            )
                        ),
                        ImageCarouselColumn(
                            image_url='https://upload.wikimedia.org/wikipedia/en/5/59/Pok%C3%A9mon_Squirtle_art.png',
                            action=MessageAction(
                                label='傑尼龜',
                                text='傑尼龜'
                            )
                        )
                    ]
                )
            )
        ]
                
        self.LINE_BOT_API.reply_message(
            event.reply_token,
            reply_messages
        )

    def handle_about_us_message(self, event: MessageEvent) -> None:
        reply_messages = [
            TextSendMessage(
                text="嗨你好啊！我們是「天氣 Hackthon 沙士比亞🌤」團隊，是一群來自不同系所並且喜歡嘗試新事物的一群熱血份子。☄️"
            ),
            TextSendMessage(
                text="我們想要將永續概念🌱結合機器學習或圖像辨識，以提供碳追蹤的系統，最後實作在大家日常生活中常使用的通訊軟體 - LINE。"
            ),
            TextSendMessage(
                text="我們秉持著與資訊工程💻結合的開源精神並且結合共筆概念管理團隊組織運作，像是個小型新創的超級新星🌟。"
            ),
            TextSendMessage(
                text="以下是我們的成員介紹，快點擊圖片來更進一步認識我們吧！🫵🏻"
            ),
            TemplateSendMessage(
                alt_text='ImageCarousel template',
                template=ImageCarouselTemplate(
                    columns=[
                        ImageCarouselColumn(
                            image_url='https://hackmd.io/_uploads/BkUURMVqh.jpg',
                            action=MessageAction(
                                label='開發者——林群賀',
                                text='我想認識成員——林群賀'
                            )
                        ),
                        ImageCarouselColumn(
                            image_url='https://upload.wikimedia.org/wikipedia/en/5/59/Pok%C3%A9mon_Squirtle_art.png',
                            action=MessageAction(
                                label='傑尼龜',
                                text='我想認識成員——葉霈恩'
                            )
                        ),
                        ImageCarouselColumn(
                            image_url='https://upload.wikimedia.org/wikipedia/en/5/59/Pok%C3%A9mon_Squirtle_art.png',
                            action=MessageAction(
                                label='傑尼龜',
                                text='我想認識成員——黃品誠'
                            )
                        ),
                        ImageCarouselColumn(
                            image_url='https://upload.wikimedia.org/wikipedia/en/5/59/Pok%C3%A9mon_Squirtle_art.png',
                            action=MessageAction(
                                label='傑尼龜',
                                text='我想認識成員——林源煜'
                            )
                        ),
                        ImageCarouselColumn(
                            image_url='https://upload.wikimedia.org/wikipedia/en/5/59/Pok%C3%A9mon_Squirtle_art.png',
                            action=MessageAction(
                                label='傑尼龜',
                                text='我想認識成員——周姿吟'
                            )
                        )
                    ]
                )
            )
        ]
        
        self.LINE_BOT_API.reply_message(
            event.reply_token,
            reply_messages
        )

config_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'config')
config_path = os.path.join(config_dir, 'linebot.conf')
line_bot_config = json.load(open(config_path, 'r', encoding='utf8'))

LINE_BOT_API = LineBotApi(line_bot_config["CHANNEL_ACCESS_TOKEN"])
HANDLER = WebhookHandler(line_bot_config["CHANNEL_SECRET"])

about_us_drama = AboutUsDrama(LINE_BOT_API, HANDLER)
test_handler = TestHandler(LINE_BOT_API, HANDLER)
error_handler = ErrorHandler(LINE_BOT_API, HANDLER)

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