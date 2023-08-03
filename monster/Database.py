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
    def __init__(self,) -> None:
        return
    
    def getUserName(item, hasUserId = False):
        db, cursor = DatabaseSetting.initDataBase()
        if hasUserId:
            sql = "SELECT id FROM stores WHERE user_id = '%s'" % (item)
        else:
            sql = "SELECT id FROM stores WHERE name = '%s'" % (item)
        cursor.execute(sql)
        results = cursor.fetchmany(1)
        db.close()
        if results:
            return results[0][0]
        else:
            raise ValueError("查無此商店")