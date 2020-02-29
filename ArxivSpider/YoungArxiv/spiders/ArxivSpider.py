# -*- coding: utf-8 -*-

import os
import scrapy
import feedparser
import dateutil.parser
from YoungArxiv.items import ArxivItem
from YoungArxiv.utils.common import encode_feedparser_dict
from YoungArxiv.utils.config import Config

class ArxivspiderSpider(scrapy.Spider):
    name = 'ArxivSpider'
    allowed_domains = ['export.arxiv.org']

    start_index = Config.start_index
    end_index = Config.end_index
    batch_size = Config.batch_size
    filter_idx = 0

    # filter_search = 'cat:cs.CV+OR+cat:cs.AI+OR+cat:cs.LG+OR+cat:cs.CL+OR+cat:cs.NE+OR+cat:stat.ML' #96404
    # filter_search = 'all:cs.CV+OR+all:cs.AI+OR+all:cs.LG+OR+all:cs.CL+OR+all:cs.NE+OR+all:stat.ML' #96410
    filter_list = ['all:cs.CV', 'all:cs.AI', 'all:cs.LG', 'all:cs.CL', 'all:cs.NE', 'all:stat.ML']
    '''
        all:cs.CV : 37321
        all:cs.AI : 22648
        all:cs.LG : 50515
        all:cs.CL : 17634
        all:cs.NE : 7473
        all:stat.ML : 36627
        all : 113837 - 172218
    '''
    query_url = 'http://export.arxiv.org/api/query?search_query={0}&sortBy=lastUpdatedDate&start={1}&max_results={2}'
    start_urls = [query_url.format(filter_list[filter_idx],start_index,batch_size)]

    def parse(self, response):
        item = ArxivItem()
        parser = feedparser.parse(response.body)
        if self.end_index == -1 :
            self.end_index = int(parser.feed['opensearch_totalresults'])
        for i in parser.entries:
            j = encode_feedparser_dict(i)
            item['pid'] = j['id'].split('/')[-1]
            item['title'] = j['title'].replace('\n','').strip()
            item['published'] = dateutil.parser.parse(j['published'])
            item['updated'] = dateutil.parser.parse(j['updated'])
            item['summary'] = j['summary'].replace('\n','').strip()
            item['author'] = j['author']
            item['authors'] = '|'.join([x['name'] for x in j['authors']])
            item['cate'] = j['arxiv_primary_category']['term']
            item['tags'] = '|'.join([x['term'] for x in j['tags']])
            item['link'] = j['link']
            item['pdf'] = [x['href'] for x in j['links'] if x['type'] == 'application/pdf'][0]+'.pdf'
            item['version'] = item['pid'].split('v')[-1]
            item['pv'] = 0  # 假数据
            item['pv_total_times'] = 0  # 假数据
            item['favorite'] = self.start_index # 假数据
            item['id'] = self.start_index # 假数据
            self.start_index += 1
            yield item

        if self.start_index < self.end_index and self.start_index < 50000:
            yield scrapy.Request(url=self.query_url.format(self.filter_list[self.filter_idx],self.start_index,self.batch_size),
                                 callback=self.parse,dont_filter=True)
        elif self.filter_idx < len(self.filter_list):
            # 爬取下一个分类
            self.filter_idx = self.filter_idx + 1
            self.start_index = Config.start_index
            self.end_index = Config.end_index
            yield scrapy.Request(
                url=self.query_url.format(self.filter_list[self.filter_idx], self.start_index, self.batch_size),
                callback=self.parse, dont_filter=True)
        else:
            print('Done')