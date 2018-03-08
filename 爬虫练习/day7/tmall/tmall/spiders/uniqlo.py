# -*- coding: utf-8 -*-
import scrapy
import requests

"""
优衣库商品详情页
https://uniqlo.tmall.com/category.htm
"""
class UniqloSpider(scrapy.Spider):
    name = 'uniqlo'
    allowed_domains = ['tmall.com']
    start_urls = ['https://uniqlo.tmall.com/category.htm']

    def parse(self, response):
        """/i/asynSearch.htm?mid=w-15676986369-0&wid=15676986369&path=/category.htm商品详情信息部分连接"""
        temp_search_url = response.xpath("//input[@id='J_ShopAsynSearchURL']/@value").extract_first()
        temp_url = requests.utils.urlparse(response.request.url)
        # 补完详情页的url的地址
        search_url = temp_url.scheme + "://" + temp_url.netloc + temp_search_url
        print(search_url, "*" * 100)
        # 向商品详情页发送请求
        yield scrapy.Request(
            search_url,
            callback=self.parse_product_list
        )

