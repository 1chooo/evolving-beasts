# -*- coding: utf-8 -*-
'''
Create Date: 2023/07/07
Author: @1chooo(Hugo ChunHo Lin)
Version: v0.0.1
'''

import os
import datetime
import json
import flask
import linebot
import linebot.models.events
import linebot.exceptions
import linebot.models
import linebot.models.events
import Monster.Utils
import Monster.Drama

config_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '.', 'config')
config_path = os.path.join(config_dir, 'linebot.conf')
line_bot_config = json.load(open(config_path, 'r', encoding='utf8'))

current_date = datetime.datetime.today().strftime('%Y%m%d')

LINE_BOT_API = linebot.LineBotApi(line_bot_config["CHANNEL_ACCESS_TOKEN"])
HANDLER = linebot.WebhookHandler(line_bot_config["CHANNEL_SECRET"])
USER_LOG_PATH = "./log/" + current_date

Monster.Utils.check_dir(USER_LOG_PATH)

app = flask.Flask(__name__)

@app.route("/callback", methods=['POST'])
def callback() -> str:

    global USER_LOG_PATH

    signature = flask.request.headers['X-Line-Signature'] # get X-Line-Signature header value
    body = flask.request.get_data(as_text=True)   # get request body as text

    print(body)

    file_path = USER_LOG_PATH + '/user-event.log'   # record users' log
    
    with open(file_path, 'a') as output_file:
      output_file.write(body)
      output_file.write('\n')

    try:        # handle webhook body
        HANDLER.handle(body, signature)
    except linebot.exceptions.InvalidSignatureError:
        flask.abort(400)

    return 'OK'

@HANDLER.add(linebot.models.events.FollowEvent)
def reply_text_and_get_user_profile(event) -> None:
    
    global USER_LOG_PATH
    
    try:
        user_profile = LINE_BOT_API.get_profile(event.source.user_id)
    except linebot.exceptions.LineBotApiError as e: # Handling the fails when obtaining the user profile
        print(f"LineBotApiError: {e}")
        return
    
    file_path = USER_LOG_PATH + '/users-info.txt'   # Store User INFO
    
    with open(file_path, "a") as myfile:
        try:
            print(json.dumps(vars(user_profile)))
            myfile.write(json.dumps(vars(user_profile),sort_keys=True))
            myfile.write('\n')
        except Exception as e:  # Handling the fails when writing a file
            print(f"Error: {e}")
            return
        
@HANDLER.add(linebot.models.events.MessageEvent, message=linebot.models.TextMessage)
def handle_text_message(event) -> None:

    try:
        if (event.message.text) == 'Hi Test':
            Monster.Drama.handle_test_text_message(event)
        else:
            Monster.Drama.handle_unknown_text_message(event)

    except Exception as e:
        print(f"Error occurred: {e}")
        Monster.Drama.handle_invalid_text_message(event)

def start_flask() -> None:
    app.run(port=5002)

def main() -> None:
    start_flask()

if __name__ == '__main__':
    main()