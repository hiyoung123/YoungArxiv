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
            item['published'] = j['published']
            item['author'] = j['author']
            item['authors'] = [x['name'] for x in j['authors']]
            item['link'] = j['link']
            item['summary'] = j['summary']
            item['title'] = j['title']
            item['tags'] = [x['term'] for x in j['tags']]
            item['updated'] = j['updated']
            item['arxiv_primary_category'] = j['arxiv_primary_category']['term']
            pid, version = parse_arxiv_url(item['link'])
            item['pid'] = pid
            item['version'] = version
            pdfs = [x['href'] for x in j['links'] if x['type'] == 'application/pdf']
            pdf_url = pdfs[0] + '.pdf'
            basename = pdfs[0].split('/')[-1]
            fname = os.path.join(Config.PDF_PATH, basename+'.pdf')
            tname = os.path.join(Config.THUMB_PATH,basename+'.jpg')
            item['pdf_path'] = fname
            item['pdf_url'] = pdf_url
            item['thumb_path'] = tname



            # item['title_detail'] = j['title_detail']
            # item['updated_parsed'] = j['updated_parsed']
            # item['published_parsed'] = j['published_parsed']
            # item['guidislink'] = j['guidislink']
            # item['author_detail'] = j['author_detail']
            # item['summary_detail'] = j['summary_detail']
            # item['links'] = j['links']

            self.start_index += 1
            yield item

        if self.start_index < self.end_index :
            yield scrapy.Request(url=self.query_url.format(self.filter_search,self.start_index,self.batch_size),
                                 callback=self.parse,dont_filter=True)


def parse_arxiv_url(url):
  """
  examples is http://arxiv.org/abs/1512.08756v2
  we want to extract the raw id and the version
  """
  ix = url.rfind('/')
  idversion = url[ix+1:] # extract just the id (and the version)
  parts = idversion.split('v')
  assert len(parts) == 2, 'error parsing url ' + url
  return parts[0], int(parts[1])