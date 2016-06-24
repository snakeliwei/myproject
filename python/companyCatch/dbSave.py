# -*- coding: utf-8 -*-
# file: dbSave.py
# author: Lyndon

import json
from pymongo import MongoClient


class datasave(object):

    def __init__(self):
        self.client = MongoClient('192.168.99.100', 27017)
        self.db = self.client.companyinfo

    def setLoginInfo(self, user, key):
        ''''''
        self.user = user
        self.password = key

    def dataInsert(self, data):
        '''插入数据'''
        if (data):
            posts = self.db.posts
            posts.insert(data)
        else:
            print "Data is empty!!!"

    def dataRead(self):
        '''读取数据'''
        records = []
        posts = self.db.posts
        for post in posts.find():
            post.pop('_id')
            records.append(post)
        return records

if __name__ == '__main__':
    datasaver = datasave()
    # # datasaver.dataInsert(data)
    records = datasaver.dataRead()
    print json.dumps(records, ensure_ascii=False)


