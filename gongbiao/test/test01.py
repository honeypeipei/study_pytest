# @File  : test01.py
# @Author: leipei
# @Date  :  2020/08/12

import urllib.request, urllib.error    #指定URL，获取网页数据
import re
from bs4 import BeautifulSoup

myinput = input()

#找到空格用+号替换
keyword = re.sub(" ", "+", myinput)

def main():

    url = "http://www.csres.com/s.jsp?keyword="+ keyword + '&pageNum=1'
    # print(url)

    html = askURL(url)

    bs = BeautifulSoup(html, "html.parser")
    # print(bs)

    t_list = bs.select("tr[bgcolor='#FFFFFF']")

    key = []
    val = []

    # for item in t_list:
    #     # print(item['title'])
    #     item1 = item['title']
    #     res = re.split('\n', item1)
    #
    #     for i in res:
    #         # print(res[i])
    #         res1 = re.split('\uFF1A', i)
    #         # newVal = re.sub(' ','',res1[1])
    #         key.append(res1[0])
    #         val.append(res1[1].rstrip())
    #
    #     myres = dict(zip(key, val))
    #     if myres['编号'] == myinput:
    #         print(myres)
    #     else:
    #         print("error!!!!!")

    for item in t_list:
        item1 = item['title']
        res = re.split('\n', item1)

        for i in res:
            # print(res[i])
            res1 = re.split('\uFF1A', i)
            # newVal = re.sub(' ','',res1[1])
            key.append(res1[0])
            val.append(res1[1].rstrip())

        # myres = dict(zip(key, val))
        # if myres['编号'] == myinput:
        #     print(myres)
        # else:
        #     print("error!!!!!")
        if val[0] == myinput:
            print('标准号为：',val[0])
            print('标准名为：',val[1])
            print('替代情况：', val[6])
            print('发布日期： ', val[8])
            print('实施日期： ', val[9])
        else:
            print('error!!!!')

#爬取网页
def getData(baseurl):
    datalist = []
    # 2.逐一解析数据
    return datalist

# 得到指定URL的网页内容
def askURL(url):
    head = {
        "User-Agent" : "Mozilla / 5.0(Windows NT 10.0;Win64;x64) AppleWebKit / 537.36(KHTML, like Gecko) Chrome / 78.0.390s4.70 Safari / 537.36"
    }

    request = urllib.request.Request(url,headers = head)
    html = ""
    try:
        response = urllib.request.urlopen(request)
        html = response.read().decode("gbk" , "ignore")
        return html
    except urllib.error.URLError as e:
        if hasattr(e , "code"):
            print(e.code)
        if hasattr(e, "reason"):
            print(e.reason)

    # print(html)




if __name__ == "__main__":
    #调用函数
    main()