# -*- coding: utf-8 -*-
'''
Create Date: 2023/08/02
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
from Monster.Utils import file_handler
import pymysql

class UnknownHandler:
    def __init__(self, line_bot_api: LineBotApi, handler: WebhookHandler):
        self.LINE_BOT_API = line_bot_api
        self.HANDLER = handler

    def handle_unknown_text_message(self, event: MessageEvent) -> None:
        reply_messages = [
            TextSendMessage(
                text=f'小怪怪目前還不能辨識您的這則文字訊息\n'
                     f'再嘗試投餵多投餵點食物給小怪怪吧～\n'
                     f'讓他早日學起來🤤🤤🤤'
            ),
            TextSendMessage(
                text=f'快查看以下列表挖掘小怪怪喜歡什麼吧🫵🏻'
            ),
            TemplateSendMessage(
                alt_text='ImageCarousel template',
                template=ImageCarouselTemplate(
                    columns=[
                        ImageCarouselColumn(
                            image_url='https://hackmd.io/_uploads/ByHY3GE93.png',
                            action=MessageAction(
                                label='如何投餵小怪怪',
                                text='我想學習如何上傳回收物📖'
                            ),
                        ),
                        ImageCarouselColumn(
                            image_url='https://hackmd.io/_uploads/BkoK2GNc2.png',
                            action=MessageAction(
                                label='投餵小怪怪',
                                text='我想上傳回收物📸'
                            )
                        ),
                        ImageCarouselColumn(
                            image_url='https://hackmd.io/_uploads/ryGdhGVc2.png',
                            action=MessageAction(
                                label='查看怪獸狀態',
                                text='我想關心怪獸🔦'
                            )
                        ),
                        ImageCarouselColumn(
                            image_url='https://hackmd.io/_uploads/Skwd2fVcn.png',
                            action=MessageAction(
                                label='關注永續新知',
                                text='我想關心永續新知🌏'
                            )
                        ),
                        ImageCarouselColumn(
                            image_url='https://hackmd.io/_uploads/Hy1_hMN52.png',
                            action=MessageAction(
                                label='認識我們',
                                text='我想更認識你們👋🏻'
                            )
                        ),
                    ]
                )
            ),
        ]
                
        self.LINE_BOT_API.reply_message(
            event.reply_token,
            reply_messages
        )

    def handle_unknown_image_message(self, event: MessageEvent) -> None:
        reply_messages = [
            TextSendMessage(
                text=f'小怪怪目前還不能辨識您的這則圖片訊息\n'
                     f'再嘗試投餵多投餵點食物給小怪怪吧～\n'
                     f'讓他早日學起來🤤🤤🤤'
            ),
            TextSendMessage(
                text='快查看以下列表挖掘小怪怪喜歡什麼吧🫵🏻'
            ),
            TemplateSendMessage(
                alt_text='ImageCarousel template',
                template=ImageCarouselTemplate(
                    columns=[
                        ImageCarouselColumn(
                            image_url='https://hackmd.io/_uploads/ByHY3GE93.png',
                            action=MessageAction(
                                label='如何投餵小怪怪',
                                text='我想學習如何上傳回收物📖'
                            ),
                        ),
                        ImageCarouselColumn(
                            image_url='https://hackmd.io/_uploads/BkoK2GNc2.png',
                            action=MessageAction(
                                label='投餵小怪怪',
                                text='我想上傳回收物📸'
                            )
                        ),
                        ImageCarouselColumn(
                            image_url='https://hackmd.io/_uploads/ryGdhGVc2.png',
                            action=MessageAction(
                                label='查看怪獸狀態',
                                text='我想關心怪獸🔦'
                            )
                        ),
                        ImageCarouselColumn(
                            image_url='https://hackmd.io/_uploads/Skwd2fVcn.png',
                            action=MessageAction(
                                label='關注永續新知',
                                text='我想關心永續新知🌏'
                            )
                        ),
                        ImageCarouselColumn(
                            image_url='https://hackmd.io/_uploads/Hy1_hMN52.png',
                            action=MessageAction(
                                label='認識我們',
                                text='我想更認識你們👋🏻'
                            )
                        ),
                    ]
                )
            ),
        ]
                
        self.LINE_BOT_API.reply_message(
            event.reply_token,
            reply_messages
        )

    def handle_unknown_video_message(self, event: MessageEvent) -> None:
        reply_messages = [
            TextSendMessage(
                text=f'小怪怪目前還不能辨識您的這則影音訊息\n'
                     f'再嘗試投餵多投餵點食物給小怪怪吧～\n'
                     f'讓他早日學起來🤤🤤🤤'
            ),
            TextSendMessage(
                text='快查看以下列表挖掘小怪怪喜歡什麼吧🫵🏻'
            ),
            TemplateSendMessage(
                alt_text='ImageCarousel template',
                template=ImageCarouselTemplate(
                    columns=[
                        ImageCarouselColumn(
                            image_url='https://hackmd.io/_uploads/ByHY3GE93.png',
                            action=MessageAction(
                                label='如何投餵小怪怪',
                                text='我想學習如何上傳回收物📖'
                            ),
                        ),
                        ImageCarouselColumn(
                            image_url='https://hackmd.io/_uploads/BkoK2GNc2.png',
                            action=MessageAction(
                                label='投餵小怪怪',
                                text='我想上傳回收物📸'
                            )
                        ),
                        ImageCarouselColumn(
                            image_url='https://hackmd.io/_uploads/ryGdhGVc2.png',
                            action=MessageAction(
                                label='查看怪獸狀態',
                                text='我想關心怪獸🔦'
                            )
                        ),
                        ImageCarouselColumn(
                            image_url='https://hackmd.io/_uploads/Skwd2fVcn.png',
                            action=MessageAction(
                                label='關注永續新知',
                                text='我想關心永續新知🌏'
                            )
                        ),
                        ImageCarouselColumn(
                            image_url='https://hackmd.io/_uploads/Hy1_hMN52.png',
                            action=MessageAction(
                                label='認識我們',
                                text='我想更認識你們👋🏻'
                            )
                        ),
                    ]
                )
            ),
        ]
                
        self.LINE_BOT_API.reply_message(
            event.reply_token,
            reply_messages
        )

    def handle_unknown_audio_message(self, event: MessageEvent) -> None:
        reply_messages = [
            TextSendMessage(
                text=f'小怪怪目前還不能辨識您的這則語音訊息\n'
                     f'再嘗試投餵多投餵點食物給小怪怪吧～\n'
                     f'讓他早日學起來🤤🤤🤤'
            ),
            TextSendMessage(
                text='快查看以下列表挖掘小怪怪喜歡什麼吧🫵🏻'
            ),
            TemplateSendMessage(
                alt_text='ImageCarousel template',
                template=ImageCarouselTemplate(
                    columns=[
                        ImageCarouselColumn(
                            image_url='https://hackmd.io/_uploads/ByHY3GE93.png',
                            action=MessageAction(
                                label='如何投餵小怪怪',
                                text='我想學習如何上傳回收物📖'
                            ),
                        ),
                        ImageCarouselColumn(
                            image_url='https://hackmd.io/_uploads/BkoK2GNc2.png',
                            action=MessageAction(
                                label='投餵小怪怪',
                                text='我想上傳回收物📸'
                            )
                        ),
                        ImageCarouselColumn(
                            image_url='https://hackmd.io/_uploads/ryGdhGVc2.png',
                            action=MessageAction(
                                label='查看怪獸狀態',
                                text='我想關心怪獸🔦'
                            )
                        ),
                        ImageCarouselColumn(
                            image_url='https://hackmd.io/_uploads/Skwd2fVcn.png',
                            action=MessageAction(
                                label='關注永續新知',
                                text='我想關心永續新知🌏'
                            )
                        ),
                        ImageCarouselColumn(
                            image_url='https://hackmd.io/_uploads/Hy1_hMN52.png',
                            action=MessageAction(
                                label='認識我們',
                                text='我想更認識你們👋🏻'
                            )
                        ),
                    ]
                )
            ),
        ]
                
        self.LINE_BOT_API.reply_message(
            event.reply_token,
            reply_messages
        )

config_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'config')
config_path = os.path.join(config_dir, 'linebot.conf')
line_bot_config = json.load(open(config_path, 'r', encoding='utf8'))

LINE_BOT_API = LineBotApi(line_bot_config["CHANNEL_ACCESS_TOKEN"])
HANDLER = WebhookHandler(line_bot_config["CHANNEL_SECRET"])

unknown_handler = UnknownHandler(LINE_BOT_API, HANDLER)