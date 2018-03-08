# -*- coding: utf-8 -*-
import scrapy
import re
class BookSpider(scrapy.Spider):
    name = 'book'
    allowed_domains = ['suning.com']
    start_urls = ['http://snbook.suning.com/web/trd-fl/100301/46.htm']

    def parse(self, response):
        book_cargory_lists = response.xpath('//li/div[@class=\'three-sort\']/a/@href').extract()
        for book_url in book_cargory_lists:
            book_small_cargory_url = 'http://snbook.suning.com'+book_url
            # print(book_small_cargory_url)
            yield scrapy.Request(url=book_small_cargory_url,callback=self.parse_book_small_list,)

    def parse_book_small_list(self, response):
        """各个图书小类别详情解析"""
        """第一次:http://snbook.suning.com/web/trd-fl/150400/51.htm
        第二次:http://snbook.suning.com/web/trd-fl/150400/51.htm??pageNumber=2
        使用正则表达式把后缀清除
        """
        if re.findall(r'\?pageNumber=(\d+)', response.url): #能够提取页码标签时候
            page = re.findall(r'\?pageNumber=(\d+)', response.url) #findall给的是列表
            page = int(page[0])
        else:
            page = 1
        url = response.url
        url = re.sub(r'\?pageNumber=(\d+)', '', url)
        """//div[@id='pagebottomxx']/a[@class='next']"""
        book_href_lists = response.xpath("//div[@class='book-title']/a/@href").extract() #各个图书跳转标签列表
        # next_page_url = response.xpath() # 图书下一页
        # 如果xpath //span[@style="cursor: not-allowed;"]存在,就没有下一页,不生成下一页请求,并且图书列表也要存在
        # print(response.url)
        if not response.xpath('//span[@style="cursor: not-allowed;"]')and book_href_lists:
            page += 1
            # print('进入第%{}页'.format(page))
            next_page_url = url+'?pageNumber={}'.format(page)
            yield scrapy.Request(url=next_page_url,callback=self.parse_book_small_list,)

        """"当前地址的url+?pageNumber=2是第二页"""
        for book_detail_url in book_href_lists:
            yield scrapy.Request(url=book_detail_url,callback=self.parse_book_detail,)


    def parse_book_detail(self, response):
        book_element = response.xpath("//div[contains(@class,'brief-info')]")
        book_item={}
        book_item['title'] = book_element.xpath(".//strong/text()").extract_first()
        # book_item['price'] = book.xpath(".//div[@class='parm wauto']//span[contains(@class,'snPrice')]//em/text()").extract_first()
        # 图书价格是通过js动态生成的所以只能用正则表达式匹配
        book_item["price"] = re.findall(r"\"bp\":'(.*?)',",response.body.decode(),re.S)[0]
        # print(book_item)
        yield book_item
