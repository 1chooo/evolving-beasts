# -*- coding: utf-8 -*-
'''
Create Date: 2023/08/03
Author: @1chooo(Hugo ChunHo Lin)
Version: v0.0.1
'''

import pymysql
import os
import json

class DatabaseSetting:
    def __init__(self,) -> None:
        self.config_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'config')
        self.config_path = os.path.join(self.config_dir, 'mysql.conf')
        self.mysql_config = json.load(open(self.config_path, 'r', encoding='utf8'))

        self.database_host = self.mysql_config['database_host']
        self.database_port = self.mysql_config['database_port']
        self.database_user = self.mysql_config['database_user']
        self.database_pwd = self.mysql_config['database_pwd']
        self.database_name = self.mysql_config['database_name']
        self.database_charset = self.mysql_config['database_charset']

    def initDataBase(self,):
        db = pymysql.connect(
            host = self.database_host, 
            port = self.database_port, 
            user = self.database_user, 
            passwd = self.database_pwd,
            db = self.database_name, 
            charset = self.database_charset
        )

        cursor = db.cursor()
        return db, cursor
    

class DatabaseService:
    def __init__(self) -> None:
        self.db_setting = DatabaseSetting()

    def createUser(self, username, email, age):
        try:
            db, cursor = self.db_setting.initDataBase()

            # 在這裡插入創建用戶資料的 SQL 語句，假設有一個名為 users 的資料表
            # 假設資料表有三個欄位：username, email, age
            sql = "INSERT INTO users (username, email, age) VALUES (%s, %s, %s)"
            values = (username, email, age)

            # 執行 SQL 語句
            cursor.execute(sql, values)

            # 提交變更
            db.commit()

            # 關閉連接
            db.close()

            print("用戶資料創建成功")
        except Exception as e:
            print("用戶資料創建失敗:", e)

def main():
    db_service = DatabaseService()
    db_service.createUser("JohnDoe", "john@example.com", 30)