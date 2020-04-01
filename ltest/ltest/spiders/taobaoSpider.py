# -*- coding: utf-8 -*-
import scrapy


class TaobaospiderSpider(scrapy.Spider):
    name = 'taobaoSpider'
    allowed_domains = ['baidu.com']
    start_urls = ['http://baidu.com/']

    def parse(self, response):
        pass
