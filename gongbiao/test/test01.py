# @File  : test01.py
# @Author: leipei
# @Date  :  2020/08/12

import urllib.request, urllib.error    #指定URL，获取网页数据
import re
from bs4 import BeautifulSoup
import pymysql
import traceback

myinput = input()

#找到空格用+号替换
keyword = re.sub(" ", "+", myinput)

def main():

    # 需要抓取的页面路径
    url = "http://www.csres.com/s.jsp?keyword=" + keyword + '&pageNum=1'

    # 获取页面所需数据
    stand = getData(url)

    # 将处理的数据存到数据库中
    saveDate(stand)


#爬取网页
def getData(baseurl):
    datalist = []
    # 2.逐一解析数据

    html = askURL(baseurl)

    bs = BeautifulSoup(html, "html.parser")

    # 取页面中搜到的标准列表
    t_list = bs.select("tr[bgcolor='#FFFFFF']")

    for item in t_list:
        key = []
        val = []

        # 取tr中的title，title中有每个标准的详情
        item1 = item['title']

        # 将每条数据以换行分隔
        res = re.split('\n', item1)

        for i in res:
            # print(res[i])
            res1 = re.split('\uFF1A', i)
            # newVal = re.sub(' ','',res1[1])
            key.append(res1[0])
            val.append(res1[1].rstrip())


        if val[0] == myinput:
            item_souceId = re.findall('\d+', item['onclick'])[0]
            datalist.append(item_souceId)
            for j in range(len(val)):
                if (j == 0) or (j == 1) or (j ==6) or (j == 8) or (j == 9):
                    datalist.append(val[j])

            #拿到标准状态插入到列表中
            datalist.insert(3,item.findChildren('td')[-1].get_text())
        else:
            print('error!!!!')
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


def saveDate(param):

    conn = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='test_pei', charset='utf8')
    cur = conn.cursor()
    cur.execute('SELECT access_id FROM sdm_access ORDER BY ID desc LIMIT 1')
    result1 = cur.fetchall()
    # print(result1)
    access_id = result1[0][0]
    # print(access_id)
    access_key = access_id[0:4]
    access_id = access_id[4:]
    accessID = access_key + str((int(access_id) + 1))



    sourceID = param[0]
    standardId = param[1]
    standardName = param[2]
    standardType = param[3]
    alternativeName = param[4]
    publishTime = param[5]
    implementTime =param[6]

    t = [(accessID, sourceID, standardId, standardName, standardType, alternativeName, publishTime, implementTime)]
    print(t)
    # sql1 = "INSERT INTO sdm_access (access_id,source_id,standard_id,standard_name,standard_type,alternative,publish_time,implement_time)VALUES('%s','%s','%s','%s','%s','%s','%s','%s')" %(accessID, sourceID, standardId, standardName, standardType, alternativeName, publishTime, implementTime)
    sql1 = "INSERT INTO sdm_access (access_id,source_id,standard_id,standard_name,standard_type,alternative,publish_time,implement_time)VALUES(%s,%s,%s,%s,%s,%s,%s,%s)"
    # sql1 = f"INSERT INTO sdm_access (access_id,source_id,standard_id,standard_name,standard_type,alternative,publish_time,implement_time) " \
    #     f"VALUES('{accessID}','{sourceID}','{standardId}','{standardName}','{standardType}','{alternativeName}','{publishTime}','{implementTime}')"
    # cur.executemany(sql1, t)
    try:
        cur.executemany(sql1, t)
        conn.commit()
        print('该标准已存到数据库中了')
    except Exception:
        traceback.print_exc()


    cur.close()
    conn.close()

if __name__ == "__main__":
    #调用函数
    main()