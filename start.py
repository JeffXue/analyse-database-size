# -*- coding:utf-8 -*-
import datetime

from util.mysqlHelper import MysqlHelper
from config import config
from report import generate_report

db = MysqlHelper(config.db_ip, config.db_user, config.db_password, config.database, config.db_port)


class Model:

    def __init__(self, table, amount, range_count, range_percentile, sql, total_dbid):
        self.table = table
        self.amount = amount
        self.range_count = range_count
        self.range_percentile = range_percentile
        self.sql = sql
        self.total_dbid = total_dbid


def analyse_db():
    analyse_results = []
    for table in config.tables:
        sql = config.sql % (config.database, table)
        print datetime.datetime.now(), ' Start Query DB: ' + sql
        results = db.query(sql)

        print datetime.datetime.now(), ' Start Analyse'
        total_dbid = float(len(results))
        amount = 0
        count = []
        for item in results:
            count.append(int(item[0]))
        range_count = {'r1': 0, 'r2': 0, 'r3': 0, 'r4': 0, 'r5': 0, 'r6': 0, 'r7': 0, 'r8': 0, 'r9': 0, 'r10': 0}
        for item in count:
            amount += item
            if item <= 1000:
                range_count['r1'] += 1
            elif 1000 < item <= 5000:
                range_count['r2'] += 1
            elif 5000 < item <= 10000:
                range_count['r3'] += 1
            elif 10000 < item <= 50000:
                range_count['r4'] += 1
            elif 50000 < item <= 100000:
                range_count['r5'] += 1
            elif 100000 < item <= 500000:
                range_count['r6'] += 1
            elif 500000 < item <= 1000000:
                range_count['r7'] += 1
            elif 1000000 < item <= 5000000:
                range_count['r8'] += 1
            elif 5000000 < item <= 10000000:
                range_count['r9'] += 1
            else:
                range_count['r10'] += 1

        range_percentile = {'r1p': 0, 'r2p': 0, 'r3p': 0, 'r4p': 0, 'r5p': 0, 'r6p': 0,
                            'r7p': 0, 'r8p': 0, 'r9p': 0, 'r10p': 0, 'r11p': 0}
        if range_count['r1']:
            range_percentile['r1p'] = '%0.3f' % float(range_count['r1']*100/total_dbid)
        if range_count['r2']:
            range_percentile['r2p'] = '%0.3f' % float(range_count['r2']*100/total_dbid)
        if range_count['r3']:
            range_percentile['r3p'] = '%0.3f' % float(range_count['r3']*100/total_dbid)
        if range_count['r4']:
            range_percentile['r4p'] = '%0.3f' % float(range_count['r4']*100/total_dbid)
        if range_count['r5']:
            range_percentile['r5p'] = '%0.3f' % float(range_count['r5']*100/total_dbid)
        if range_count['r6']:
            range_percentile['r6p'] = '%0.3f' % float(range_count['r6']*100/total_dbid)
        if range_count['r7']:
            range_percentile['r7p'] = '%0.3f' % float(range_count['r7']*100/total_dbid)
        if range_count['r8']:
            range_percentile['r8p'] = '%0.3f' % float(range_count['r8']*100/total_dbid)
        if range_count['r9']:
            range_percentile['r9p'] = '%0.3f' % float(range_count['r9']*100/total_dbid)
        if range_count['r10']:
            range_percentile['r10p'] = '%0.3f' % float(range_count['r10']*100/total_dbid)
        analyse_results.append(Model(table, amount, range_count, range_percentile, sql, total_dbid))
        print datetime.datetime.now(), ' End'

    return analyse_results


if __name__ == '__main__':
    generate_report(analyse_db())
    db.close()
