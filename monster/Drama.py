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



class UploadDrama:
    
    def __init__(self, line_bot_api: LineBotApi, handler: WebhookHandler):
        self.LINE_BOT_API = line_bot_api
        self.HANDLER = handler

    def handle_upload_test(self, event: MessageEvent) -> None:
        reply_messages = [
            TextSendMessage(text='看來你想上傳回收物呢！'),
            TextSendMessage(text='再給我們一段時間，我們即將譜出專屬於我們的樂章🎶'),
            TextSendMessage(text='近請期待～'),
            ImageSendMessage(
                original_content_url = "https://hackmd.io/_uploads/BkoK2GNc2.png",
                preview_image_url = "https://hackmd.io/_uploads/BkoK2GNc2.png",
            ),
        ]
                
        self.LINE_BOT_API.reply_message(
            event.reply_token,
            reply_messages
        )
    
    def handle_upload_welcome_message(self, event: MessageEvent) -> None:
        reply_messages = [
            TextSendMessage(text='歡迎投餵小怪怪'),
            TextSendMessage(text='在上傳之前，想先問您是否知道小怪怪的喜好了呢！'),
            ImageSendMessage(
                original_content_url = "https://hackmd.io/_uploads/BkoK2GNc2.png",
                preview_image_url = "https://hackmd.io/_uploads/BkoK2GNc2.png",
            ),
            TemplateSendMessage(
                alt_text='ConfirmTemplate',
                template=ConfirmTemplate(
                        text='了解小怪怪的喜好了嗎？',
                        actions=[
                            MessageAction(
                                label='我最了解小怪怪了',
                                text='我最了解小怪怪了，我想要直接上傳'
                            ),
                            MessageAction(
                                label='沒聽說小怪怪的洗好',
                                text='我還不太認識小怪怪，我想先了解小怪怪的喜好'
                            )
                        ]
                    )
            ),
        ]
                
        self.LINE_BOT_API.reply_message(
            event.reply_token,
            reply_messages
        )

class CheckMonsterDrama:
    
    def __init__(self, line_bot_api: LineBotApi, handler: WebhookHandler):
        self.LINE_BOT_API = line_bot_api
        self.HANDLER = handler

    def handle_check_monster_test(self, event: MessageEvent) -> None:
        reply_messages = [
            TextSendMessage(text='看來你想查看怪獸狀態呢！'),
            TextSendMessage(text='再給我們一段時間，我們即將譜出專屬於我們的樂章🎶'),
            TextSendMessage(text='近請期待～'),
            ImageSendMessage(
                original_content_url = "https://hackmd.io/_uploads/ryGdhGVc2.png",
                preview_image_url = "https://hackmd.io/_uploads/ryGdhGVc2.png",
            ),
        ]
                
        self.LINE_BOT_API.reply_message(
            event.reply_token,
            reply_messages
        )
    
    def handle_check_monster_welcome_message(self, event: MessageEvent) -> None:
        reply_messages = [
            TextSendMessage(text='看來你想查看怪獸狀態呢！'),
            TextSendMessage(text='再給我們一段時間，我們即將譜出專屬於我們的樂章🎶'),
            TextSendMessage(text='近請期待～'),
            ImageSendMessage(
                original_content_url = "https://hackmd.io/_uploads/ryGdhGVc2.png",
                preview_image_url = "https://hackmd.io/_uploads/ryGdhGVc2.png",
            ),
        ]
                
        self.LINE_BOT_API.reply_message(
            event.reply_token,
            reply_messages
        )

class CheckNewsDrama:
    
    def __init__(self, line_bot_api: LineBotApi, handler: WebhookHandler):
        self.LINE_BOT_API = line_bot_api
        self.HANDLER = handler

    def handle_check_news_test(self, event: MessageEvent) -> None:
        reply_messages = [
            TextSendMessage(text='看來你想查看永續新知呢！'),
            TextSendMessage(text='再給我們一段時間，我們即將譜出專屬於我們的樂章🎶'),
            TextSendMessage(text='近請期待～'),
            ImageSendMessage(
                original_content_url = "https://hackmd.io/_uploads/Skwd2fVcn.png",
                preview_image_url = "https://hackmd.io/_uploads/Skwd2fVcn.png",
            ),
        ]
                
        self.LINE_BOT_API.reply_message(
            event.reply_token,
            reply_messages
        )

    def handle_check_news_welcome_message(self, event: MessageEvent) -> None:
        reply_messages = [
            TextSendMessage(text='看來你想查看永續新知呢！'),
            TextSendMessage(text='再給我們一段時間，我們即將譜出專屬於我們的樂章🎶'),
            TextSendMessage(text='近請期待～'),
            ImageSendMessage(
                original_content_url = "https://hackmd.io/_uploads/Skwd2fVcn.png",
                preview_image_url = "https://hackmd.io/_uploads/Skwd2fVcn.png",
            ),
        ]
                
        self.LINE_BOT_API.reply_message(
            event.reply_token,
            reply_messages
        )

class UploadTeachingDrama:
    
    def __init__(self, line_bot_api: LineBotApi, handler: WebhookHandler):
        self.LINE_BOT_API = line_bot_api
        self.HANDLER = handler

    def handle_upload_teaching_test(self, event: MessageEvent) -> None:
        reply_messages = [
            TextSendMessage(text='看來你想查看上傳教學呢！'),
            TextSendMessage(text='再給我們一段時間，我們即將譜出專屬於我們的樂章🎶'),
            TextSendMessage(text='近請期待～'),
            ImageSendMessage(
                original_content_url = "https://hackmd.io/_uploads/ByHY3GE93.png",
                preview_image_url = "https://hackmd.io/_uploads/ByHY3GE93.png",
            ),
        ]
                
        self.LINE_BOT_API.reply_message(
            event.reply_token,
            reply_messages
        )

    def handle_upload_teaching_welcome_message(self, event: MessageEvent) -> None:
        reply_messages = [
            TextSendMessage(
                text=f"哈囉您好！歡迎使用\n"
                     f"蛤！？為甚麼你的怪獸一直變大？\n"
                     f"接下來我們將會有請小怪怪帶大家說明如何投餵怪獸回收物以讓怪獸健康成長"
            ),
            TextSendMessage(
                text=f"首先簡單介紹小怪怪喜歡的回收物種類：\n"
                     f"小怪怪因為還在成長，目前還是非常挑食（挑食是不好得行為哦～）\n"
                     f"所以目前只喜歡吃：「寶特瓶、鋁箔包以及飲料紙杯」\n"
                     f"因此為了滿足小怪怪的任性，目前請投餵這三種回收物為主"
            ),
            TemplateSendMessage(
                alt_text='ConfirmTemplate',
                template=ConfirmTemplate(
                        text='了解小怪怪的任性了嗎？',
                        actions=[
                            MessageAction(
                                label='了解了',
                                text='我已經看懂了！我想知道更多小怪怪的資訊！'
                            ),
                            MessageAction(
                                label='還想再看看',
                                text='我還不太認識小怪怪，我還想再看看'
                            )
                        ]
                    )
            ),
        ]
                
        self.LINE_BOT_API.reply_message(
            event.reply_token,
            reply_messages
        )

    def handle_upload_teaching_welcome_yes_message(self, event: MessageEvent) -> None:
        reply_messages = [
            TextSendMessage(
                text=f"相信您已經初步認識小怪怪了\n"
                     f"小怪怪還是要好心跟大家說：\n"
                     f"「我目前只喜歡吃寶特瓶、鋁箔包以及飲料紙杯，其他的我會挑食」"
            ),
            TextSendMessage(
                text=f"首先請打開您的相機，根據以下範例圖式，"
                     f"將回收物品置中按下快門",
            ),
            ImageSendMessage(
                original_content_url = "https://hackmd.io/_uploads/ByHY3GE93.png",
                preview_image_url = "https://hackmd.io/_uploads/ByHY3GE93.png",
            ),
            # TextSendMessage(),
        ]
                
        self.LINE_BOT_API.reply_message(
            event.reply_token,
            reply_messages
        )

class CheckRankDrama:
    
    def __init__(self, line_bot_api: LineBotApi, handler: WebhookHandler):
        self.LINE_BOT_API = line_bot_api
        self.HANDLER = handler

    def handle_check_rank_test(self, event: MessageEvent) -> None:
        reply_messages = [
            TextSendMessage(text='看來你想查看怪獸排行榜呢！'),
            TextSendMessage(text='再給我們一段時間，我們即將譜出專屬於我們的樂章🎶'),
            TextSendMessage(text='近請期待～'),
            ImageSendMessage(
                original_content_url = "https://hackmd.io/_uploads/H13O3fVqn.png",
                preview_image_url = "https://hackmd.io/_uploads/H13O3fVqn.png",
            ),
        ]
                
        self.LINE_BOT_API.reply_message(
            event.reply_token,
            reply_messages
        )

    def handle_check_rank_welcome_message(self, event: MessageEvent) -> None:
        reply_messages = [
            TextSendMessage(text='看來你想查看怪獸排行榜呢！'),
            TextSendMessage(text='再給我們一段時間，我們即將譜出專屬於我們的樂章🎶'),
            TextSendMessage(text='近請期待～'),
            ImageSendMessage(
                original_content_url = "https://hackmd.io/_uploads/H13O3fVqn.png",
                preview_image_url = "https://hackmd.io/_uploads/H13O3fVqn.png",
            ),
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

    def handle_about_us_welcome_message(self, event: MessageEvent) -> None:
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
                text="以下是我們的成員頭像，快接續滑動以下成員列表，並點擊成員頭像以，更進一步認識我們吧！🫵🏻"
            ),
            TemplateSendMessage(
                alt_text='ImageCarousel template',
                template=ImageCarouselTemplate(
                    columns=[
                        ImageCarouselColumn(
                            image_url='https://hackmd.io/_uploads/BkUURMVqh.jpg',
                            action=MessageAction(
                                label='開發者——林群賀',
                                text='我想更認識開發者——林群賀'
                            )
                        ),
                        ImageCarouselColumn(
                            image_url='https://hackmd.io/_uploads/HyXj8OBq3.jpg',
                            action=MessageAction(
                                label='資料前處理——周姿吟',
                                text='我想更認識——周姿吟'
                            )
                        ),
                        ImageCarouselColumn(
                            image_url='https://upload.wikimedia.org/wikipedia/en/5/59/Pok%C3%A9mon_Squirtle_art.png',
                            action=MessageAction(
                                label='最多五個字——傑尼龜',
                                text='我想更認識成員——葉霈恩'
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
                    ]
                )
            )
        ]
        
        self.LINE_BOT_API.reply_message(
            event.reply_token,
            reply_messages
        )

    def handle_about_us_ho_message(self, event: MessageEvent) -> None:
        reply_messages = [
            TextSendMessage(
                text="嗨！大家好我是林群賀，主要負責本次專案 LINE BOT 的開發者，希望大家能享受這次的服務。"
            ),
            TextSendMessage(
                text=f"若還想知道更多關於我的資訊可以前往我的個人網站\n"
                     f"可以點擊以下連結前往哦：\n"
                     f"https://sites.google.com/g.ncu.edu.tw/1chooo"
            ),
            TextSendMessage(
                text=f"快接續滑動以下成員列表，並點擊成員頭像以，更進一步認識我們吧！🫵🏻"
            ),
            TemplateSendMessage(
                alt_text='ImageCarousel template',
                template=ImageCarouselTemplate(
                    columns=[
                        ImageCarouselColumn(
                            image_url='https://hackmd.io/_uploads/BkUURMVqh.jpg',
                            action=MessageAction(
                                label='開發者——林群賀',
                                text='我想更認識開發者——林群賀'
                            )
                        ),
                        ImageCarouselColumn(
                            image_url='https://hackmd.io/_uploads/HyXj8OBq3.jpg',
                            action=MessageAction(
                                label='資料前處理——周姿吟',
                                text='我想更認識——周姿吟'
                            )
                        ),
                        ImageCarouselColumn(
                            image_url='https://upload.wikimedia.org/wikipedia/en/5/59/Pok%C3%A9mon_Squirtle_art.png',
                            action=MessageAction(
                                label='最多五個字——傑尼龜',
                                text='我想更認識成員——葉霈恩'
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
                    ]
                )
            )
        ]
        
        self.LINE_BOT_API.reply_message(
            event.reply_token,
            reply_messages
        )

    def handle_about_us_chou_message(self, event: MessageEvent) -> None:
        reply_messages = [
            TextSendMessage(
                text=f"嗨！大家好我是周姿吟，"
                     f"主要負責本次專案 CNN 的資料前處理。"
            ),
            TextSendMessage(
                text=f"額外資訊～抱有科學夢的怪人\n"
                     f"最大的願望是世界和平\n"
                     f"擅長出口成真 & 拖延"
            ),
            TextSendMessage(
                text=f"快接續滑動以下成員列表，並點擊成員頭像以，更進一步認識我們吧！🫵🏻"
            ),
            TemplateSendMessage(
                alt_text='ImageCarousel template',
                template=ImageCarouselTemplate(
                    columns=[
                        ImageCarouselColumn(
                            image_url='https://hackmd.io/_uploads/BkUURMVqh.jpg',
                            action=MessageAction(
                                label='開發者——林群賀',
                                text='我想更認識開發者——林群賀'
                            )
                        ),
                        ImageCarouselColumn(
                            image_url='https://hackmd.io/_uploads/HyXj8OBq3.jpg',
                            action=MessageAction(
                                label='資料前處理——周姿吟',
                                text='我想更認識——周姿吟'
                            )
                        ),
                        ImageCarouselColumn(
                            image_url='https://upload.wikimedia.org/wikipedia/en/5/59/Pok%C3%A9mon_Squirtle_art.png',
                            action=MessageAction(
                                label='最多五個字——傑尼龜',
                                text='我想更認識成員——葉霈恩'
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
                    ]
                )
            )
        ]
        
        self.LINE_BOT_API.reply_message(
            event.reply_token,
            reply_messages
        )
    def handle_about_us_yeh_message(self, event: MessageEvent) -> None:
        reply_messages = [
            TextSendMessage(
                text="嗨！大家好我是葉霈恩，主要負責xxx"
            ),
            TextSendMessage(
                text=f"Hi"
            ),
            TextSendMessage(
                text=f"快接續滑動以下成員列表，並點擊成員頭像以，更進一步認識我們吧！🫵🏻"
            ),
            TemplateSendMessage(
                alt_text='ImageCarousel template',
                template=ImageCarouselTemplate(
                    columns=[
                        ImageCarouselColumn(
                            image_url='https://hackmd.io/_uploads/BkUURMVqh.jpg',
                            action=MessageAction(
                                label='開發者——林群賀',
                                text='我想更認識開發者——林群賀'
                            )
                        ),
                        ImageCarouselColumn(
                            image_url='https://hackmd.io/_uploads/HyXj8OBq3.jpg',
                            action=MessageAction(
                                label='資料前處理——周姿吟',
                                text='我想更認識——周姿吟'
                            )
                        ),
                        ImageCarouselColumn(
                            image_url='https://upload.wikimedia.org/wikipedia/en/5/59/Pok%C3%A9mon_Squirtle_art.png',
                            action=MessageAction(
                                label='最多五個字——傑尼龜',
                                text='我想更認識成員——葉霈恩'
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
                    ]
                )
            )
        ]
        
        self.LINE_BOT_API.reply_message(
            event.reply_token,
            reply_messages
        )
    def handle_about_us_huang_message(self, event: MessageEvent) -> None:
        reply_messages = [
            TextSendMessage(
                text="嗨！大家好我是黃品誠，主要負責xxx"
            ),
            TextSendMessage(
                text=f"Hi"
            ),
            TextSendMessage(
                text=f"快接續滑動以下成員列表，並點擊成員頭像以，更進一步認識我們吧！🫵🏻"
            ),
            TemplateSendMessage(
                alt_text='ImageCarousel template',
                template=ImageCarouselTemplate(
                    columns=[
                        ImageCarouselColumn(
                            image_url='https://hackmd.io/_uploads/BkUURMVqh.jpg',
                            action=MessageAction(
                                label='開發者——林群賀',
                                text='我想更認識開發者——林群賀'
                            )
                        ),
                        ImageCarouselColumn(
                            image_url='https://hackmd.io/_uploads/HyXj8OBq3.jpg',
                            action=MessageAction(
                                label='資料前處理——周姿吟',
                                text='我想更認識——周姿吟'
                            )
                        ),
                        ImageCarouselColumn(
                            image_url='https://upload.wikimedia.org/wikipedia/en/5/59/Pok%C3%A9mon_Squirtle_art.png',
                            action=MessageAction(
                                label='最多五個字——傑尼龜',
                                text='我想更認識成員——葉霈恩'
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
                    ]
                )
            )
        ]
        
        self.LINE_BOT_API.reply_message(
            event.reply_token,
            reply_messages
        )
    def handle_about_us_aaron_message(self, event: MessageEvent) -> None:
        reply_messages = [
            TextSendMessage(
                text="嗨！大家好我是林源煜，主要負責xxx"
            ),
            TextSendMessage(
                text=f"Hi"
            ),
            TextSendMessage(
                text=f"快接續滑動以下成員列表，並點擊成員頭像以，更進一步認識我們吧！🫵🏻"
            ),
            TemplateSendMessage(
                alt_text='ImageCarousel template',
                template=ImageCarouselTemplate(
                    columns=[
                        ImageCarouselColumn(
                            image_url='https://hackmd.io/_uploads/BkUURMVqh.jpg',
                            action=MessageAction(
                                label='開發者——林群賀',
                                text='我想更認識開發者——林群賀'
                            )
                        ),
                        ImageCarouselColumn(
                            image_url='https://hackmd.io/_uploads/HyXj8OBq3.jpg',
                            action=MessageAction(
                                label='資料前處理——周姿吟',
                                text='我想更認識——周姿吟'
                            )
                        ),
                        ImageCarouselColumn(
                            image_url='https://upload.wikimedia.org/wikipedia/en/5/59/Pok%C3%A9mon_Squirtle_art.png',
                            action=MessageAction(
                                label='最多五個字——傑尼龜',
                                text='我想更認識成員——葉霈恩'
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
                    ]
                )
            )
        ]
        
        self.LINE_BOT_API.reply_message(
            event.reply_token,
            reply_messages
        )

'''
'''

config_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'config')
config_path = os.path.join(config_dir, 'linebot.conf')
line_bot_config = json.load(open(config_path, 'r', encoding='utf8'))

LINE_BOT_API = LineBotApi(line_bot_config["CHANNEL_ACCESS_TOKEN"])
HANDLER = WebhookHandler(line_bot_config["CHANNEL_SECRET"])

upload_drama = UploadDrama(LINE_BOT_API, HANDLER)
check_monster_drama = CheckMonsterDrama(LINE_BOT_API, HANDLER)
check_news_drama = CheckNewsDrama(LINE_BOT_API, HANDLER)
upload_teaching_drama = UploadTeachingDrama(LINE_BOT_API, HANDLER)
check_rank_drama = CheckRankDrama(LINE_BOT_API, HANDLER)
about_us_drama = AboutUsDrama(LINE_BOT_API, HANDLER)

test_handler = TestHandler(LINE_BOT_API, HANDLER)
error_handler = ErrorHandler(LINE_BOT_API, HANDLER)

text_message_handlers = {
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

