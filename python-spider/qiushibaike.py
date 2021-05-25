import requests
from lxml import etree
import pymongo
# xpath爬取糗事百科的文字
class QiushSpider:
    def __init__(self):
        self.url = "https://www.qiushibaike.com/text/"
        self.headers = {"User-Agent": "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0"}
        # 连接对象
        self.conn = pymongo.MongoClient("localhost", 27017)
        # 库对象
        self.db = self.conn["python"]
        # 集合对象
        self.myset = self.db["qiushidb"]

    # 获取页面
    def getPage(self):
        res = requests.get(self.url, headers=self.headers)
        res.encoding = 'utf-8'
        html = res.text

        self.parsePage(html)

    # 解析并写入数据库
    def parsePage(self, html):
        # 创建解析对象，也是 节点对象
        parseHtml = etree.HTML(html)
        # 利用解析对象调用xpath,每个段子的对象
        baseList = parseHtml.xpath('//div[contains(@id,"qiushi_tag_")]')
        # 遍历每个段子对象，1个1个提取
        for base in baseList:
            # base: <element at ...> 节点对象
            coverUrl = 'https:'+base.xpath('./div/a/img/@src')[0]
            age = base.xpath('./div/div')[0].text
            # 用户昵称
            username = base.xpath('./div/a/h2')
            if username:
                username = username[0].text
            else:
                username = '匿名用户'

            # 段子内容
            content = base.xpath('./a/div[@class="content"]/span/text()')
            content = "".join(content).strip()
            # 好笑的数量
            laugh = base.xpath('.//i[@class="number"]')[0].text
            # 评论的数量
            comments = base.xpath('.//i[@class="number"]')[1].text

            # 存入 mongo 数据库，先定义成字典
            d = {
                "coverUrl": coverUrl.strip(),
                "age": age.strip(),
                "username": username.strip(),
                "content": content.strip(),
                "laugh": laugh.strip(),
                "comments": comments.strip()
            }
            self.myset.insert_one(d)

            # 主函数

    def workOn(self):
        print('正在爬取中...')
        self.getPage()
        print('爬取结束，存入Qiushidb库')


if __name__ == '__main__':
    spider = QiushSpider()
    urls = ['https://www.qiushibaike.com/text/page/{}/'.format(str(k)) for k in range(1, 20)]
    for url in urls:
        spider.url = url
        spider.workOn()
