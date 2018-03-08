from datetime import datetime
from urllib.parse import urlencode
from multiprocessing import Pool
import requests
from bs4 import BeautifulSoup
from zhilian_kw_config import *
import time
from itertools import product
import pymysql


connection = pymysql.connect(**configs)

def date_insert(item):
    try:
        with connection.cursor() as cursor:
            sql = 'INSERT INTO zhilian(zwmc,fkl,gsmc,zwyx,gzdd,gbsj,brief,zw_link,save_date) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)'
            cursor.execute(sql,(item["zwmc"],item["fkl"],item["gsmc"],item["zwyx"],
                                item["gzdd"],item["gbsj"],item["brief"],item["zw_link"],item["save_date"]))
        connection.commit()
    except Exception as e:
        print(e)

def download(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:51.0) Gecko/20100101 Firefox/51.0'}
    response = requests.get(url, headers=headers)
    return response.text

def get_content(html):
    # 记录保存日期
    date = datetime.now().date()
    date = datetime.strftime(date, '%Y-%m-%d')  # 转变成str

    soup = BeautifulSoup(html, 'lxml')
    body = soup.body
    data_main = body.find('div', {'class': 'newlist_list_content'})

    if data_main:
        tables = data_main.find_all('table')

        for i, table_info in enumerate(tables):
            if i == 0:
                continue
            tds = table_info.find('tr').find_all('td')
            zwmc = tds[0].find('a').get_text()  # 职位名称
            zw_link = tds[0].find('a').get('href')  # 职位链接
            fkl = tds[1].find('span').get_text()  # 反馈率
            gsmc = tds[2].find('a').get_text()  # 公司名称
            zwyx = tds[3].get_text()  # 职位月薪
            gzdd = tds[4].get_text()  # 工作地点
            gbsj = tds[5].find('span').get_text()  # 发布日期

            tr_brief = table_info.find('tr', {'class': 'newlist_tr_detail'})
            # 招聘简介
            brief = tr_brief.find('li', {'class': 'newlist_deatil_last'}).get_text()

            # 用生成器获取信息
            item ={'zwmc': zwmc,  # 职位名称
                   'fkl': fkl,  # 反馈率
                   'gsmc': gsmc,  # 公司名称
                   'zwyx': zwyx,  # 职位月薪
                   'gzdd': gzdd,  # 工作地点
                   'gbsj': gbsj,  # 公布时间
                   'brief': brief,  # 招聘简介
                   'zw_link': zw_link,  # 网页链接
                   'save_date': date  # 记录信息保存的日期
                   }
            yield item

def main(args):
    basic_url = 'http://sou.zhaopin.com/jobs/searchresult.ashx?'

    for keyword in KEYWORDS:
        paras = {'jl': args[0],
                 'kw': keyword,
                 'p': args[1]  # 第X页
                 }
        url = basic_url + urlencode(paras)
        # print(url)
        html = download(url)
        # print(html)
        if html:
            data = get_content(html)
            # print(data)
            for item in data:
                print(item,type(item))
                date_insert(item)

if __name__ == '__main__':
    start = time.time()
    number_list = list(range(TOTAL_PAGE_NUMBER))
    args = product(ADDRESS, number_list)
    pool = Pool()
    pool.map(main, args) # 多进程运行
    end = time.time()
    print('Finished, task runs %s seconds.' % (end - start))