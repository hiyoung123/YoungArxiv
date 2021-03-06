
# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import copy
import os
import time
import random
import shutil
from urllib.request import urlopen
from twisted.enterprise import adbapi
import pymysql.cursors
from scrapy.exporters import CsvItemExporter

from YoungArxiv.utils.config import Config


class CSVPipeline(object):
    def __init__(self):
        self.file = open('../data/papers/papers.csv', 'wb')
        self.exporter = CsvItemExporter(self.file, include_headers_line=True,encoding='utf-8')
        self.exporter.start_exporting()
        self.saved_list = []

    def process_item(self, item, spider):
        if item['pid'] not in self.saved_list:
            self.exporter.export_item(item)
            self.saved_list.append(item['pid'])
        return item

    def close_spider(self, spider):
        self.exporter.finish_exporting()
        self.file.close()
        print('Saved item size: {0}'.format(len(self.saved_list)))

class DbPipeline(object):
    def __init__(self):
        """Initialize"""
        self.dbpool = adbapi.ConnectionPool('pymysql',
                host='localhost',
                db='YoungArxiv',
                user='root',
                passwd='liuhaiyang210',
                cursorclass=pymysql.cursors.DictCursor,
                charset='utf8',
                use_unicode=True
                )

    def shutdown(self):
        """Shutdown the connection pool"""
        self.dbpool.close()

    def process_item(self,item,spider):
        """Process each item process_item"""
        asynItem = copy.deepcopy(item) #解决插入数据混乱重复的bug，添加同步锁。
        query = self.dbpool.runInteraction(self.__insertdata, asynItem, spider)
        query.addErrback(self.handle_error)
        return item

    def __insertdata(self,tx,item,spider):
        """Insert data into the sqlite3 database"""

        tx.execute("select * from arxivapi_papermodel where `pid` = %s", item['pid'])
        result = tx.fetchone()
        if result:
            print("已经存在"+item['title'])
        else:
            print('insert {0}:{1}:{2}'.format(item['pid'],item['title'],item['favorite']))
            insert_sql = """
                    insert into arxivapi_papermodel(`pid`, `title`, `published`, `updated`, 
                    `summary`, `author`, `authors`, `cate`, `tags`, `link`, `pdf`, `version`, `favorite`, `pv`, `pv_total_times`) 
                    VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
                    """
            tx.execute(insert_sql,(
                        item['pid'],
                        item['title'],
                        item['published'],
                        item['updated'],
                        item['summary'],
                        item['author'],
                        item['authors'],
                        item['cate'],
                        item['tags'],
                        item['link'],
                        item['pdf'],
                        item['version'],
                        item['favorite'],
                        item['pv'],
                        item['pv_total_times']
                    ))
            print("Item stored in db")
    def handle_error(self,e):
        print(e)



def download_pdf(pdf_path,pdf_url):
    timeout_secs = 10
    # try retrieve the pdf
    if not os.path.exists(Config.PDF_PATH): os.makedirs(Config.PDF_PATH)
    try:
        print('fetching {0} into {1}'.format(pdf_url, pdf_path))
        req = urlopen(pdf_url, None, timeout_secs)
        with open(pdf_path, 'wb') as fp:
            shutil.copyfileobj(req, fp)
        time.sleep(0.05 + random.uniform(0, 0.1))
    except Exception as e:
        print('error downloading: {0}'.format(pdf_url))
        print(e)
        return False
    return True

def covert_thumb(pdf_path,thumb_path):
    if not os.path.exists(Config.THUMB_PATH): os.makedirs(Config.THUMB_PATH)
    if not os.path.exists(Config.TMP_PATH): os.makedirs(Config.TMP_PATH)
    tmp_path = os.path.join(Config.TMP_PATH,'thumb.png')

    cmd = 'convert {0}[0-7] -thumbnail x156 {1}'.format(pdf_path,tmp_path)
    os.system(cmd)
    if not os.path.isfile(os.path.join(Config.TMP_PATH,'thumb-0.png')):
        print('error {0} is not file'.format(tmp_path))
        return False
    cmd = 'montage -mode concatenate -quality 80 -tile x1 {0}/thumb-*.png {1}'.format(Config.TMP_PATH,thumb_path)
    os.system(cmd)

    if not os.path.isfile(thumb_path):
        print('error {0} is not file'.format(thumb_path))
        return False
    
    cmd = 'rm -rf {0}/thumb-*.png'.format(Config.TMP_PATH)
    os.system(cmd)
    return True
    



# if __name__ == '__main__':
#     covert_thumb('./data/pdf/1907.07212v2.pdf','./data/thumb/1907.07212v2.jpg')