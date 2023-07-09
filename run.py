# -*- coding: utf-8 -*-
'''
Create Date: 2023/07/07
Author: @1chooo(Hugo ChunHo Lin)
Version: v0.0.1
'''

import os
import json
from Monster import Utils
from Monster import Drama
from datetime import datetime
from flask import Flask
from flask import request
from flask import abort
from linebot import LineBotApi
from linebot import WebhookHandler
from linebot.exceptions import LineBotApiError
from linebot.exceptions import InvalidSignatureError
from linebot.models import TextMessage
from linebot.models import ImageMessage
from linebot.models import AudioMessage
from linebot.models import TextSendMessage
from linebot.models.events import FollowEvent
from linebot.models.events import MessageEvent
from linebot.v3.messaging import MessagingApiBlob

config_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '.', 'config')
config_path = os.path.join(config_dir, 'linebot.conf')
line_bot_config = json.load(open(config_path, 'r', encoding='utf8'))

current_date = datetime.today().strftime('%Y%m%d')

LINE_BOT_API = LineBotApi(line_bot_config['CHANNEL_ACCESS_TOKEN'])
HANDLER = WebhookHandler(line_bot_config['CHANNEL_SECRET'])
USER_LOG_PATH = os.path.join(".", "log", current_date)

Utils.check_dir(USER_LOG_PATH)

app = Flask(__name__)

@app.route('/callback', methods=['POST'])
def callback() -> str:

    global USER_LOG_PATH

    signature = request.headers['X-Line-Signature'] # get X-Line-Signature header value
    body = request.get_data(as_text=True)   # get request body as text

    file_path = USER_LOG_PATH + '/user-event.log'   # record users' log
    
    with open(file_path, 'a') as output_file:
        output_file.write(body)
        output_file.write('\n')

    try:        # handle webhook body
        HANDLER.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'

@HANDLER.add(FollowEvent)
def handle_user_profile(event) -> None:
    
    global USER_LOG_PATH
    
    try:
        user_profile = LINE_BOT_API.get_profile(event.source.user_id)
    except LineBotApiError as e: # Handling the fails when obtaining the user profile
        print(f'LineBotApiError: {e}')
        return
    
    file_path = USER_LOG_PATH + '/users-info.log'   # Store User INFO

    with open(file_path, 'a') as myfile:
        try:
            print(json.dumps(vars(user_profile)))
            myfile.write(json.dumps(vars(user_profile), sort_keys=True))
            myfile.write('\n')
        except Exception as e:  # Handling the fails when writing a file
            print(f'Error: {e}')
            return
        
@HANDLER.add(MessageEvent, message=TextMessage)
def handle_text_message(event) -> None:

    try:
        if (event.message.text) == 'Hi Test':
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
            
            LINE_BOT_API.reply_message(
                event.reply_token,
                reply_message
            )
        else:
            reply_message = []

            message1 = TextSendMessage(
                text='這句話我們還不認識，或許有一天我們會學起來！')
            reply_message.append(message1)

            LINE_BOT_API.reply_message(
                event.reply_token,
                reply_message
            )

    except Exception as e:
        print(f'Error occurred: {e}')
        LINE_BOT_API.reply_message(
            event.reply_token, 
            TextSendMessage('''
                我們目前還不能辨識您的這則訊息\n或許可以試試看別的內容哦～''')
        )

@HANDLER.add(MessageEvent, message=ImageMessage)
def handle_image_message(event):

    global USER_LOG_PATH

    LINE_BOT_API.reply_message(
        event.reply_token,
        TextSendMessage(
            text='Image has been Uploaded ' +
            event.message.id +
            '\non ' +
            str(datetime.now().strftime('%Y/%m/%d %H:%M:%S'))
        )
    )

    try:    # Download the image
        message_content = LINE_BOT_API.get_message_content(event.message.id)


        file_path = os.path.join(USER_LOG_PATH, "imgs")
        Utils.check_dir(file_path)

        output_path = Utils.get_output_path(file_path, current_date, event.message.id, ".mp4")

        with open(output_path, "wb") as fd:
            for chunk in message_content.iter_content():
                fd.write(chunk)

    except LineBotApiError as e:
        print('Unable to get message content: ' + str(e))

@HANDLER.add(MessageEvent, message=AudioMessage)
def handle_audio_message(event):

    global USER_LOG_PATH
    LINE_BOT_API.reply_message(
        event.reply_token,
        TextSendMessage(
            text='Audio has been Uploaded ' +
            event.message.id +
            '\non ' +
            str(datetime.now().strftime('%Y/%m/%d %H:%M:%S'))
        )
    )

    try:    # Download the audio
        message_content = LINE_BOT_API.get_message_content(event.message.id)

        file_path = os.path.join(USER_LOG_PATH, "audio")
        print(file_path)
        Utils.check_dir(file_path)

        output_path = Utils.get_output_path(file_path, current_date, event.message.id, ".MP4")

        with open(output_path, "wb") as fd:
            for chunk in message_content.iter_content():
                fd.write(chunk)

    except LineBotApiError as e:
        print('Unable to get message content: ' + str(e))

def start_flask() -> None:
    app.run(port=5002)

def main() -> None:
    start_flask()

if __name__ == '__main__':
    main()