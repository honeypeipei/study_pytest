# @File  : testMysql.py
# @Author: leipei
# @Date  :  2020/08/12

import pymysql
import traceback

def conn_mysql():
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
    sourceID = '50602'
    standardId = 'GB/T 10265-1998'
    standardName = '烧结氧化钆-二氧化铀芯块分析方法 第3部分:波长色散X射线荧光光谱法测定氧化钆含量'
    standardType = '现行'
    alternativeName = ''
    publishTime = ''
    implementTime = ''

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
        # print("发生异常", Exception)
        # conn.close()
        # print('数据库报错了')
    # result1 = cur.fetchall()



    cur.close()
    conn.close()
    # print(result)

if __name__ == '__main__':
    conn_mysql()