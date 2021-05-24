#!/usr/bin/env python
# coding=utf-8

import requests
from bs4 import BeautifulSoup
import pymysql

import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8') # Change default encoding to utf8

print('连接到mysql服务器...')
# db = pymysql.connect("localhost","root","123456","python")
db = pymysql.connect(host="localhost", user="root", password="123456", database="python",connect_timeout=3)
print('连接上了!')
cursor = db.cursor()

hdrs = {'User-Agent':'Mozilla/5.0 (X11; Fedora; Linux x86_64;Windows NT) AppleWebKit/537.36 (KHTML, like Gecko)'}


def has_class_but_no_id(tag):
    # boo = tag.has_attr('img')
    # return boo
    return tag.has_attr('class') and tag.has_attr('href') and  tag.has_attr('target')

# urls = ['http://www.zztez.com/tezgl/list_1_{}.html'.format(str(i)) for i in range(5,11)]
# urls = ['http://www.jiapai.net.cn/index.php/Judicial/index.html?p={}'.format(str(i)) for i in range(1,30)]
# urls = ['http://www.jiapai.net.cn/index.php/Judicial/index?px=152&qx=153&jx=154&lx=155&mx=156&zx=157&orderlei=1&orderp2=desc&orderp3=desc&orderp4=desc&ditiex=166&jia1=&jia2=&mj1=&mj2=&p={}'.format(str(i)) for i in range(1,1000)]
# urls = ['http://www.jiapai.net.cn/index.php/State/index?px=152&qx=153&jx=154&lx=155&mx=156&zx=157&orderlei=1&orderp2=desc&orderp3=desc&orderp4=desc&ditiex=166&jia1=&jia2=&mj1=&mj2=&p={}'.format(str(i)) for i in range(1,100)]
urls = ['http://www.jiapai.net.cn/index.php/Judicialt/index?px=152&qx=153&jx=154&lx=155&mx=156&zx=157&orderlei=1&orderp2=desc&orderp3=desc&orderp4=desc&ditiex=166&jia1=&jia2=&mj1=&mj2=&p={}'.format(str(i)) for i in range(1,200)]

# urls = ['http://www.jiapai.net.cn/index.php/Judicial/index?px=152&qx=153&jx=154&lx=155&mx=156&zx=151&orderlei=1&orderp2=desc&orderp3=desc&orderp4=desc&ditiex=166&jia1=&jia2=&mj1=&mj2=&p={}'.format(str(i)) for i in range(1,10000)]

for url in urls:
    print(url)
    # r = requests.get(url, headers = hdrs)
    s = requests.session()
    r = s.request("GET", url=url, timeout=30,headers = hdrs)
    soup = BeautifulSoup(r.content.decode('utf-8', 'ignore'), 'html')

    for link in soup.find_all(class_='sflistdiv'):
                # url="http://www.jiapai.net.cn" + link.get('href')
                # r = requests.get(url, headers = hdrs)
                # soup = BeautifulSoup(r.content.decode('utf-8', 'ignore'), 'html')

                # title=link.find("contents")
                img=link.find(class_="sflistdivn1")
                img_bf_2 =  img.find_all('img')[1]
                imgUrl = 'http://www.jiapai.net.cn' + img_bf_2.get('src')

                status =  img.find("div").find("div").text.lstrip()

                data2 = link.find(class_="sflistdivn2")

                title = data2.find(class_='f20hei')
                title = title.text

                addr = data2.find(class_='sflistban')
                addr=addr.text

                content = data2.find(class_='sflistcan')
                content = content.text

                times = data2.find(class_='sflisttime')
                times = times.text.split('：',1)[1]

                s = data2.find_all(class_='sflistcan')[1]
                addr =addr+" "+ s.text.split('：',1)[1]
                # intro=soup.select(".intro")
                # rintro=intro[0].string.encode("utf-8")
                data3 = link.find(class_="sflistdivn3")
                money = data3.find(class_='f34hong')
                money = money.text
                #查询数据
                # sql="SELECT count(*) as total FROM article WHERE title = %s"
                # data=(title)
                # print('sql:   '+sql)
                # row_affected=cursor.execute(sql,data)
                # one=cursor.fetchone()

                # if one==(0,):
                # print('title:   ' + title)
                insert = ("INSERT INTO article(imgUrl,title,addr,times,content,money,status)" "VALUES(%s,%s,%s,%s,%s,%s,%s)")
                data = (imgUrl,title,addr,times,content,money,status)
                cursor.execute(insert, data)
                db.commit()

print('爬取数据并插入mysql数据库完成...')