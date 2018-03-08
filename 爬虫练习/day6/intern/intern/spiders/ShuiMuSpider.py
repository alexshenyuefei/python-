# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from selenium import webdriver
from asyncore import dispatcher
from intern.items import InternItem

class ShuimuspiderSpider(CrawlSpider):
    name = 'ShuiMuSpider'
    allowed_domains = ['newsmth.net']
    base_url = 'http://www.newsmth.net/nForum/board/Intern'
    start_urls = [base_url]
    start_urls.extend([base_url + '?p=' + str(i) for i in range(2, 4)])

    def __init__(self):
        scrapy.spiders.Spider.__init__(self)
        # if self.platform == 'linux':
        #     self.driver = webdriver.PhantomJS()
        self.driver = webdriver.PhantomJS(
                executable_path=r'C:\phantomjs\bin/phantomjs.exe')
        self.driver.set_page_load_timeout(10)

    def spider_closed(self, spider):
        self.driver.quit()

    def parse(self, response):
        self.driver.get(response.url)
        print
        response.url
        # 等待，直到table标签出现
        try:
            element = WebDriverWait(self.driver, 30).until(
                EC.presence_of_all_elements_located((By.TAG_NAME, 'table')))
            print
            'element:\n', element
        except Exception, e:
            print
            Exception, ":", e
            print
            "wait failed"
        page_source = self.driver.page_source
        bs_obj = BeautifulSoup(page_source, "lxml")
        print
        bs_obj
        table = bs_obj.find('table', class_='board-list tiz')
        print
        table
        print
        "find message ====================================\n"
        intern_messages = table.find_all('tr', class_=False)
        for message in intern_messages:
            title, href, time, author = '', '', '', ''
            td_9 = message.find('td', class_='title_9')
            if td_9:
                title = td_9.a.get_text().encode('utf-8', 'ignore')
                href = td_9.a['href']
            td_10 = message.find('td', class_='title_10')
            if td_10:
                time = td_10.get_text().encode('utf-8', 'ignore')
            td_12 = message.find('td', class_='title_12')
            if td_12:
                author = td_12.a.get_text().encode('utf-8', 'ignore')
            item = InternItem()
            print
            'title:', title
            print
            'href:', href
            print
            'time:', time
            print
            'author:', author
            item['title'] = title
            item['href'] = href
            item['time'] = time
            item['author'] = author
            item['base_url_index'] = 0
            # 嵌套爬取每条实习信息的具体内容
            root_url = 'http://www.newsmth.net'
            if href != '':
                content = self.parse_content(root_url + href)
            item['content'] = content
            yield item

