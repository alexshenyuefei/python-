from lxml import etree
import requests
import datetime
import pymysql


"""
2017-12-05
北京新发地水果
第一页:http://www.xinfadi.com.cn/marketanalysis/2/list/1.shtml
最后一页http://www.xinfadi.com.cn/marketanalysis/2/list/2678.shtml
"""
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'}
URL = 'http://www.xinfadi.com.cn/marketanalysis/2/list/{}.shtml'

config = {
          'host':'127.0.0.1',
          'port':3306,
          'user':'root',
          'password':'python',
          'db':'xinfadi',
          'charset':'utf8'
          }
connection = pymysql.connect(**config)


def insert_into_mysql(item):
    try:
        with connection.cursor() as cursor:
            sql = 'INSERT INTO fruits(names,low_price,avg_price,high_price,guige,unit,times) VALUES (%s,%s,%s,%s,%s,%s,%s)'
            cursor.execute(sql,(item['name'], item['low_price'], item['avg_price'], item['high_price'], item['guige'],item['unit'], item['datetime']))
        connection.commit()
    except Exception as e:
        print(e)
        print(item)


def xinfadi_fruits():
    for i in range(1,2678+1):
        response = requests.get(url=URL.format(i),headers=headers)
        temp_html = etree.HTML(response.content.decode())
        father_elemet_lists= temp_html.xpath("//div[@class='hangq_left']//tr[position()>1]")
        content_list = []
        for son in father_elemet_lists:
            item = {}
            item['name']=son.xpath(r"./td[position()=1]/text()")[0] if len(son.xpath(r".//td[position()=1]/text()"))>0 else [""]
            item['low_price']=son.xpath(r"./td[position()=2]/text()")[0] if len(son.xpath(r".//td[position()=2]/text()"))>0 else [""]
            item['avg_price']=son.xpath(r"./td[position()=3]/text()")[0] if len(son.xpath(r".//td[position()=3]/text()"))>0 else [""]
            item['high_price']=son.xpath(r"./td[position()=4]/text()")[0] if len(son.xpath(r".//td[position()=4]/text()"))>0 else [""]
            item['guige']=son.xpath(r"./td[position()=5]/text()")[0] if len(son.xpath(r".//td[position()=5]/text()"))>0 else [""]
            item['unit']=son.xpath(r"./td[position()=6]/text()")[0] if len(son.xpath(r".//td[position()=6]/text()"))>0 else [""]
            # item['datetime']=son.xpath(r"./td[position()=7]/text()") if len(son.xpath(r".//td[position()=7]/text()"))>0 else ""
            if len(son.xpath(r".//td[position()=7]/text()")) > 0:
                item['datetime'] = son.xpath(r"./td[position()=7]/text()")
                item['datetime'] = datetime.datetime.strptime(item['datetime'][0],'%Y-%m-%d')
            else:
                item['datetime'] = [""]
            insert_into_mysql(item)
            content_list.append(item)
            # print(item)
        # print(content_list)


if __name__ == '__main__':
    xinfadi_fruits()