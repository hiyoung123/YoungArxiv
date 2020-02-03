# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import json
import os
import time
import random
import shutil
from urllib.request import urlopen

from YoungArxiv.db.mgdb import MgDb
from YoungArxiv.db.esdb import EsDb
from YoungArxiv.utils.config import Config

class ToMongoDbPipeline(object):

    def __init__(self):
        self.db = MgDb()
        self.skip_num = 0
        self.insert_num = 0

    def process_item(self, item, spider):
        result = self.db.find_one_by_id(item['id'])
        if result is None or len(result) == 0 or result['version'] < item['version']:
            if download_pdf(item['pdf_path'], item['pdf_url']):
                if not covert_thumb(item['pdf_path'],item['thumb_path']):
                    item['thumb_path'] = os.path.join(Config.THUMB_PATH,'missing.jpg')
                self.db.insert_one(item.to_dict())
                self.insert_num += 1
                print('insert item {0}'.format(self.insert_num))
            else:
                self.skip_num += 1
                print('skip item {0}'.format(self.skip_num))
        else:
            self.skip_num += 1
            print('skip item {0}'.format(self.skip_num))


class ToEsPipeline(object):
    def __init__(self):
        self.db = EsDb()
        self.skip_num = 0
        self.insert_num = 0

    def process_item(self, item, spider):
        result = self.db.find_one_by_id(item['id'])
        if result is None or len(result) == 0 or result[0]['_source']['version'] < item['version']:
            if download_pdf(item['pdf_path'], item['pdf_url']):
                if not covert_thumb(item['pdf_path'], item['thumb_path']):
                    item['thumb_path'] = os.path.join(Config.THUMB_PATH, 'missing.jpg')
                self.db.insert_one(item)
                self.insert_num += 1
                print('insert item {0}'.format(self.insert_num))
            else:
                self.skip_num += 1
                print('skip item {0}'.format(self.skip_num))
        else:
            self.skip_num += 1
            print('skip item {0}'.format(self.skip_num))


class ToJsonPipeline(object):

    def open_spider(self, spider):
        self.file = open('../data/papers/papers.json', 'w')

    def close_spider(self, spider):
        self.file.close()

    def process_item(self, item, spider):
        line = json.dumps(dict(item)) + "\n"
        self.file.write(line)
        return item


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