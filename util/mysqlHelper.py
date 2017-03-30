# -*- coding:utf-8 -*-
import MySQLdb


class MysqlHelper:

    def __init__(self, ip, username, password, database, port):
        self.db = MySQLdb.connect(ip, username, password, database, port, charset="utf8")

    def close(self):
        self.db.close()

    def query(self, sql):
        result = []
        cursor = self.db.cursor()
        try:
            cursor.execute(sql)
            result = cursor.fetchall()
        except Exception, e:
            print e
            self.db.rollback()
        finally:
            cursor.close()
        return result

    def insert(self, sql):
        cursor = self.db.cursor()
        try:
            cursor.execute(sql)
            self.db.commit()
        except Exception, e:
            print e
            self.db.rollback()
        finally:
            cursor.close()

    def update(self, sql):
        cursor = self.db.cursor()
        try:
            cursor.execute(sql)
            self.db.commit()
        except Exception, e:
            print e
            self.db.rollback()
        finally:
            cursor.close()

