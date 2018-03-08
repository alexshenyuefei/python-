# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from pymongo import MongoClient

class SuningbookPipeline(object):
    def open_spider(self,spider):
        client = MongoClient("192.168.111.130", 27017)
        self.collection = client["book"]["suningbook"]
    def process_item(self, item, spider):
        self.collection.insert(item)
        return item

class SuningbookPipeline2(object):
    def open_spider(self,spider):
        client = MongoClient("192.168.111.130", 27017)
        self.collection = client["book"]["suningbook"]
    def process_item(self, item, spider):
        self.collection.insert(item)
        return item
