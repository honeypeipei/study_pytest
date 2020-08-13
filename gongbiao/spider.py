# @File  : spider.py
# @Author: leipei
# @Date  :  2020/08/11


import bs4  #网页解析，获取数据
import re   #正则表达式，进行文字匹配
import urllib.request, urllib.error    #指定URL，获取网页数据
import sqlite3    #进行SQLite数据库操作
from bs4 import BeautifulSoup


def main():
    # baseurl = "http://www.csres.com/detail/286829.html"
    # datalist = getData(baseurl)
    savepath = ".\\gongBiaoData.xls"

    # saveData(savepath)

    askURL("http://www.csres.com/detail/286829.html")


#爬取网页
def getData(baseurl):
    datalist = []
    # 2.逐一解析数据
    return datalist

#得到指定URL的网页内容
def askURL(url):
    #用户代理，告诉服务器，我们是什么类型的机器，浏览器（本质是告诉服务器，我们可以接收什么水平的文件内容）
    #模拟服务器头部信息，向服务器发送信息
    head = {
        "User-Agent" : "Mozilla / 5.0(Windows NT 10.0;Win64;x64) AppleWebKit / 537.36(KHTML, like Gecko) Chrome / 78.0.390s4.70 Safari / 537.36"
    }

    request = urllib.request.Request(url,headers = head)
    html = ""
    try:
        response = urllib.request.urlopen(request)
        html = response.read().decode("gbk" , "ignore")
        # print(html)
    except urllib.error.URLError as e:
        if hasattr(e , "code"):
            print(e.code)
        if hasattr(e, "reason"):
            print(e.reason)




#保存数据
# def saveData(savepath):
#     pass
if __name__ == "__main__":
    #调用函数
    main()