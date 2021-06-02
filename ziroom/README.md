# Scrapy 框架--首先安装
##  scrapy startproject 工程名 (创建Scrapy项目)

* 放置 spider 代码的目录文件 spiders（用于编写爬虫）。
* 项目中的 item 文件 items.py（用于保存所抓取的数据的容器，其存储方式类似于 Python 的字典）。
* 项目的中间件
* middlewares.py（提供一种简便的机制，通过允许插入自定义代码来拓展 Scrapy 的功能）。
* 项目的 pipelines 文件 pipelines.py（核心处理器）。 处理爬取的数据流向。重要的是process_item()方法
* 项目的设置文件 settings.py。
* 项目的配置文件 scrapy.cfg。

* POBOTSOXT_OBEY = True
    * robots.txt 是遵循 Robot 协议的一个文件，在 Scrapy 启动后，首先会访问网站的 robots.txt 文件，
    然后决定该网站的爬取范围。有时我们需要将此配置项设置为 False。在 settings.py 文件中，
    修改文件属性的方法如下。 
    * ROBOTSTXT_OBEY=False
    
* BOT_NAME  # 爬虫名

* ROBOTSTXT_OBEY = True  # 遵守robots协议

* USER_AGENT=''  # 指定爬取时使用。一定要更改user-agent，否则访问会报403错误

* CONCURRENT_REQUEST = 16  # 默认16个并行

* DOWNLOAD_DELAY = 3  # 下载延时

* COOKIES_ENABLED = False  # 缺省是启用。一般需要登录时才需要开启cookie

* DEFAULT_REQUEST_HEADERS = {}  # 默认请求头，需要时填写

* SPIDER_MIDDLEWARES  # 爬虫中间件

* DOWNLOADER_MIDDLEWARES  # 下载中间件

* 'first.middlewares.FirstDownloaderMiddleware': 543  # 543优先级越小越高

* 'firstscrapy.pipelines.FirstscrapyPipeline': 300  # item交给哪一个管道处理，300优先级越小越高

* 在弹出的快捷菜单中选择“Mark Directory as”命令→选择“Sources Root”命令，这样可以使得导入包的语法更加简洁    