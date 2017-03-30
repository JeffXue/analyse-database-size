# -*- coding:utf-8 -*-
import ConfigParser


class Config:
    """get config from the ini file"""

    def __init__(self, config_file):
        all_config = ConfigParser.ConfigParser()
        with open(config_file, 'r') as cfg_file:
            all_config.readfp(cfg_file)

        self.db_ip = all_config.get('db', 'ip')
        self.db_port = int(all_config.get('db', 'port'))
        self.db_user = all_config.get('db', 'user')
        self.db_password = all_config.get('db', 'password')
        self.database = all_config.get('db', 'database')

        self.tables = all_config.get('tables', 'tables').split(',')
        self.sql = all_config.get('tables', 'sql')


config = Config('config.ini')
