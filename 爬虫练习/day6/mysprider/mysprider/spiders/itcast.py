# -*- coding: utf-8 -*-
import scrapy
from mysprider.items import ItcastItem  # 从项目根目录导包
import logging
logger = logging.getLogger(__name__)
class ItcastSpider(scrapy.Spider):
    name = 'itcast'
    allowed_domains = ['itcast.cn']
    start_urls = ["http://www.itcast.cn/channel/teacher.shtml"]

    def parse(self, response):
        li_list = response.xpath("//div[@class='tea_con']/div/ul/li")
        for li in li_list:
            item = ItcastItem()
            item["name"] = li.xpath(".//h3/text()").extract_first()
            item["title"] = li.xpath(".//h4/text()").extract_first()
            item["profile"] = li.xpath(".//p/text()").extract_first()
            item["come_from"] = "itcast"
            # print(item)
            # logger.warning(item)

            # 将获取的数据交给pipelines
            yield item

            # 返回数据，不经过pipeline
            # return item
