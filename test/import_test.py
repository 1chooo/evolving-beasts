# -*- coding: utf-8 -*-

import os
from numpy import NaN
import json
import pandas as pd
import datetime
import tornado.web
import tornado.ioloop
import asyncio
import threading
import config
import pytz

""" Import the package concerning flask """
from flask import (
    Flask, Request, 
    abort, jsonify, 
    render_template, url_for,
    send_from_directory, redirect,
    Config, Response,
    request
)
from werkzeug.utils import secure_filename

""" Below is the package with Line Bot """

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError, LineBotApiError
)
# Import the message type of the line bot
from linebot.models import (
    ImagemapSendMessage, TextSendMessage,
    ImageSendMessage, LocationSendMessage,
    FlexSendMessage, VideoSendMessage,
    StickerSendMessage, AudioSendMessage,
    ImageMessage, VideoMessage,
    AudioMessage, TextMessage,
    TemplateSendMessage, QuickReply
)

# Import the action type of the line bot
from linebot.models import (
    MessageTemplateAction, PostbackAction,
    MessageAction, URIAction, 
    QuickReplyButton, LocationAction,
    DatetimePickerAction, RichMenuSwitchAction
)
from linebot.models.template import (
    ButtonsTemplate, CarouselTemplate,
    ConfirmTemplate, ImageCarouselTemplate
)
from linebot.models.template import *
from linebot.models.events import (
    FollowEvent, MessageEvent
)
import linebot
import Monster

line_bot_config = json.load(open("../config/linebot.conf", "r", encoding="utf8"))
line_bot_api = LineBotApi(line_bot_config["access_token"])
handler = WebhookHandler(line_bot_config["channel_secret"])

LINE_BOT_API = linebot.LineBotApi(Monster.config.CHANNEL_ACCESS_TOKEN)
HANDLER = linebot.WebhookHandler(Monster.config.CHANNEL_SECRET)