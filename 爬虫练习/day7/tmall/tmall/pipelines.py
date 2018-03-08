# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql

class TmallPipeline(object):
    def open_spider(self, spider):
        conn = pymysql.connect(host='localhost', port=3306, database='uniqlo', user='root', password='python', charset='utf8')
    def process_item(self, item, spider):
        return item

    def close_spider(self, spider):
        print('close_spider启动')