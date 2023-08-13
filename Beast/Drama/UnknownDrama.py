# -*- coding: utf-8 -*-
'''
Create Date: 2023/08/12
Author: @1chooo(Hugo ChunHo Lin)
Version: v0.0.2
'''

from linebot import LineBotApi
from linebot import WebhookHandler
from linebot.models import TextSendMessage
from linebot.models import ImageCarouselTemplate
from linebot.models import ImageCarouselColumn
from linebot.models import TemplateSendMessage
from linebot.models import MessageAction
from linebot.models import URIAction
from linebot.models.events import MessageEvent

class UnknownDrama:
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
                            action=URIAction(
                                label='關注永續新知',
                                uri='https://weather-shakespeare.github.io/2023/07/31/aluminum/'
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
                            action=URIAction(
                                label='關注永續新知',
                                uri='https://weather-shakespeare.github.io/2023/07/31/aluminum/'
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
                            action=URIAction(
                                label='關注永續新知',
                                uri='https://weather-shakespeare.github.io/2023/07/31/aluminum/'
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
                            action=URIAction(
                                label='關注永續新知',
                                uri='https://weather-shakespeare.github.io/2023/07/31/aluminum/'
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