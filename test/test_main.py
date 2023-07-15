# -*- coding: utf-8 -*-
'''
Create Date: 2023/07/15
Author: @1chooo(Hugo ChunHo Lin)
Version: v0.0.1
Status: Failed
'''

import unittest
from unittest.mock import patch, MagicMock
from flask import Flask
from ..Monster import Drama, Utils
from ..run import app, handle_user_profile, handle_text_message, handle_image_message, handle_video_message, handle_audio_message

class MainTestCase(unittest.TestCase):

    def setUp(self):
        app.testing = True
        self.client = app.test_client()

    @patch('Monster.Utils.store_user_info')
    @patch('linebot.LineBotApi.get_profile')
    def test_handle_user_profile(self, mock_get_profile, mock_store_user_info):
        mock_get_profile.return_value = MagicMock(user_id='USER_ID', display_name='John Doe')
        response = self.client.post('/callback', headers={'X-Line-Signature': 'SIGNATURE'}, json={'events': [{'type': 'follow', 'source': {'user_id': 'USER_ID'}}]})
        mock_store_user_info.assert_called_once()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b'OK')

    @patch('Monster.Drama.handle_test_text_message')
    def test_handle_text_message(self, mock_handle_test_text_message):
        response = self.client.post('/callback', headers={'X-Line-Signature': 'SIGNATURE'}, json={'events': [{'type': 'message', 'message': {'type': 'text', 'text': 'Hi Test'}}]})
        mock_handle_test_text_message.assert_called_once()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b'OK')

    @patch('Monster.Drama.handle_test_image_message')
    @patch('Monster.Utils.download_file')
    def test_handle_image_message(self, mock_download_file, mock_handle_test_image_message):
        response = self.client.post('/callback', headers={'X-Line-Signature': 'SIGNATURE'}, json={'events': [{'type': 'message', 'message': {'type': 'image'}}]})
        mock_handle_test_image_message.assert_called_once()
        mock_download_file.assert_called_once()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b'OK')

    @patch('Monster.Drama.handle_test_video_message')
    @patch('Monster.Utils.download_file')
    def test_handle_video_message(self, mock_download_file, mock_handle_test_video_message):
        response = self.client.post('/callback', headers={'X-Line-Signature': 'SIGNATURE'}, json={'events': [{'type': 'message', 'message': {'type': 'video'}}]})
        mock_handle_test_video_message.assert_called_once()
        mock_download_file.assert_called_once()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b'OK')

    @patch('Monster.Drama.handle_test_audio_message')
    @patch('Monster.Utils.download_file')
    def test_handle_audio_message(self, mock_download_file, mock_handle_test_audio_message):
        response = self.client.post('/callback', headers={'X-Line-Signature': 'SIGNATURE'}, json={'events': [{'type': 'message', 'message': {'type': 'audio'}}]})
        mock_handle_test_audio_message.assert_called_once()
        mock_download_file.assert_called_once()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b'OK')

if __name__ == '__main__':
    unittest.main()
