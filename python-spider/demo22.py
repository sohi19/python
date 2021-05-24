#!/usr/bin/env python
# coding=utf-8

import requests
from bs4 import BeautifulSoup
import pymysql

import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8') # Change default encoding to utf8

print('连接到mysql服务器...')
db = pymysql.connect(host="localhost", user="root", password="123456", database="python")
print('连接上了!')
cursor = db.cursor()

hdrs = {'User-Agent':'Mozilla/5.0 (X11; Fedora; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko)'}


def has_class_but_no_id(tag):
    return tag.has_attr('title') and tag.has_attr('href') and not tag.has_attr('target')

urls = ['http://www.zztez.com/tezgl/list_1_{}.html'.format(str(i)) for i in range(5,11)]

for url in urls:
    print(url)
    r = requests.get(url, headers = hdrs)
    soup = BeautifulSoup(r.content.decode('gbk', 'ignore'), 'html')

    for link in soup.find_all(has_class_but_no_id):
                url="http://www.zztez.com" + link.get('href')
                r = requests.get(url, headers = hdrs)
                soup = BeautifulSoup(r.content.decode('gbk', 'ignore'), 'html')

                title=soup.find("h1")
                title=title.string.encode("utf-8")

                intro=soup.select(".intro")
                rintro=intro[0].string.encode("utf-8")

                content=soup.select(".content")
                rcontent=content[0].encode("utf-8")

                #查询数据
                sql="SELECT count(*) as total FROM article WHERE title like %s"
                data=(title)
                row_affected=cursor.execute(sql,data)
                one=cursor.fetchone()

                if one==(0,):
                    insert = ("INSERT INTO article(title,intro,content)" "VALUES(%s,%s,%s)")
                    data = (title, rintro, rcontent)
                    cursor.execute(insert, data)
                    db.commit()

print('爬取数据并插入mysql数据库完成...')