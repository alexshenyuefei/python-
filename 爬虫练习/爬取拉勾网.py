from selenium import webdriver
from lxml import etree
from pymysql import *
import time
conn = connect(host='localhost', port=3306,database='work', user='root',password='python', charset='utf8')
def insert_date(job_name,work_place,salary,job_require,company_name,work_keyword,position_id):
    try:
        cur = conn.cursor()
        result = cur.execute('INSERT INTO pythonshanghai(job_name,work_place,salary,job_require,company_name,wo_rkkeyword,position_id) VALUES(%s,%s,%s,%s,%s,%s,%s)',(job_name, work_place, salary, job_require, company_name, work_keyword,position_id))
        print(result)
        conn.commit()
    except Exception as e:
        print(e)
    finally:
        cur.close()


"""
https://www.lagou.com/jobs/list_Python?px=default&city=%E5%8C%97%E4%BA%AC


"""
"""拉勾python北京站"""

content = ""
work_number = 0
URL = 'https://www.lagou.com/jobs/list_Python?px=default&city=%E4%B8%8A%E6%B5%B7'
driver = webdriver.Chrome()
driver.get(url=URL)

html_element_result = driver.page_source # driver.page_source是浏览器渲染后的页面,即elements,类型是str
temp_html = etree.HTML(html_element_result)
job_element_list = temp_html.xpath(r"//li[@data-index]")
job_lists = []
for job_element in job_element_list:
    job = {}
    job['job_name'] = job_element.xpath(r".//h3/text()") if len(job_element.xpath(r".//h3/text()")) > 0 else ["",]
    job['work_place'] = job_element.xpath(r".//span/em/text()") if len(job_element.xpath(r".//span/em/text()")) > 0 else ["",]
    job['salary'] = job_element.xpath(r"./@data-salary") if len(job_element.xpath(r"./@data-salary")) > 0 else ["",]
    job['job_require'] = job_element.xpath(r".//div[@class='p_bot']//div[@class='li_b_l']/text()") if len(job_element.xpath(r".//div[@class='p_bot']//div[@class='li_b_l']/text()")) > 0 else ["",]
    job['company_name'] = job_element.xpath(r".//div[@class='company_name']/a/text()") if len(job_element.xpath(r".//div[@class='company_name']/a/text()")) > 0 else ["",]
    job['work_keyword'] = job_element.xpath(r".//div[@class='list_item_bot']//div[@class='li_b_l']//span/text()") if len(job_element.xpath(r".//div[@class='list_item_bot']//div[@class='li_b_l']//span/text()")) > 0 else ["", ]
    job['position_id'] = job_element.xpath(r"./@data-positionid") if len(job_element.xpath(r"./@data-positionid")) > 0 else ["", ]
    job_lists.append(job)
print(job_lists,'第一页')
for job in job_lists:
    work_number += 1
    content += '工作名字: '+job['job_name'][0].strip()+'\n'
    content += '工作地点: '+job['work_place'][0].strip()+'\n'
    content += '工资: '+job['salary'][0].strip()+'\n'
    content += '工作要求: '+job['job_require'][2].strip()+'\n'
    content += '公司名: '+job['company_name'][0].strip()+'\n'
    content += '关键字: '+str(job['work_keyword'])+'\n\n\n'
    job_name = job['job_name'][0].strip()
    work_place = job['work_place'][0].strip()
    salary = job['salary'][0].strip()
    job_require = job['job_require'][2].strip()
    company_name = job['company_name'][0].strip()
    work_keyword = str(job['work_keyword'])
    position_id = job['position_id'][0].strip()
    insert_date(job_name=job_name, work_place=work_place, salary=salary, job_require=job_require,company_name=company_name, work_keyword=work_keyword,position_id=position_id)

# job_name,work_place,salary,job_require,company_name,work_keyword

"""
点击下一页,获取新的elements
"""
"""
有bug,按钮灰了,还存在下一页还能爬取
"""
for i in range(2,100):
    """当这次数据和上一次数据一样时,跳出循环"""
    prev = content #上一次数据
    time.sleep(2)
    print('点击下一页')
    driver.find_element_by_xpath(r"//span[@action='next']").click()  # 点击下一页
    #要等第二页加载完成
    time.sleep(5)
    html_element_result = driver.page_source # driver.page_source是浏览器渲染后的页面,即elements,类型是str
    temp_html = etree.HTML(html_element_result)
    job_element_list = temp_html.xpath(r"//li[@data-index]")
    job_lists = []
    for job_element in job_element_list:
        job = {}
        job['job_name'] = job_element.xpath(r".//h3/text()") if len(job_element.xpath(r".//h3/text()")) > 0 else ["",]
        job['work_place'] = job_element.xpath(r".//span/em/text()") if len(job_element.xpath(r".//span/em/text()")) > 0 else ["",]
        job['salary'] = job_element.xpath(r"./@data-salary") if len(job_element.xpath(r"./@data-salary")) > 0 else ["",]
        job['job_require'] = job_element.xpath(r".//div[@class='p_bot']//div[@class='li_b_l']/text()") if len(job_element.xpath(r".//div[@class='p_bot']//div[@class='li_b_l']/text()")) > 0 else ["",]
        job['company_name'] = job_element.xpath(r".//div[@class='company_name']/a/text()") if len(job_element.xpath(r".//div[@class='company_name']/a/text()")) > 0 else ["",]
        job['work_keyword'] = job_element.xpath(r".//div[@class='list_item_bot']//div[@class='li_b_l']//span/text()") if len(job_element.xpath(r".//div[@class='list_item_bot']//div[@class='li_b_l']//span/text()")) > 0 else ["",]
        job['position_id'] = job_element.xpath(r"./@data-positionid") if len(job_element.xpath(r"./@data-positionid")) > 0 else ["",]
        job_lists.append(job)
    print('第{}页'.format(i),job_lists,)
    content = ""
    for job in job_lists:
        work_number += 1
        print(work_number)
        content += '工作名字: '+job['job_name'][0].strip()+'\n'
        content += '工作地点: '+job['work_place'][0].strip()+'\n'
        content += '工资: '+job['salary'][0].strip()+'\n'
        content += '工作要求: '+job['job_require'][2].strip()+'\n'
        content += '公司名: '+job['company_name'][0].strip()+'\n'
        content += '关键字: '+str(job['work_keyword'])+'\n\n\n'
        job_name = job['job_name'][0].strip()
        work_place = job['work_place'][0].strip()
        salary = job['salary'][0].strip()
        job_require = job['job_require'][2].strip()
        company_name = job['company_name'][0].strip()
        work_keyword = str(job['work_keyword'])
        position_id = job['position_id'][0].strip()
        insert_date(job_name=job_name, work_place=work_place, salary=salary, job_require=job_require,
                    company_name=company_name, work_keyword=work_keyword, position_id=position_id)
    if content == prev:
        print('结束循环')
        with open('拉勾python上海.txt', 'a', encoding='utf-8') as f:
            f.write('\n\n\n')
            f.write('今日工作总数: {}个工作'.format(work_number))
            conn.close()
            driver.quit()
        break
    with open('拉勾python上海.txt','a',encoding='utf-8') as f:
        f.write(content)

