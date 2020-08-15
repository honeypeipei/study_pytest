# @File  : test01.py
# @Author: leipei
# @Date  :  2020/08/12
# encode=utf-8
import urllib.request, urllib.error    #指定URL，获取网页数据
import re
from bs4 import BeautifulSoup
import pymysql
import traceback
import time
from urllib.parse import quote
import  string



import xlrd

#读取excel文件
def excel():
    wb = xlrd.open_workbook('E:\\test01.xls')  # 打开Excel文件
    sheet = wb.sheet_by_name('Sheet1')  # 通过excel表格名称(rank)获取工作表
    dat = []  # 创建空list
    for a in range(sheet.nrows):
        # 循环读取表格内容（每次读取一行数据）
        cells = sheet.row_values(a)
        # 每行数据赋值给cells
        data = cells[0]
        # 因为表内可能存在多列数据，0代表第一列数据，1代表第二列，以此类推
        if data != '':
            mydata = data[0:data.find('-')] + data[data.find('-'):((data.find('-')) + 5)]
            dat.append(mydata.strip())
        # 把每次循环读取的数据插入到list
    # return dat
    res_dat = []
    for i in dat:
        if i not in res_dat:
            res_dat.append(i)
    return res_dat





mylist = excel()

for item in mylist:
    myinput = item

    # 找到空格用+号替换
    keyword = re.sub(" ", "+", myinput)


    def main():

        # 需要抓取的页面路径
        url = "http://www.csres.com/s.jsp?keyword=" + keyword + '&pageNum=1'

        # 获取页面所需数据
        stand = getData(url)

        # 将处理的数据存到数据库中
        saveDate(stand)


    # 爬取网页
    def getData(baseurl):
        datalist = []
        # 2.逐一解析数据

        html = askURL(baseurl)

        bs = BeautifulSoup(html, "html.parser")
        t_list1 = bs.select('.crumbTrail')
        find = int(re.findall('\d', t_list1[0].get_text())[0])
        if find == 0:
            print(myinput + ' 工标网上无此标准 ')
            # 自动生成sourceId
            # sourceid = 'source_' + str(int(time.time()))
            # datalist.append(sourceid)
            # datalist.append(myinput)
            # datalist.append('')
            # datalist.append('现行')
            # datalist.append('')
            # datalist.append('')
            # datalist.append('')

        else:
            # 取页面中搜到的标准列表
            t_list = bs.select("tr[bgcolor='#FFFFFF']")

            for item in t_list:
                key = []
                val = []

                # 取tr中的title，title中有每个标准的详情
                item1 = item['title']

                # 将每条数据以换行分隔
                res = re.split('\n', item1)

                try:
                    for i in res:
                        # print(res[i])
                        res1 = re.split('\uFF1A', i)
                        # newVal = re.sub(' ','',res1[1])
                        key.append(res1[0])
                        # print(key)
                        val.append(res1[1].rstrip())
                        # print(val)

                    if val[0] == myinput:
                        print('恭喜！！工标网上有您要查找的标准')
                        item_souceId = re.findall('\d+', item['onclick'])[0]
                        datalist.append(item_souceId)
                        for j in range(len(val)):
                            if (j == 0) or (j == 1) or (j == 6) or (j == 8) or (j == 9):
                                datalist.append(val[j])

                        # 拿到标准状态插入到列表中
                        datalist.insert(3, item.findChildren('td')[-1].get_text())
                        # break
                    else:
                        print(' 这一条数据和您搜索的关键字不一致哦，跳过！！！！')
                except Exception as r:
                    print('未知错误 %s' %r )
                    print(datalist,'数据不规范，不标准')
        return datalist


    # 得到指定URL的网页内容
    def askURL(url):
        head = {
            "User-Agent": "Mozilla / 5.0(Windows NT 10.0;Win64;x64) AppleWebKit / 537.36(KHTML, like Gecko) Chrome / 78.0.390s4.70 Safari / 537.36"
        }

        s = quote(url, safe=string.printable)
        # response = request.urlopen(s)

        request = urllib.request.Request(s, headers=head)
        html = ""
        try:
            response = urllib.request.urlopen(request)
            # response = request.urlopen(s)
            html = response.read().decode("gbk", "ignore")
            return html
        except urllib.error.URLError as e:
            if hasattr(e, "code"):
                print(e.code)
            if hasattr(e, "reason"):
                print(e.reason)


    def saveDate(param):

        conn = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='test_pei', charset='utf8')
        cur = conn.cursor()

        accessID = 'access_' + str(int(time.time()))

        if param == []:
            print(myinput + " 在工标网上没找到")
        else:

            sourceID = param[0]
            standardId = param[1]
            standardName = param[2]
            standardType = param[3]
            alternativeName = param[4]
            publishTime = param[5]
            implementTime = param[6]

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
                print('success!!!您需要的标准已抓取成功，可以使用了！！！')
            except Exception:
                traceback.print_exc()
                print('数据库中已有该条标准')

            cur.close()
            conn.close()


    if __name__ == "__main__":
        # 调用函数
        main()



    time.sleep(1)



