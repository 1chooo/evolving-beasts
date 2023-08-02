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
from linebot.exceptions import LineBotApiError
from linebot.models import Profile
from linebot.models.events import MessageEvent

class FileHandler:
    def __init__(self, line_bot_api: LineBotApi, current_date: str):
        self.LINE_BOT_API = line_bot_api
        self.CURRENT_DATE = current_date

    def create_directory(self, directory_path: str):
        if not os.path.isdir(directory_path):
            os.mkdir(directory_path, mode=0o777)
            print(directory_path, 'has been created successfully.')

    def generate_output_path(self, directory_path: str, id, file_type: str):
        filename = f"{self.CURRENT_DATE}_{id}{file_type}"
        output_path = os.path.join(directory_path, filename)
        
        return output_path

    def download_file(self, event: MessageEvent, type: str, file_type: str, user_log_path: str):
        message_content = self.LINE_BOT_API.get_message_content(event.message.id)
        directory_path = os.path.join(user_log_path, type)
        self.create_directory(directory_path)
        output_path = self.generate_output_path(directory_path, event.message.id, file_type)

        with open(output_path, 'wb') as fd:
            for chunk in message_content.iter_content():
                fd.write(chunk)

class ConsoleLogger:
    def __init__(self, line_bot_api: LineBotApi, handler: WebhookHandler):
        self.LINE_BOT_API = line_bot_api
        self.HANDLER = handler

    def text_exception_console(self, e: LineBotApiError) -> None:
        print(f'Error occurred: {str(e)}')

    def image_exception_console(self, e: LineBotApiError) -> None:
        print(f'Unable to get Image message content: {str(e)}')

    def video_exception_console(self, e: LineBotApiError) -> None:
        print(f'Unable to get Video message content: {str(e)}')

    def audio_exception_console(self, e: LineBotApiError) -> None:
        print(f'Unable to get Audio message content: {str(e)}')

    def line_bot_api_error_console(self, e: Exception) -> None:
        print(f'LineBotApiError: {str(e)}')

    def user_info_console(self, user_profile: Profile) -> None:
        print(json.dumps(vars(user_profile)))

    def user_info_exception_console(self, e: Exception) -> None:
        print(f'Error in getting user info: {str(e)}')

    def store_user_info(self, user_profile: Profile, user_log_path: str) -> None:
        file_path = os.path.join(user_log_path, 'users-info.log')

        with open(file_path, 'a') as myfile:
            try:
                self.user_info_console(user_profile)
                myfile.write(json.dumps(vars(user_profile), sort_keys=True))
                myfile.write('\n')
            except Exception as e:      # Handling the fails when writing a file
                self.user_info_exception_console(e)

    def user_event_exception_console(self, e: Exception) -> None:
        print(f'Error in getting user event: {str(e)}')

    def store_user_event(self, body: str, user_log_path: str) -> None:
        file_path = os.path.join(user_log_path, 'users-event.log')
        
        with open(file_path, 'a') as output_file:
            try:
                output_file.write(body)
                output_file.write('\n')
            except Exception as e:      # Handling the fails when writing a file
                self.user_event_exception_console(e)

config_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'config')
config_path = os.path.join(config_dir, 'linebot.conf')
line_bot_config = json.load(open(config_path, 'r', encoding='utf8'))

LINE_BOT_API = LineBotApi(line_bot_config["CHANNEL_ACCESS_TOKEN"])
HANDLER = WebhookHandler(line_bot_config["CHANNEL_SECRET"])

CURRENT_DATE = datetime.today().strftime('%Y%m%d')

console_logger = ConsoleLogger(LINE_BOT_API, HANDLER)
file_handler = FileHandler(LINE_BOT_API, CURRENT_DATE)