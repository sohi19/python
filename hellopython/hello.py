import time
import datetime
# import Scrapy

print("hello world123")


def newTime():
    s = time.time()
    print(s)
    return s


ss = newTime()
print(newTime())


# 可写函数说明
def changeme(mylist):
    "修改传入的列表"
    mylist.append([1, 2, 3, 4])
    print("函数内取值: ", mylist)
    return


# 调用changeme函数
mylist = [10, 20, 30]
changeme(mylist)
print("函数外取值: ", mylist)


def datetime():
    a = 103 % 4
    return a, 10


print(datetime())
