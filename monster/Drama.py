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

class ErrorHandler:
    def __init__(self, line_bot_api: LineBotApi, handler: WebhookHandler):
        self.LINE_BOT_API = line_bot_api
        self.HANDLER = handler

    def handle_invalid_text_message(self, event: MessageEvent) -> None:
        reply_messages = [
            TextSendMessage(
                text=f'小怪怪在您的這則文字訊息中好像發現問題🤯'
                     f'或許可以試試看別的內容哦～'
                ),
        ]
                
        self.LINE_BOT_API.reply_message(
            event.reply_token,
            reply_messages
        )
    
    def handle_invalid_image_message(self, event: MessageEvent) -> None:
        reply_messages = [
            TextSendMessage(
                text=f'小怪怪在您的這則圖片訊息中好像發現問題🤯'
                     f'或許可以試試看別的內容哦～'
                ),
        ]
                
        self.LINE_BOT_API.reply_message(
            event.reply_token,
            reply_messages
        )

    def handle_invalid_video_message(self, event: MessageEvent) -> None:
        reply_messages = [
            TextSendMessage(
                text=f'小怪怪在您的這則影音訊息中好像發現問題🤯'
                     f'或許可以試試看別的內容哦～'
                ),
        ]
                
        self.LINE_BOT_API.reply_message(
            event.reply_token,
            reply_messages
        )

    def handle_invalid_audio_message(self, event: MessageEvent) -> None:
        reply_messages = [
            TextSendMessage(
                text=f'小怪怪在您的這則語音訊息中好像發現問題🤯'
                     f'或許可以試試看別的內容哦～'
                ),
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
            TextSendMessage(
                text=f'Monster HiHi! Test 1'
            ),
            TextSendMessage(
                text=f'HiHi! Test 2'
            ),
            TextSendMessage(
                text=f'HiHi! Test 3'
            ),
        ]
                
        self.LINE_BOT_API.reply_message(
            event.reply_token,
            reply_messages
        )

class UploadDrama:
    
    def __init__(self, line_bot_api: LineBotApi, handler: WebhookHandler):
        self.LINE_BOT_API = line_bot_api
        self.HANDLER = handler
        self.ready_to_get_image = False

    def handle_upload_test(self, event: MessageEvent) -> None:
        reply_messages = [
            TextSendMessage(
                text=f'看來你想上傳回收物呢！'
            ),
            TextSendMessage(
                text=f'再給我們一段時間，我們即將譜出專屬於我們的樂章🎶'
            ),
            TextSendMessage(
                text=f'近請期待～'
            ),
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
            TextSendMessage(
                text=f'歡迎大家投餵小怪怪'
            ),
            TextSendMessage(
                text=f'在投餵之前，想先問您是否已經完成命名小怪怪的名稱呢！'
            ),
            TemplateSendMessage(
                alt_text='Buttons template',
                template=ButtonsTemplate(
                    title='小怪怪有名字了嗎？',
                    text='小怪怪想要酷酷的名字～～～',
                    actions=[
                        MessageTemplateAction(
                            label='已經給小怪怪酷酷的名字了',
                            text='我的小怪怪已經有名字了，我想直接投餵小怪怪！',
                        ),
                        MessageTemplateAction(
                            label='忘記幫小怪怪取名字了',
                            text='還沒幫小怪怪取名誒，我現在想要幫他命名',
                        ),
                    ]
                )
            ),
        ]
                
        self.LINE_BOT_API.reply_message(
            event.reply_token,
            reply_messages
        )

    def handle_upload_ready_upload_message(self, event: MessageEvent) -> None:
        self.ready_to_get_image = True

        reply_messages = [
            TextSendMessage(
                text=f'哈囉您好！在投餵小怪怪前，\n'
                     f'再次提醒小怪怪目前還小只能消化：\n'
                     f'「寶特瓶、鋁箔包🧃以及飲料紙杯🥤」'
            ),
            TextSendMessage(
                text=f'若還是不太確定小怪怪的喜好可以點擊以下圖示，'
                     f'讓小怪怪有最完整的用餐體驗🍽'
            ),
            TemplateSendMessage(
                alt_text='ImageCarousel template',
                template=ImageCarouselTemplate(
                    columns=[
                        ImageCarouselColumn(
                            image_url='https://hackmd.io/_uploads/BkrFRThs2.png',
                            action=MessageAction(
                                label='寶特瓶教學',
                                text='我想看寶特瓶上傳詳細教學！'
                            ),
                        ),
                        ImageCarouselColumn(
                            image_url='https://hackmd.io/_uploads/HkBKRa3s3.png',
                            action=MessageAction(
                                label='鋁箔包教學',
                                text='我想看鋁箔包上傳詳細教學！'
                            )
                        ),
                        ImageCarouselColumn(
                            image_url='https://hackmd.io/_uploads/ryHtCT2jn.png',
                            action=MessageAction(
                                label='飲料紙杯教學',
                                text='我想看飲料紙杯上傳詳細教學！'
                            )
                        ),
                    ]
                )
            ),
            TextSendMessage(
                text=f'放心傳送拍攝的回收物給小怪怪吧！\n'
                     f'小怪怪肚子餓餓～～'
            ),
        ]
                
        self.LINE_BOT_API.reply_message(
            event.reply_token,
            reply_messages
        )

    def handle_upload_get_image(self, event: MessageEvent) -> None:
        print('===Successfully get Image from User!!!===')
        self.ready_to_get_image = False

        recycle_type = "寶特瓶"

        reply_messages = [
            TextSendMessage(
                text=f'哈囉您好！小怪怪已經收到您的投餵！\n'
                     f'小怪怪感到非常開心！'
            ),
            TextSendMessage(
                text=f'因為小怪怪還在成長\n'
                     f'因此想向您再次確認剛剛回傳的照片是否為：\n'
                     f'👉🏻{recycle_type}'
            ),
            TemplateSendMessage(
                alt_text='Buttons template',
                template=ButtonsTemplate(
                    title=f'小怪怪想知道吃了什麼',
                    text='小怪怪剛吃飽',
                    actions=[
                        MessageTemplateAction(
                            label=f'沒錯就是{recycle_type}',
                            text=f'已經成功投餵{recycle_type}給小怪怪',
                        ),
                        MessageTemplateAction(
                            label=f'好像不是{recycle_type}欸',
                            text='小怪怪好像太餓認錯了！',
                        ),
                    ]
                )
            ),
        ]
                
        self.LINE_BOT_API.reply_message(
            event.reply_token,
            reply_messages
        )

    def handle_upload_bottle_message(self, event: MessageEvent) -> None:
        reply_messages = [
            TextSendMessage(
                text=f'感謝您投餵的寶特瓶\n'
                     f'小怪怪非常開心與你一起為地球盡一份心力\n'
            ),
            TextSendMessage(
                text=f'另外因為您的投餵\n'
                     f'「使用者的怪獸名稱」獲得了 10 分！！！'
            ),
            TemplateSendMessage(
                alt_text='Buttons template',
                template=ButtonsTemplate(
                    title='小怪怪又成長了！',
                    text='小怪怪想被了解～',
                    actions=[
                        MessageTemplateAction(
                            label='繼續投餵小怪怪',
                            text='我想上傳回收物📸',
                        ),
                        MessageTemplateAction(
                            label='關心小怪怪',
                            text='我想關心怪獸🔦',
                        ),
                    ]
                )
            ),
        ]
                
        self.LINE_BOT_API.reply_message(
            event.reply_token,
            reply_messages
        )

    def ready_to_get_image_or_not(self, ) -> bool:
        return self.ready_to_get_image

class CheckMonsterDrama:
    
    def __init__(self, line_bot_api: LineBotApi, handler: WebhookHandler):
        self.LINE_BOT_API = line_bot_api
        self.HANDLER = handler
        self.ready_to_get_monster_name = False
        self.CLIENT_MONSTER_NAME = '小怪怪'
        self.user_score = 100

    def handle_check_monster_test(self, event: MessageEvent) -> None:
        reply_messages = [
            TextSendMessage(
                text=f'看來你想查看怪獸狀態呢！'
            ),
            TextSendMessage(
                text=f'再給我們一段時間，我們即將譜出專屬於我們的樂章🎶'
            ),
            TextSendMessage(
                text=f'近請期待～'
            ),
            ImageSendMessage(
                original_content_url = "https://hackmd.io/_uploads/ryGdhGVc2.png",
                preview_image_url = "https://hackmd.io/_uploads/ryGdhGVc2.png",
            ),
        ]
                
        self.LINE_BOT_API.reply_message(
            event.reply_token,
            reply_messages
        )

    def handle_check_monster_rename_monster_test(self, event: MessageEvent) -> None:
        print('===Ready to let user rename Monster!!!===')
        
        self.CLIENT_MONSTER_NAME = event.message.text
        
        print(f'===User has renamed monster into {self.CLIENT_MONSTER_NAME}===')
        self.ready_to_get_monster_name = False

        reply_messages = [
            TextSendMessage(
                '已成功收到怪獸命名\n您的怪獸名稱是「' + self.CLIENT_MONSTER_NAME + '」！'
            ),
            TextSendMessage(
                '測試成功'
            ),
        ]

        LINE_BOT_API.reply_message(
            event.reply_token,
            reply_messages
        )
    
    def handle_check_monster_welcome_message(self, event: MessageEvent) -> None:
        reply_messages = [
            TextSendMessage(
                text=f'歡迎查看怪獸狀態！'
            ),
            TextSendMessage(
                text=f'在查看之前先幫小怪怪取個酷酷的名字吧！'
            ),
            TemplateSendMessage(
                alt_text='Buttons template',
                template=ButtonsTemplate(
                    title='小怪怪有名字了嗎？',
                    text='小怪怪想要酷酷的名字～～～',
                    actions=[
                        MessageTemplateAction(
                            label='已經給小怪怪酷酷的名字了',
                            text='我想關心我的怪獸',
                        ),
                        MessageTemplateAction(
                            label='還沒幫小怪怪取過名字誒',
                            text='還沒幫小怪怪取名誒，我現在想要幫他命名',
                        ),
                    ]
                )
            ),
        ]
                
        self.LINE_BOT_API.reply_message(
            event.reply_token,
            reply_messages
        )

    def handle_check_monster_user_check_message(self, event: MessageEvent) -> None:
        monster_name = self._get_user_monster_name()
        score = self._get_user_score()

        if score <= 100:
            monster_image_url = "https://hackmd.io/_uploads/HkLY0p3ih.png"
        elif score <= 500:
            monster_image_url = "https://hackmd.io/_uploads/BkeSKAa3in.png"
        else:
            monster_image_url = "https://hackmd.io/_uploads/SkBtR6nih.png"

        reply_messages = [
            TextSendMessage(
                text=f'嗨您好！您的怪獸名稱是：{monster_name}\n'
                     f'您目前的得分是：{score}'
            ),
            ImageSendMessage(
                original_content_url = monster_image_url,
                preview_image_url = monster_image_url,
            ),
            TextSendMessage(
                text=f'{monster_name}現在還是很餓，快快繼續投餵讓他繼續長大吧！'
            ),
            TemplateSendMessage(
                alt_text='Buttons template',
                template=ButtonsTemplate(
                    title=f'我要讓{monster_name}繼續成長！',
                    text=f'{monster_name}想要酷酷的名字～～～',
                    actions=[
                        MessageTemplateAction(
                            label='我想直接投餵！',
                            text='我想上傳回收物📸',
                        ),
                        MessageTemplateAction(
                            label='我想學習如何投餵',
                            text='我想學習如何上傳回收物📖',
                        ),
                    ]
                )
            ),
        ]
                
        self.LINE_BOT_API.reply_message(
            event.reply_token,
            reply_messages
        )

    def handle_check_monster_user_rename_monster_message(self, event: MessageEvent) -> None:
        self.ready_to_get_monster_name = True
        print('ready_to_get_monster_name:', self.ready_to_get_monster_name)
        reply_messages = [
            TextSendMessage(
                text=f'請直接輸入您想命名的名字！'
            ),
        ]
                
        self.LINE_BOT_API.reply_message(
            event.reply_token,
            reply_messages
        )

    def _get_user_score(self, ) -> int:
        return self.user_score

    def _get_user_monster_name(self, ) -> str:
        return self.CLIENT_MONSTER_NAME
    
    def ready_to_get_monster_name_or_not(self, ) -> bool:
        return self.ready_to_get_monster_name
    
    def _get_user_id(self, event: MessageEvent) -> str:
        return event.source.user_id

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
            TextSendMessage(
                text=f'看來你想查看上傳教學呢！'
            ),
            TextSendMessage(
                text=f'再給我們一段時間，我們即將譜出專屬於我們的樂章🎶'
            ),
            TextSendMessage(
                text=f'近請期待～'
            ),
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
                text=f"哈囉您好！歡迎加入我們\n"
                     f"👉🏻蛤！？為甚麼你的怪獸一直變大？\n"
                     f"接下來我們將會有請「小怪怪」帶大家說明小怪怪的喜好，以成功健康成長！"
            ),
            TextSendMessage(
                text=f"小怪怪目前還小，很多食物都不喜歡，目前還是非常挑食\n"
                     f"‼️挑食是不好的行為哦‼️"
            ),
            TextSendMessage(
                text=f"所以目前只喜歡吃：「寶特瓶、鋁箔包以及飲料紙杯」\n"
                     f"因此為了滿足小怪怪的任性，目前請投餵這三種回收物為主"
            ),
            TemplateSendMessage(
                alt_text='Buttons template',
                template=ButtonsTemplate(
                    title='了解小怪怪的任性了嗎？',
                    text='小怪怪還小有點小脾氣呢！',
                    actions=[
                        MessageTemplateAction(
                            label='還是不夠瞭解小怪怪～',
                            text='我還不太認識小怪怪，我還想再看看',
                        ),
                        MessageTemplateAction(
                            label='跟小怪怪很熟了！我想直接上傳',
                            text='我跟小怪怪已經變熟了，我想要直接上傳',
                        ),
                    ]
                )
            ),
        ]
                
        self.LINE_BOT_API.reply_message(
            event.reply_token,
            reply_messages
        )

    def handle_upload_teaching_welcome_understand_message(self, event: MessageEvent) -> None:
        reply_messages = [
            TextSendMessage(
                text=f"相信大家已經初步認識小怪怪了\n"
                     f"小怪怪還是想再好心跟大家說：\n"
                     f"「我目前只喜歡吃寶特瓶、鋁箔包以及飲料紙杯，其他的我會挑食」"
            ),
            TextSendMessage(
                text=f"大家可以點選以下圖示以查看完整上傳教學！"
            ),
            TemplateSendMessage(
                alt_text='ImageCarousel template',
                template=ImageCarouselTemplate(
                    columns=[
                        ImageCarouselColumn(
                            image_url='https://hackmd.io/_uploads/BkrFRThs2.png',
                            action=MessageAction(
                                label='寶特瓶教學',
                                text='我想看寶特瓶上傳詳細教學！'
                            ),
                        ),
                        ImageCarouselColumn(
                            image_url='https://hackmd.io/_uploads/HkBKRa3s3.png',
                            action=MessageAction(
                                label='鋁箔包教學',
                                text='我想看鋁箔包上傳詳細教學！'
                            )
                        ),
                        ImageCarouselColumn(
                            image_url='https://hackmd.io/_uploads/ryHtCT2jn.png',
                            action=MessageAction(
                                label='飲料紙杯教學',
                                text='我想看飲料紙杯上傳詳細教學！'
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
    
    def handle_upload_teaching_welcome_understand_yet_message(self, event: MessageEvent) -> None:
        reply_messages = [
            TextSendMessage(
                text=f"看來大家還想更認識小怪怪呢！\n"
                     f"那就來向各位介紹為什麼小怪怪喜歡回收物吧！"
            ),
            TextSendMessage(
                text=f"因為地球只有一個，小怪怪想要引申做則，"
                     f"帶頭引領大家做環保，因此發起了這次的活動",
            ),
            TextSendMessage(
                text=f"目前想帶大家做好「寶特瓶、鋁箔包以及飲料紙杯」的分類習慣\n"
                     f"因此現在只能投餵這些種類！"
            ),
            TemplateSendMessage(
                alt_text='Buttons template',
                template=ButtonsTemplate(
                    title='總算了解小怪怪的任性了',
                    text='小怪怪好愛地球',
                    actions=[
                        MessageTemplateAction(
                            label='已經初步認識小怪怪！',
                            text='我已經初步認識小怪怪了！我想知道更多小怪怪的資訊！',
                        ),
                        MessageTemplateAction(
                            label='我想支持小怪怪！',
                            text='我能體會小怪怪的苦心，因此我想了解更多小怪怪的資訊以支持他！！！',
                        ),
                    ]
                )
            ),
        ]
                
        self.LINE_BOT_API.reply_message(
            event.reply_token,
            reply_messages
        )

    def handle_upload_teaching_bottle_message(self, event: MessageEvent) -> None:
        reply_messages = [
            TextSendMessage(
                text=f"這是寶特瓶教學\n"
                     f"tt\n"
                     f"tt"
            ),
            TemplateSendMessage(
                alt_text='ImageCarousel template',
                template=ImageCarouselTemplate(
                    columns=[
                        ImageCarouselColumn(
                            image_url='https://hackmd.io/_uploads/HkBKRa3s3.png',
                            action=MessageAction(
                                label='鋁箔包教學',
                                text='我想看鋁箔包上傳詳細教學！'
                            )
                        ),
                        ImageCarouselColumn(
                            image_url='https://hackmd.io/_uploads/ryHtCT2jn.png',
                            action=MessageAction(
                                label='飲料紙杯教學',
                                text='我想看飲料紙杯上傳詳細教學！'
                            )
                        ),
                        ImageCarouselColumn(
                            image_url='https://hackmd.io/_uploads/BkrFRThs2.png',
                            action=MessageAction(
                                label='寶特瓶教學',
                                text='我想看寶特瓶上傳詳細教學！'
                            ),
                        ),
                    ]
                )
            ),
            TemplateSendMessage(
                alt_text='Buttons template',
                template=ButtonsTemplate(
                    title='已了解小怪怪的所有喜好？',
                    text='小怪怪餓了',
                    actions=[
                        MessageTemplateAction(
                            label='我跟小怪怪變朋友了！',
                            text='我跟小怪怪已經變熟了，我想要直接上傳',
                        ),
                        MessageTemplateAction(
                            label='還是不夠瞭解小怪怪',
                            text='我還是不夠了解小怪怪，我想再看一次',
                        ),
                    ]
                )
            ),
        ]
                
        self.LINE_BOT_API.reply_message(
            event.reply_token,
            reply_messages
        )

    def handle_upload_teaching_aluminum_message(self, event: MessageEvent) -> None:
        reply_messages = [
            TextSendMessage(
                text=f"這是鋁箔包教學\n"
                     f"tt\n"
                     f"tt"
            ),
            TemplateSendMessage(
                alt_text='ImageCarousel template',
                template=ImageCarouselTemplate(
                    columns=[
                        ImageCarouselColumn(
                            image_url='https://hackmd.io/_uploads/ryHtCT2jn.png',
                            action=MessageAction(
                                label='飲料紙杯教學',
                                text='我想看飲料紙杯上傳詳細教學！'
                            )
                        ),
                        ImageCarouselColumn(
                            image_url='https://hackmd.io/_uploads/BkrFRThs2.png',
                            action=MessageAction(
                                label='寶特瓶教學',
                                text='我想看寶特瓶上傳詳細教學！'
                            ),
                        ),
                        ImageCarouselColumn(
                            image_url='https://hackmd.io/_uploads/HkBKRa3s3.png',
                            action=MessageAction(
                                label='鋁箔包教學',
                                text='我想看鋁箔包上傳詳細教學！'
                            )
                        ),
                    ]
                )
            ),
            TemplateSendMessage(
                alt_text='Buttons template',
                template=ButtonsTemplate(
                    title='已了解小怪怪的所有喜好？',
                    text='小怪怪餓了',
                    actions=[
                        MessageTemplateAction(
                            label='我跟小怪怪變朋友了！',
                            text='我跟小怪怪已經變熟了，我想要直接上傳',
                        ),
                        MessageTemplateAction(
                            label='還是不夠瞭解小怪怪',
                            text='我還是不夠了解小怪怪，我想再看一次',
                        ),
                    ]
                )
            ),
        ]
                
        self.LINE_BOT_API.reply_message(
            event.reply_token,
            reply_messages
        )

    def handle_upload_teaching_cup_message(self, event: MessageEvent) -> None:
        reply_messages = [
            TextSendMessage(
                text=f"這是飲料紙杯教學\n"
                     f"tt\n"
                     f"tt"
            ),
            TemplateSendMessage(
                alt_text='ImageCarousel template',
                template=ImageCarouselTemplate(
                    columns=[
                        ImageCarouselColumn(
                            image_url='https://hackmd.io/_uploads/BkrFRThs2.png',
                            action=MessageAction(
                                label='寶特瓶教學',
                                text='我想看寶特瓶上傳詳細教學！'
                            ),
                        ),
                        ImageCarouselColumn(
                            image_url='https://hackmd.io/_uploads/HkBKRa3s3.png',
                            action=MessageAction(
                                label='鋁箔包教學',
                                text='我想看鋁箔包上傳詳細教學！'
                            )
                        ),
                        ImageCarouselColumn(
                            image_url='https://hackmd.io/_uploads/ryHtCT2jn.png',
                            action=MessageAction(
                                label='飲料紙杯教學',
                                text='我想看飲料紙杯上傳詳細教學！'
                            )
                        ),
                    ]
                )
            ),
            TemplateSendMessage(
                alt_text='Buttons template',
                template=ButtonsTemplate(
                    title='已了解小怪怪的所有喜好？',
                    text='小怪怪餓了',
                    actions=[
                        MessageTemplateAction(
                            label='我跟小怪怪變朋友了！',
                            text='我跟小怪怪已經變熟了，我想要直接上傳',
                        ),
                        MessageTemplateAction(
                            label='還是不夠瞭解小怪怪',
                            text='我還是不夠了解小怪怪，我想再看一次',
                        ),
                    ]
                )
            ),
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
            TextSendMessage(
                text=f'看來你想查看怪獸排行榜呢！'
            ),
            TextSendMessage(
                text=f'再給我們一段時間，我們即將譜出專屬於我們的樂章🎶'
            ),
            TextSendMessage(
                text=f'近請期待～'
            ),
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
                                text='我想更認識資料前處理——周姿吟'
                            )
                        ),
                        ImageCarouselColumn(
                            image_url='https://hackmd.io/_uploads/r1GmF2D5h.jpg',
                            action=MessageAction(
                                label='專案企劃——葉霈恩',
                                text='我想更認識專案企劃——葉霈恩'
                            )
                        ),
                        ImageCarouselColumn(
                            image_url='https://hackmd.io/_uploads/HyGbBitq2.jpg',
                            action=MessageAction(
                                label='效益分析——黃品誠',
                                text='我想更認識效益分析——黃品誠'
                            )
                        ),
                        ImageCarouselColumn(
                            image_url='https://hackmd.io/_uploads/r10b0zKc3.jpg',
                            action=MessageAction(
                                label='模型訓練——林源煜',
                                text='我想更認識模型訓練——林源煜'
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
                            image_url='https://hackmd.io/_uploads/HyXj8OBq3.jpg',
                            action=MessageAction(
                                label='資料前處理——周姿吟',
                                text='我想更認識資料前處理——周姿吟'
                            )
                        ),
                        ImageCarouselColumn(
                            image_url='https://hackmd.io/_uploads/r1GmF2D5h.jpg',
                            action=MessageAction(
                                label='專案企劃——葉霈恩',
                                text='我想更認識專案企劃——葉霈恩'
                            )
                        ),
                        ImageCarouselColumn(
                            image_url='https://hackmd.io/_uploads/HyGbBitq2.jpg',
                            action=MessageAction(
                                label='效益分析——黃品誠',
                                text='我想更認識效益分析——黃品誠'
                            )
                        ),
                        ImageCarouselColumn(
                            image_url='https://hackmd.io/_uploads/r10b0zKc3.jpg',
                            action=MessageAction(
                                label='模型訓練——林源煜',
                                text='我想更認識模型訓練——林源煜'
                            )
                        ),
                        ImageCarouselColumn(
                            image_url='https://hackmd.io/_uploads/BkUURMVqh.jpg',
                            action=MessageAction(
                                label='開發者——林群賀',
                                text='我想更認識開發者——林群賀'
                            )
                        ),
                    ]
                )
            ),
            TextSendMessage(
                text=f"想必大家看完關於我們成員的介紹後，都能更認識我們了\n"
                     f"若已經認識我們了，快快點擊下方選單功能👇🏻\n"
                     f"體驗我們提供的完整服務內容吧！"
            ),
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
                            image_url='https://hackmd.io/_uploads/r1GmF2D5h.jpg',
                            action=MessageAction(
                                label='專案企劃——葉霈恩',
                                text='我想更認識專案企劃——葉霈恩'
                            )
                        ),
                        ImageCarouselColumn(
                            image_url='https://hackmd.io/_uploads/HyGbBitq2.jpg',
                            action=MessageAction(
                                label='效益分析——黃品誠',
                                text='我想更認識效益分析——黃品誠'
                            )
                        ),
                        ImageCarouselColumn(
                            image_url='https://hackmd.io/_uploads/r10b0zKc3.jpg',
                            action=MessageAction(
                                label='模型訓練——林源煜',
                                text='我想更認識模型訓練——林源煜'
                            )
                        ),
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
                                text='我想更認識資料前處理——周姿吟'
                            )
                        ),
                    ]
                )
            ),
            TextSendMessage(
                text=f"想必大家看完關於我們成員的介紹後，都能更認識我們了\n"
                     f"若已經認識我們了，快快點擊下方選單功能👇🏻\n"
                     f"體驗我們提供的完整服務內容吧！"
            ),
        ]
        
        self.LINE_BOT_API.reply_message(
            event.reply_token,
            reply_messages
        )
    def handle_about_us_yeh_message(self, event: MessageEvent) -> None:
        reply_messages = [
            TextSendMessage(
                text="嗨！大家好我是葉霈恩，在這次專案負責專案管理的職位，還請多多指教！"
            ),
            TextSendMessage(
                text=f"喜歡嘗試各樣新奇的事物，富有創意與熱情"
            ),
            TextSendMessage(
                text=f"快接續滑動以下成員列表，並點擊成員頭像以，更進一步認識我們吧！🫵🏻"
            ),
            TemplateSendMessage(
                alt_text='ImageCarousel template',
                template=ImageCarouselTemplate(
                    columns=[
                        ImageCarouselColumn(
                            image_url='https://hackmd.io/_uploads/HyGbBitq2.jpg',
                            action=MessageAction(
                                label='效益分析——黃品誠',
                                text='我想更認識效益分析——黃品誠'
                            )
                        ),
                        ImageCarouselColumn(
                            image_url='https://hackmd.io/_uploads/r10b0zKc3.jpg',
                            action=MessageAction(
                                label='模型訓練——林源煜',
                                text='我想更認識模型訓練——林源煜'
                            )
                        ),
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
                                text='我想更認識資料前處理——周姿吟'
                            )
                        ),
                        ImageCarouselColumn(
                            image_url='https://hackmd.io/_uploads/r1GmF2D5h.jpg',
                            action=MessageAction(
                                label='專案企劃——葉霈恩',
                                text='我想更認識專案企劃——葉霈恩'
                            )
                        ),
                    ]
                )
            ),
            TextSendMessage(
                text=f"想必大家看完關於我們成員的介紹後，都能更認識我們了\n"
                     f"若已經認識我們了，快快點擊下方選單功能👇🏻\n"
                     f"體驗我們提供的完整服務內容吧！"
            ),
        ]
        
        self.LINE_BOT_API.reply_message(
            event.reply_token,
            reply_messages
        )
    def handle_about_us_huang_message(self, event: MessageEvent) -> None:
        reply_messages = [
            TextSendMessage(
                text="嗨！大家好我是黃品誠，主要負責產品效益分析"
            ),
            TextSendMessage(
                text=f"我來自物理系，熱衷於參加跨領域的專案～"
            ),
            TextSendMessage(
                text=f"快接續滑動以下成員列表，並點擊成員頭像以，更進一步認識我們吧！🫵🏻"
            ),
            TemplateSendMessage(
                alt_text='ImageCarousel template',
                template=ImageCarouselTemplate(
                    columns=[
                        ImageCarouselColumn(
                            image_url='https://hackmd.io/_uploads/r10b0zKc3.jpg',
                            action=MessageAction(
                                label='模型訓練——林源煜',
                                text='我想更認識模型訓練——林源煜'
                            )
                        ),
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
                                text='我想更認識資料前處理——周姿吟'
                            )
                        ),
                        ImageCarouselColumn(
                            image_url='https://hackmd.io/_uploads/r1GmF2D5h.jpg',
                            action=MessageAction(
                                label='專案企劃——葉霈恩',
                                text='我想更認識專案企劃——葉霈恩'
                            )
                        ),
                        ImageCarouselColumn(
                            image_url='https://hackmd.io/_uploads/HyGbBitq2.jpg',
                            action=MessageAction(
                                label='效益分析——黃品誠',
                                text='我想更認識效益分析——黃品誠'
                            )
                        ),
                    ]
                )
            ),
            TextSendMessage(
                text=f"想必大家看完關於我們成員的介紹後，都能更認識我們了\n"
                     f"若已經認識我們了，快快點擊下方選單功能👇🏻\n"
                     f"體驗我們提供的完整服務內容吧！"
            ),
        ]
        
        self.LINE_BOT_API.reply_message(
            event.reply_token,
            reply_messages
        )
    def handle_about_us_aaron_message(self, event: MessageEvent) -> None:
        reply_messages = [
            TextSendMessage(
                text="嗨！大家好我是林源煜，主要負責訓練影像分辨模型"
            ),
            TextSendMessage(
                text=f"喜歡探索有關於機器學習的新技術"
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
                                text='我想更認識資料前處理——周姿吟'
                            )
                        ),
                        ImageCarouselColumn(
                            image_url='https://hackmd.io/_uploads/r1GmF2D5h.jpg',
                            action=MessageAction(
                                label='專案企劃——葉霈恩',
                                text='我想更認識專案企劃——葉霈恩'
                            )
                        ),
                        ImageCarouselColumn(
                            image_url='https://hackmd.io/_uploads/HyGbBitq2.jpg',
                            action=MessageAction(
                                label='效益分析——黃品誠',
                                text='我想更認識效益分析——黃品誠'
                            )
                        ),
                        ImageCarouselColumn(
                            image_url='https://hackmd.io/_uploads/r10b0zKc3.jpg',
                            action=MessageAction(
                                label='模型訓練——林源煜',
                                text='我想更認識模型訓練——林源煜'
                            )
                        ),
                    ]
                )
            ),
            TextSendMessage(
                text=f"想必大家看完關於我們成員的介紹後，都能更認識我們了\n"
                     f"若已經認識我們了，快快點擊下方選單功能👇🏻\n"
                     f"體驗我們提供的完整服務內容吧！"
            ),
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

upload_drama = UploadDrama(LINE_BOT_API, HANDLER)
check_monster_drama = CheckMonsterDrama(LINE_BOT_API, HANDLER)
check_news_drama = CheckNewsDrama(LINE_BOT_API, HANDLER)
upload_teaching_drama = UploadTeachingDrama(LINE_BOT_API, HANDLER)
check_rank_drama = CheckRankDrama(LINE_BOT_API, HANDLER)
about_us_drama = AboutUsDrama(LINE_BOT_API, HANDLER)

test_handler = TestHandler(LINE_BOT_API, HANDLER)
unknown_handler = UnknownHandler(LINE_BOT_API, HANDLER)
error_handler = ErrorHandler(LINE_BOT_API, HANDLER)

text_message_handler_map = {
    # === Drama: Upload ===
    '我想上傳回收物📸': 
        upload_drama.handle_upload_welcome_message,
    '我的小怪怪已經有名字了，我想直接投餵小怪怪！': 
        upload_drama.handle_upload_ready_upload_message,
    '已經成功投餵寶特瓶給小怪怪':
        upload_drama.handle_upload_bottle_message,
    # === Drama: Check Monster ===
    '我想關心怪獸🔦': 
        check_monster_drama.handle_check_monster_welcome_message,
    '我想關心我的怪獸': 
        check_monster_drama.handle_check_monster_user_check_message,
    '還沒幫小怪怪取名誒，我現在想要幫他命名':
        check_monster_drama.handle_check_monster_user_rename_monster_message,
    # === Drama: Check News ===
    '我想關心永續新知🌏': 
        check_news_drama.handle_check_news_welcome_message,
    # === Drama: Upload Teaching ===
    '我想學習如何上傳回收物📖': 
        upload_teaching_drama.handle_upload_teaching_welcome_message,
    '我跟小怪怪已經變熟了，我想要直接上傳': 
        upload_drama.handle_upload_welcome_message,
    '我已經初步認識小怪怪了！我想知道更多小怪怪的資訊！': 
        upload_teaching_drama.handle_upload_teaching_welcome_understand_message,
    '我能體會小怪怪的苦心，因此我想了解更多小怪怪的資訊以支持他！！！': 
        upload_teaching_drama.handle_upload_teaching_welcome_understand_message,
    '我還不太認識小怪怪，我還想再看看': 
        upload_teaching_drama.handle_upload_teaching_welcome_understand_yet_message,
    '我想看飲料紙杯上傳詳細教學！': 
        upload_teaching_drama.handle_upload_teaching_cup_message,
    '我想看寶特瓶上傳詳細教學！': 
        upload_teaching_drama.handle_upload_teaching_bottle_message,
    '我想看鋁箔包上傳詳細教學！': 
        upload_teaching_drama.handle_upload_teaching_aluminum_message,
    '我還是不夠了解小怪怪，我想再看一次': 
        upload_teaching_drama.handle_upload_teaching_welcome_message,
    # === Drama: Check Rank ===
    '我想看最強怪獸👾': 
        check_rank_drama.handle_check_rank_welcome_message,
    # === Drama: About Us ===
    '我想更認識你們👋🏻': 
        about_us_drama.handle_about_us_welcome_message,
    '我想更認識開發者——林群賀': 
        about_us_drama.handle_about_us_ho_message,
    '我想更認識資料前處理——周姿吟': 
        about_us_drama.handle_about_us_chou_message,
    '我想更認識專案企劃——葉霈恩': 
        about_us_drama.handle_about_us_yeh_message,
    '我想更認識模型訓練——林源煜': 
        about_us_drama.handle_about_us_aaron_message,
    '我想更認識效益分析——黃品誠': 
        about_us_drama.handle_about_us_huang_message,
}

test_text_message_handler_map = {
    'Hi Test': 
    test_handler.handle_test_text_message,
}

upload_text_message_handler_map = {
    '我想上傳回收物📸': 
        upload_drama.handle_upload_welcome_message,
    '我的小怪怪已經有名字了，我想直接投餵小怪怪！': 
        upload_drama.handle_upload_ready_upload_message,
    '已經成功投餵寶特瓶給小怪怪':
        upload_drama.handle_upload_bottle_message,
}

check_monster_text_message_handler_map = {
    '我想關心怪獸🔦': 
        check_monster_drama.handle_check_monster_welcome_message,
}

check_rank_text_message_handler_map = {
    '我想看最強怪獸👾': 
        check_rank_drama.handle_check_rank_welcome_message,
}

check_news_text_message_handler_map = {
    '我想關心永續新知🌏': 
        check_news_drama.handle_check_news_welcome_message,
}

upload_teaching_text_message_handler_map = {
    '我想學習如何上傳回收物📖': 
        upload_teaching_drama.handle_upload_teaching_welcome_message,
    '我跟小怪怪已經變熟了，我想要直接上傳': 
        upload_drama.handle_upload_welcome_message,
    '我已經初步認識小怪怪了！我想知道更多小怪怪的資訊！': 
        upload_teaching_drama.handle_upload_teaching_welcome_understand_message,
    '我能體會小怪怪的苦心，因此我想了解更多小怪怪的資訊以支持他！！！': 
        upload_teaching_drama.handle_upload_teaching_welcome_understand_message,
    '我還不太認識小怪怪，我還想再看看': 
        upload_teaching_drama.handle_upload_teaching_welcome_understand_yet_message,
    '我想看飲料紙杯上傳詳細教學！': 
        upload_teaching_drama.handle_upload_teaching_cup_message,
    '我想看寶特瓶上傳詳細教學！': 
        upload_teaching_drama.handle_upload_teaching_bottle_message,
    '我想看鋁箔包上傳詳細教學！': 
        upload_teaching_drama.handle_upload_teaching_aluminum_message,
    '我還是不夠了解小怪怪，我想再看一次': 
        upload_teaching_drama.handle_upload_teaching_welcome_message,
}

about_us_text_message_handler_map = {
    '我想更認識你們👋🏻': 
        about_us_drama.handle_about_us_welcome_message,
    '我想更認識開發者——林群賀': 
        about_us_drama.handle_about_us_ho_message,
    '我想更認識資料前處理——周姿吟': 
        about_us_drama.handle_about_us_chou_message,
    '我想更認識專案企劃——葉霈恩': 
        about_us_drama.handle_about_us_yeh_message,
    '我想更認識模型訓練——林源煜': 
        about_us_drama.handle_about_us_aaron_message,
    '我想更認識效益分析——黃品誠': 
        about_us_drama.handle_about_us_huang_message,
}
