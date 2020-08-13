# @File  : testUrllib.py
# @Author: leipei
# @Date  :  2020/08/11

import urllib.request
import urllib.parse
import urllib.error


#获取一个get请求
# res =urllib.request.urlopen('http://www.csres.com')
#
# #decode()方法的第二个参数errors为严格（strict）
# print(res.read().decode('gbk','ignore'))

#获取一个post请求

# data = bytes(urllib.parse.urlencode({
#     "hello":"world"
# }), encoding="utf-8")
# res = urllib.request.urlopen("http://httpbin.org/post",data = data)
# print(res.read().decode('utf-8', 'ignore'))


# try:
#     res = urllib.request.urlopen("http://httpbin.org/get", timeout = 0.01)
#     print(res.read().decode('utf-8', 'ignore'))
# except urllib.error.URLError as e:
#     print("time out!")

# res = urllib.request.urlopen("http://www.csres.com/")
# print(res.status)

url = "http://www.csres.com/get"

headers = {
"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36"
}

data = bytes(urllib.parse.urlencode({"keywords" : "QB/T 1584-2018",
                                     "pageNum" : 1}), encoding = "utf-8")

req = urllib.request.Request(url = url, data = data, headers= headers , method = "GET")
response = urllib.request.urlopen(req)
print(response.read().decode('utf-8', 'ignore'))