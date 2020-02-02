#!usr/bin/env python  
#-*- coding:utf-8 _*-  
""" 
@author: hiyoung 
@file: mgdb
@time: 2019/8/30:
"""
import pymongo

class MgDb(object):

    def __init__(self):
        myclient = pymongo.MongoClient('mongodb://localhost:27018/')
        mydb = myclient['arxiv']
        self.mycol = mydb["paper_info"]

    def find_one_by_id(self,id):
        if self.mycol != None and id != None:
            return self.mycol.find_one({'id':id})
        else:
            print('col is null or id is null')

    def insert_one(self,item):
        if self.mycol != None and item != None:
            self.mycol.insert_one(item)
        else:
            print('col is null or item is null')