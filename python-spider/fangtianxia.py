
# -*- coding: gbk -*-
import  requests
import  bs4
import pymysql
import pymongo
def get_lastdata():
    conn = pymysql.connect(
        host="localhost",
        user="root", password="123456",
        database="python",
        charset="utf8")
    cursor = conn.cursor()
    # 连接对象
    conn = pymongo.MongoClient("localhost", 27017)
    # 库对象
    db = conn["python"]
    # 集合对象
    myset =db["houseInfo"]
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36',
    }
    urls = ['https://cd.zu.fang.com/house-a016749/c20-d22000-i3{}/?rfss=1-8b8730452120141744-3c'.format(str(i)) for i in range (1,10)]
    for url in urls:
        print(url)
        data = requests.get(url, headers=headers)
        #因为打印出来的格式有乱码，所以更改一下编码
        data.encoding="gbk"
        soup = bs4.BeautifulSoup(data.text, "html.parser")
        title = soup.find_all("p", "title")
        # for link in soup.find_all(class_="list"):
        #     # 标题
        #     title = soup.find_all("p", "title")
        #     src = link.find('img').get('src')
        # 价格
        price = soup.select("#listBox > div.houseList > dl > dd > div.moreInfo > p > span")
        # 具体的内容
        concretedata = soup.select("#listBox > div.houseList > dl > dd > p.font15.mt12.bold")
        #地址
        addr = soup.select("#listBox > div.houseList > dl > dd > p.gray6.mt12")
        #地铁
        metro = soup.select("#listBox > div.houseList > dl > dd > div > p.mt12")
        #存入mongo
        for title,price,concretedata ,addr in zip(title,price,concretedata,addr):
            last_data={
                "title":title.get_text().strip(),
                "concretedata":concretedata.get_text().strip(),
                "addr":addr.get_text().strip(),
                # "metro":metro.get_text().strip(),
                "price":price.get_text().strip()
            }
            print(last_data)
            #存入mongo
            myset.insert_one(last_data)
            #存入mysql
            # store_data(title.get_text().strip(), concretedata.get_text().strip(), addr.get_text().strip(),
            #            price.get_text().strip(),conn,cursor)

#存入mysql
def store_data(title, concretedata, addr, price, conn, cursor):
    try:
        cursor.execute(
            'insert into house_info (title,addr,concretedata,price) '
            'values ("{}","{}","{}","{}")'.format(title, addr, concretedata,price))
    except:
        print("存入数据库失败")

    conn.commit()
if __name__ == '__main__':
    get_lastdata()
