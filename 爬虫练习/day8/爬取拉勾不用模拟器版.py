import requests
import json
import datetime
import pymysql
import time
import random

# URL = 'https://www.lagou.com/jobs/positionAjax.json?city=%E5%8C%97%E4%BA%AC&needAddtionalResult=false&isSchoolJob=0'  # 北京url
URL = 'https://www.lagou.com/jobs/positionAjax.json?city=%E4%B8%8A%E6%B5%B7&needAddtionalResult=false&isSchoolJob=0' # 上海的url
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3112.113 Safari/537.36',
           "Referer": "https://www.lagou.com/jobs/list_python"}
config = {
          'host':'127.0.0.1',
          'port':3306,
          'user':'root',
          'password':'python',
          'db':'work',
          'charset':'utf8'
          }
connection = pymysql.connect(**config)

def date_insert(item):
    try:
        with connection.cursor() as cursor:
            sql = 'INSERT INTO pythonshanghai2(createTime,positionName,workYear,' \
                  'education,companyShortName,city,salary,financeStage,positionAdvantage,' \
                  'industryField,district,companyLabelList,companySize,positionLables,industryLables,firstType,' \
                  'secondType,formatCreateTime) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
            cursor.execute(sql,(item["createTime"],item["positionName"],item["workYear"],item["education"],
                                item["companyShortName"],item["city"],item["salary"],item["financeStage"],
                                item["positionAdvantage"],item["industryField"],item["district"],item["companyLabelList"],
                                item["companySize"],item["positionLables"],item["industryLables"],item["firstType"],
                                item["secondType"],item["formatCreateTime"]))
        connection.commit()
    except Exception as e:
        print(e)


def first_requset():
    post_data = {"first": "true", "pn": 1, "kd": "python"}
    r = requests.post(url=URL, headers=headers, data=post_data, )
    result = json.loads(r.content.decode())
    page_total_number = result["content"]["pageSize"]
    # print(page_total_number, type(page_total_number))
    job_lists = result["content"]["positionResult"]["result"]
    for job in job_lists:
        item = {}
        item["createTime"] = datetime.datetime.strptime(job["createTime"], '%Y-%m-%d %H:%M:%S')
        item["positionName"] = job.get("positionName", "")
        item["workYear"] = job.get("workYear", "")
        item["education"] = job.get("education", "")
        item["companyShortName"] = job.get("companyShortName", "")
        item["city"] = job.get("city", "")
        item["salary"] = job.get("salary", "")
        item["financeStage"] = job.get("financeStage", "")
        item["positionAdvantage"] = job.get("positionAdvantage", "")
        item["industryField"] = job.get("industryField", "")
        item["district"] = job.get("district", "")
        item["companyLabelList"] = str(job.get("companyLabelList", ""))
        item["companySize"] = job.get("companySize", "")
        item["positionLables"] = str(job.get("positionLables", ""))
        item["industryLables"] = str(job.get("industryLables", ""))
        item["firstType"] = job.get("firstType", "")
        item["secondType"] = job.get("secondType", "")
        item["formatCreateTime"] = job.get("formatCreateTime", "")
        date_insert(item)
    return page_total_number


def next_request(page_total_number):
    for i in range(2,int(page_total_number)+1):
        print(page_total_number,i)
        post_data = {"first": "true", "pn": i, "kd": "python"}
        time.sleep(random.randint(15, 26))
        r = requests.post(url=URL, headers=headers, data=post_data, )
        result = json.loads(r.content.decode())
        # print(page_total_number, type(page_total_number))
        try:
            job_lists = result["content"]["positionResult"]["result"]
        except:
            print(result)

        for job in job_lists:
            item = {}
            item["createTime"] = datetime.datetime.strptime(job["createTime"], '%Y-%m-%d %H:%M:%S')
            item["positionName"] = job.get("positionName", "")
            item["workYear"] = job.get("workYear", "")
            item["education"] = job.get("education", "")
            item["companyShortName"] = job.get("companyShortName", "")
            item["city"] = job.get("city", "")
            item["salary"] = job.get("salary", "")
            item["financeStage"] = job.get("financeStage", "")
            item["positionAdvantage"] = job.get("positionAdvantage", "")
            item["industryField"] = job.get("industryField", "")
            item["district"] = job.get("district", "")
            item["companyLabelList"] = str(job.get("companyLabelList", ""))
            item["companySize"] = job.get("companySize", "")
            item["positionLables"] = str(job.get("positionLables", ""))
            item["industryLables"] = str(job.get("industryLables", ""))
            item["firstType"] = job.get("firstType", "")
            item["secondType"] = job.get("secondType", "")
            item["formatCreateTime"] = job.get("formatCreateTime", "")
            date_insert(item)


if __name__ == '__main__':
    page_total_number = first_requset()
    next_request(page_total_number)
    connection.close()




