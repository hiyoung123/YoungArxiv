# -*- coding: utf-8 -*-

import os
import scrapy
import feedparser
from YoungArxiv.items import ArxivItem
from YoungArxiv.utils.common import encode_feedparser_dict
from YoungArxiv.utils.config import Config

class ArxivspiderSpider(scrapy.Spider):
    name = 'ArxivSpider'
    allowed_domains = ['export.arxiv.org']

    start_index = Config.start_index
    end_index = Config.end_index
    batch_size = Config.batch_size


    filter_search = 'cat:cs.CV+OR+cat:cs.AI+OR+cat:cs.LG+OR+cat:cs.CL+OR+cat:cs.NE+OR+cat:stat.ML' #96404
    # all: cs.CV + OR + all:cs.AI + OR + all: cs.LG + OR + all:cs.CL + OR + all: cs.NE + OR + all:stat.ML 96410
    query_url = 'http://export.arxiv.org/api/query?search_query={0}&sortBy=lastUpdatedDate&start={1}&max_results={2}'
    start_urls = [query_url.format(filter_search,start_index,batch_size)]

    def parse(self, response):
        item = ArxivItem()
        parser = feedparser.parse(response.body)
        if self.end_index == -1 :
            self.end_index = int(parser.feed['opensearch_totalresults'])
        for i in parser.entries:
            j = encode_feedparser_dict(i)
            item['id'] = self.start_index
            item['pid'] = j['id'].split('/')[-1]
            item['title'] = j['title'].replace('\n','').strip()
            item['published'] = j['published']
            item['updated'] = j['updated']
            item['summary'] = j['summary'].replace('\n','').strip()
            item['author'] = j['author']
            item['authors'] = '|'.join([x['name'] for x in j['authors']])
            item['cate'] = j['arxiv_primary_category']['term']
            item['tags'] = '|'.join([x['term'] for x in j['tags']])
            item['link'] = j['link']
            item['pdf'] = [x['href'] for x in j['links'] if x['type'] == 'application/pdf'][0]+'.pdf'
            item['version'] = item['pid'].split('v')[-1]
            self.start_index += 1
            yield item

        if self.start_index < self.end_index :
            yield scrapy.Request(url=self.query_url.format(self.filter_search,self.start_index,self.batch_size),
                                 callback=self.parse,dont_filter=True)

