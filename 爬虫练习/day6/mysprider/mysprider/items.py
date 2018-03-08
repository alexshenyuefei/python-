# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MyspriderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

# Item 定义结构化数据字段，用来保存爬取到的数据，有点像Python中的dict，但是提供了一些额外的保护减少错误。
class ItcastItem(scrapy.Item):
    name = scrapy.Field()
    come_from = scrapy.Field()
    profile = scrapy.Field()
    title = scrapy.Field()
    avalon = scrapy.Field()