#!usr/bin/env python  
#-*- coding:utf-8 _*-  
""" 
@author: hiyoung 
@file: main
@time: 2019/8/29:
"""
import os
import sys
from scrapy.cmdline import execute

if __name__ == '__main__':
    sys.path.append(os.path.abspath(__file__))
    execute(['scrapy','crawl','ArxivSpider'])