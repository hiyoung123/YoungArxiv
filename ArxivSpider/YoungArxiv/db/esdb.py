#!usr/bin/env python  
#-*- coding:utf-8 _*-  
""" 
@author: hiyoung 
@file: esdb
@time: 2019/9/9:
"""

from elasticsearch_dsl import Document, Date, Integer, Keyword, Text, connections,Completion
from elasticsearch_dsl.analysis import CustomAnalyzer as _CustomAnalyzer
from elasticsearch_dsl import Search

from elasticsearch import Elasticsearch

# Define a default Elasticsearch client
es = connections.create_connection(hosts=['localhost'])

class CustomAnalyzer(_CustomAnalyzer):
    def get_analysis_definition(self):
        return {}

ik_analyzer = CustomAnalyzer("ik_max_word", filter=["lowercase"])

class ArxivIndex(Document):
    id = Text()
    version = Text()
    author = Keyword()
    authors = Keyword()
    summary = Text(analyzer='snowball')
    title = Text(analyzer='snowball', fields={'raw': Keyword()})
    updated = Date()
    published = Date()
    link = Text()
    pdf_path = Text()
    pdf_url = Text()
    thumb_path = Text()
    tags = Text(analyzer='snowball')
    arxiv_primary_category = Text()

    suggest = Completion(analyzer='snowball')

    class Index:
        name = 'arxiv'

class EsDb(object):
    def __init__(self):

        self.client = Elasticsearch()

    def find_one_by_id(self,id):
        if self.client != None and id != None:
            s = Search(index='arxiv').using(self.client).query("match", id=id)
            response = s.execute()
            return response.hits.hits
        return None

    def insert_one(self,item):
        arxiv = ArxivIndex()
        arxiv.id = item['id']
        arxiv.version = item['version']
        arxiv.title = item['title']
        arxiv.author = item['author']
        arxiv.authors = item['authors']
        arxiv.summary = item['summary']
        arxiv.published = item['published']
        arxiv.updated = item['updated']
        arxiv.thumb_path = item['thumb_path']
        arxiv.pdf_path = item['pdf_path']
        arxiv.pdf_url = item['pdf_url']
        arxiv.tags = item['tags']
        arxiv.link = item['link']
        arxiv.arxiv_primary_category = item['arxiv_primary_category']

        arxiv.suggest = gen_suggests('arxiv', ((arxiv.title,10),(arxiv.summary, 7)))

        arxiv.save()

def gen_suggests(index, info_tuple):
    used_words = set()
    suggests = []
    for text, weight in info_tuple:
        if text:
            words = es.indices.analyze(index=index,body={'text':text,'analyzer':"ik_max_word"})
            anylyzed_words = set([r["token"] for r in words["tokens"] if len(r["token"])>1])
            new_words = anylyzed_words - used_words
        else:
            new_words = set()

        if new_words:
            suggests.append({"input":list(new_words), "weight":weight})

    return suggests


# if __name__ == '__main__':
#     ArxivIndex.init()