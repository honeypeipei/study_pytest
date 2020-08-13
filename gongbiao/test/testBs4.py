# @File  : testBs4.py
# @Author: leipei
# @Date  :  2020/08/12

from bs4 import BeautifulSoup
import re

file = open("./gongbiao.html", "rb")
html = file.read()

bs = BeautifulSoup(html, "html.parser")

t_list = bs.select("tr[bgcolor='#FFFFFF']")


# print(type(t_list))
# print(type(t_list[0]['title']))
# print(t_list[0]['title'])

title = ''
key = []
val = []

for item in t_list:
    # print(item['title'])
    item1 = item['title']
    res = re.split('\n', item1)

    for i in res:
        # print(res[i])
        res1 = re.split('\uFF1A', i)
        # newVal = re.sub(' ','',res1[1])
        key.append(res1[0])
        val.append(res1[1].rstrip())

    myres = dict(zip(key,val))
    if myres['编号'] == 'HJ 84-2016':
        print(myres)
    # else:
    #     print('工标网无此数据')
    # print(myres)

# myres = {}


# item1 = t_list[0]['title']



# res = re.split('\n',item1)
#
# for i in res:
#     # print(res[i])
#     res1 = re.split('\uFF1A', i)
#     key.append(res1[0])
#     val.append(res1[1])
#
#
# myres = dict(zip(key,val))
# print(myres)


# for x in item1:
#     r = re.match(r'\uFF1A', x)
#     if r:
#         # print(r.group(0))
#         key.append(title)
#         title = ''
#     else:
#         title += x
#
# print(key)

# r = re.match(r'(\n)', item1)
# print(r.group(0))


# for item in t_list:
#     text = item['title']
#     r = re.match(r'(.)\uFF1A(.)', text)
#     print(r)
#     print(item['title'])


# print(t_list)
# attr = bs.table.tr
# print(attr)
# r = re.match(r'^title=\"[\w\u4e00-\u9fa5]+\">$', t_list[0])
# print(r.group(0))


# t_list = bs.find_all(re.compile("tr"))



# def title_is_exitsts(tag):
#     return tag.has_attr('title')
#
# t_list = bs.find_all(title_is_exitsts)
#
# for item in t_list:
#     print(item)

# print(t_list)

# t_list = bs.select('h3')

# t_list = bs.find_all('h3')
# standName = t_list[0].get_text()
# print(standName)
#



#
# t_list2 = bs.find_all(text = re.compile("标准编号"))

# res = t_list.get_text()

# print(t_list2)

# print(bs.title.string)

# print(type(bs.title.string))
# # #NavigableString 标签里的内容（字符串）
# #
# # print(bs.a.attrs)


#文档的搜索
#(1)find_all()
#字符串过滤：查找与字符串完全匹配的内容
# t_list = bs.find_all("a")


#正则表达式搜索：使用search()方法匹配内容
# t_list = bs.find_all(re.compile("a"))
# print(t_list)

#方法：传入一个函数（方法），根据函数的邀请搜索
# def name_is_exits(tag):
#     return tag.has_attr("name")
#
# t_list = bs.find_all(name_is_exits)

#参数kwargs参数

#text参数
# t_list = bs.find_all( text= "")

# t_list = bs.find_all(text = re.compile("\d"))
#
# #css选择器
#
# t_list = bs.select('title')  #通过标签来查找
#
# t_list = bs.select('.mnav')  #通过类名来查找
#
# t_list = bs.select("#ul")    #通过id来查找
#
# t_list = bs.select("#a[class = 'bri']")  #通过属性来查找