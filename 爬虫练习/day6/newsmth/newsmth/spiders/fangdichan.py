# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class FangdichanSpider(CrawlSpider):
    name = 'fangdichan'
    allowed_domains = ['newsmth.net']
    start_urls = ['http://www.newsmth.net/nForum/#!board/RealEstate?p=1']


    """
    /nForum/article/RealEstate/6673394  每个帖子
    /nForum/article/RealEstate/6670378
    /nForum/article/RealEstate/6647675?p=3 这种每个帖子的第x页不要
    
    /nForum/board/RealEstate?p=2 论坛第二页
    
    """
    rules = (
        Rule(LinkExtractor(allow=r'/nForum/board/RealEstate?p=\d+$'), follow=True), #请求论坛第x页
        Rule(LinkExtractor(allow=r'/nForum/article/RealEstate/\d+$'), callback='parse_item', follow=False),
    )

    def parse_item(self, response):
        item = {}
        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()
        return item
