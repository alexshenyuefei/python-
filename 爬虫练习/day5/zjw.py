import requests
from lxml import etree
import random
import time
"""
违反中央八项规定精神问题
第一页:http://www.ccdi.gov.cn/special/jdbg3/qb_bgt/fjbxgdwt_jdbg3/index.html
第二页:http://www.ccdi.gov.cn/special/jdbg3/qb_bgt/fjbxgdwt_jdbg3/index_1.html
"""
class ZjwSpider(object):
    def __init__(self):
        firstpage = 'http://www.ccdi.gov.cn/special/jdbg3/qb_bgt/fjbxgdwt_jdbg3/index.html'
        url_lists=[firstpage,]
        for i in range(1,100):
            url = 'http://www.ccdi.gov.cn/special/jdbg3/qb_bgt/fjbxgdwt_jdbg3/index_{}.html'.format(i)
            url_lists.append(url)
        self.url_lists = url_lists
        self.headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36"}
        self.part_url = 'http://www.ccdi.gov.cn/special/jdbg3'

    def parse_url(self,url):
        print(url)
        session = requests.session()
        session.trust_env = False
        response = session.get(url,headers=self.headers)
        return response.content

    def get_content_list(self,html_str):
        """
        父元素：//li[@class='fixed']

        a标签 //li[@class='fixed']//a
        时间 //li[@class='fixed']//span
        获取列表页标题和链接
        """
        html = etree.HTML(html_str)
        li_lists = html.xpath("//li[@class='fixed']")
        content_list = []
        for li in li_lists:
            item = {}
            """xpath默认返回的都是"""
            item["title"] = li.xpath(".//a/text()")[0] if len(li.xpath(".//a/text()"))>0 else [""]
            item["href"] = self.part_url + li.xpath(".//a/@href")[0][5:] if len(li.xpath(".//a/@href")[0]) > 0 else [""]
            content_list.append(item)
        print(content_list)
        return content_list

    def get_detail(self,detail_url):
        """
        父元素://div[@class="flater_tab"]
        标题://div[@class="flater_tab"]//h2
        内容://div[@class="flater_tab"]//p
        """
        print('正在请求详情页')
        a = random.randint(1, 5)
        time.sleep(a)
        detail_html_str = self.parse_url(detail_url)
        detail_html = etree.HTML(detail_html_str)
        title = detail_html.xpath('//div[@class="flater_tab"]//h2/text()') if len(detail_html.xpath('//div[@class="flater_tab"]//h2/text()')) >0 else [""]
        content = detail_html.xpath('//div[@class="flater_tab"]//p/text()') if len(detail_html.xpath('//div[@class="flater_tab"]//p/text()')) >0 else [""]

        return title,content

    def save_content_list(self,title,content):
        with open('zjw.txt','a',encoding='utf-8') as f:
            content = str(content)
            content = content.replace("['", '')
            content = content.replace("']", '')
            content = content.replace(r"\u3000\u30001.", '')
            content = content.replace(r"\u3000\u30002.", '')
            content = content.replace(r"\u3000\u30003.", '')
            content = content.replace(r"\u3000\u3000", '')

            f.write(title[0].strip()+'\n')
            f.write(content+'\n\n')

    def run(self):
        for url in self.url_lists:
            html_str = self.parse_url(url=url)
            content_list = self.get_content_list(html_str)
            for item in content_list:
                detail_url = item["href"]
                title,content =self.get_detail(detail_url)
                self.save_content_list(title,content)

if __name__ == '__main__':
    spider = ZjwSpider()
    spider.run()
