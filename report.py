# -*- coding:utf-8 -*-
import datetime
from jinja2 import Environment, FileSystemLoader

env = Environment(loader=FileSystemLoader('./templates'))
report_template = env.get_template('report.html')


def generate_report(datas):
    report_name = 'database_size_' + datetime.datetime.strftime(datetime.datetime.now(), '%Y%m%d_%H%M%S') + '.html'
    html = report_template.render(datas=datas)

    with open('result/'+report_name, 'w') as f:
        f.write(html.encode('utf-8'))
