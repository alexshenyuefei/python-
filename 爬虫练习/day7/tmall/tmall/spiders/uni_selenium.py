# -*- coding: utf-8 -*-
import scrapy
from selenium import webdriver
import time
from lxml import etree

class UniSeleniumSpider(scrapy.Spider):
    name = 'uni_selenium'
    allowed_domains = ['tmall.com']
    start_urls = ['https://uniqlo.tmall.com/category-97377015.htm',]

    def __init__(self):
        # self.driver = webdriver.PhantomJS(r'C:\phantomjs\bin\phantomjs.exe')
        self.driver = webdriver.Chrome()
        self.driver.set_page_load_timeout(20)

    def parse(self, response):
        self.driver.get(response.url)
        # self.driver.save_screenshot("优衣库截屏.png")
        time.sleep(10)
        html_element_result = self.driver.page_source
        temp_html = etree.HTML(html_element_result)
        cloths_element_list = temp_html.xpath(r'//div[@class="J_TItems"]//*[position()<=8]//dl[@data-id]')
        for cloth_element in cloths_element_list:
            cloth = {}
            if len(cloth_element.xpath(r".//a[@class='item-name J_TGoldData']/text()")):
                cloth['cloth_name'] = cloth_element.xpath(r".//a[@class='item-name J_TGoldData']/text()")[0]
            else:
                cloth['cloth_name'] = ""
            if len(cloth_element.xpath(r".//span[@class='c-price']/ text()")):
                cloth['cloth_price'] = cloth_element.xpath(r".//span[@class='c-price']/ text()")[0].strip()
            else:
                cloth['cloth_price'] = ""
            if len(cloth_element.xpath(r".//span[@class='sale-num']/ text()")):
                cloth['sales_number'] = cloth_element.xpath(r".//span[@class='sale-num']/ text()")[0]
            else:
                cloth['sales_number'] = ""
            if len(cloth_element.xpath(r".//h4//span/text()")):
                cloth['comment_number'] = cloth_element.xpath(r".//h4//span/text()")[0]
            else:
                cloth['comment_number'] = ""
            print(cloth,)
            yield cloth

        next_url_element = temp_html.xpath(r"//a[@class='J_SearchAsync next']/@href")
        if len(next_url_element):
            next_url = "https:"+next_url_element[0]
            print(next_url, '*' * 10)
            yield scrapy.Request(url=next_url,callback=self.parse)


    # def spider_closed(self, spider):
    #     self.driver.quit()
