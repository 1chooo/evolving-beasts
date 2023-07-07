# -*- coding: utf-8 -*-
'''
Create Date: 2023/07/07
Author: @1chooo(Hugo ChunHo Lin)
Version: v0.0.1
'''

import config
import datetime
import json
import flask
import linebot
import linebot.models.events
import linebot.exceptions
import linebot.models
import linebot.models.events
import monster.Utils

LINE_BOT_API = linebot.LineBotApi(config.CHANNEL_ACCESS_TOKEN)
HANDLER = linebot.WebhookHandler(config.CHANNEL_SECRET)
current_date = datetime.datetime.today().strftime('%Y%m%d')
USER_LOG_PATH = "./log/" + current_date

monster.Utils.check_dir(USER_LOG_PATH)

app = flask.Flask(__name__)

@app.route("/callback", methods=['POST'])
def callback() -> str:

    global USER_LOG_PATH

    signature = flask.request.headers['X-Line-Signature'] # get X-Line-Signature header value
    body = flask.request.get_data(as_text=True)   # get request body as text

    print(body)

    # record users' log
    file_path = USER_LOG_PATH + '/user-event.log'
    
    with open(file_path, 'a') as output_file:
      output_file.write(body)
      output_file.write('\n')

    # handle webhook body
    try:
        HANDLER.handle(body, signature)
    except linebot.exceptions.InvalidSignatureError:
        flask.abort(400)

    return 'OK'

@HANDLER.add(linebot.models.events.FollowEvent)
def reply_text_and_get_user_profile(event) -> None:
    
    global USER_LOG_PATH
    
    try:
        user_profile = LINE_BOT_API.get_profile(event.source.user_id)
    except linebot.exceptions.LineBotApiError as e: # 處理取得 user profile 失敗的情況
        print(f"LineBotApiError: {e}")
        return
    
    # 將用戶資訊存在檔案內
    file_path = USER_LOG_PATH + '/users-info.txt'
    with open(file_path, "a") as myfile:
        try:
            print(json.dumps(vars(user_profile)))
            myfile.write(json.dumps(vars(user_profile),sort_keys=True))
            myfile.write('\n')
        except Exception as e:  # 處理寫檔失敗的情況
            print(f"Error: {e}")
            return
        
@HANDLER.add(linebot.models.events.MessageEvent, message=linebot.models.TextMessage)
def handle_text_message(event) -> None:

    try:
        if (event.message.text) == 'Hi Test':

            reply_message = []
            message1 = linebot.models.TextSendMessage(
                text='HiHi! Test 1')
            reply_message.append(message1)
            message2 = linebot.models.TextSendMessage(
                text='HiHi! Test 2')
            reply_message.append(message2)
            message3 = linebot.models.TextSendMessage(
                text='HiHi! Test 3')
            reply_message.append(message3)
            
            LINE_BOT_API.reply_message(
                event.reply_token,
                reply_message
            )

    except Exception as e:
        print(f"Error occurred: {e}")
        LINE_BOT_API.reply_message(
            event.reply_token, 
            linebot.models.TextSendMessage('''我們目前還不能辨識您的這則訊息\n或許可以試試看別的內容哦～''')
        )

def start_flask() -> None:
    app.run(port=5002)

def main() -> None:
    start_flask()

if __name__ == '__main__':
    main()