# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class YoungarxivItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class ArxivItem(scrapy.Item):
    id = scrapy.Field()
    pid = scrapy.Field()
    title = scrapy.Field()
    published = scrapy.Field()
    updated = scrapy.Field()
    summary = scrapy.Field()
    author = scrapy.Field()
    authors = scrapy.Field()
    cate = scrapy.Field()
    tags = scrapy.Field()
    link = scrapy.Field()
    pdf = scrapy.Field()
    version = scrapy.Field()
    favorite = scrapy.Field()
    pv = scrapy.Field()
    pv_total_times = scrapy.Field()

    def to_dict(self):
        res = {}
        for k,v in super().items():
            res[k] = v
        return res

