# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class MyspriderPipeline(object):
    def process_item(self, item, spider):
        """item由spider传到引擎,再由引擎传到Pipeline"""
        if item["come_from"] == "itcast":
            item['avalon'] = '亚瑟王'
            print(item)
        """传递数据给下一个管道,没有下一个管道就不用return数据了"""
        # return item
