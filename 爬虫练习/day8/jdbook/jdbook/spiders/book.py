# -*- coding: utf-8 -*-
import scrapy
from copy import deepcopy
import json

class BookSpider(scrapy.Spider):
    name = 'book'
    allowed_domains = ['jd.com','p.3.cn'] #允许多个域,p.3.cn是图书价格域
    start_urls = ['https://book.jd.com/booksort.html'] # 京东图书详情页

    def parse(self, response):
        book_catgory_lists = response.xpath("//div[@class='mc']//dd/em/a")  # 各个小图书分类的a标签
        for book_catgory in book_catgory_lists:
            item = {}
            item['book_catgory'] = book_catgory.xpath("./text()").extract_first()
            # item['book_catgory_url'] = "https:"+book_catgory.xpath("./@href").extract_first()
            book_catgory_url = book_catgory.xpath("./@href").extract_first()
            # print(item)
            if book_catgory_url:
                book_catgory_url = "https:" + book_catgory.xpath("./@href").extract_first()
                yield scrapy.Request(
                    book_catgory_url,callback=self.parse_book_catgory,
                    meta={"item":deepcopy(item)}
                )

    def parse_book_catgory(self, response):  # 图书小分类解析函数
        item = response.meta["item"]
        book_list_element = response.xpath("//div[@id='plist']//li[@class='gl-item']")
        for book in book_list_element:
            item["book_name"] = book.xpath(".//div[@class='p-name']/a/em/text()").extract_first()
            if item["book_name"]:
                item["book_name"] = item["book_name"].strip()
            item["book_author"] = book.xpath(".//span[@class='p-bi-name']/span/a/text()").extract()
            item["book_press"] = book.xpath(".//span[@class='p-bi-store']/a/text()").extract_first()
            item["book_publish_date"] = book.xpath(".//span[@class='p-bi-date']/text()").extract_first()
            if item["book_publish_date"]:
                item["book_publish_date"] = item["book_publish_date"].strip()
            item["book_sku"] = book.xpath("./div/@data-sku").extract_first()
            if item["book_sku"]:
                book_price_url = "https://p.3.cn/prices/mgets?skuIds=J_{}".format(item["book_sku"])
                yield scrapy.Request(
                    book_price_url,
                    callback=self.parse_book_price,
                    meta={"item": deepcopy(item)}
                )
        next_page_url = response.xpath("//a[@class='pn-next']/@href").extract_first()
        if next_page_url:
            next_page_url = "https://list.jd.com" + next_page_url
            yield scrapy.Request(
                next_page_url,
                callback=self.parse_book_catgory,
                meta = {"item": response.meta["item"]}
            )

    def parse_book_price(self, response):
        item = response.meta["item"]
        price_date = json.loads(response.body.decode())
        # <class 'list'> [{'op': '62.80', 'm': '93.00', 'id': 'J_11757834', 'p': '62.80'}]
        item["book_price"] = price_date[0].get("op",None) if len(price_date)>0 else None
        print(item,'*'*10)
        yield item