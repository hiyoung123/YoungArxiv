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
    version = scrapy.Field()
    author = scrapy.Field()
    authors = scrapy.Field()
    summary = scrapy.Field()
    title = scrapy.Field()
    updated = scrapy.Field()
    published = scrapy.Field()
    link = scrapy.Field()
    pdf_path = scrapy.Field()
    pdf_url = scrapy.Field()
    thumb_path = scrapy.Field()
    tags = scrapy.Field()
    arxiv_primary_category = scrapy.Field()

    # title_detail = scrapy.Field()
    # updated_parsed = scrapy.Field()
    # published_parsed = scrapy.Field()
    # guidislink = scrapy.Field()
    # author_detail = scrapy.Field()
    # summary_detail = scrapy.Field()
    # links = scrapy.Field()

    def to_dict(self):
        res = {}
        for k,v in super().items():
            res[k] = v
        return res

