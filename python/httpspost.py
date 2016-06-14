# -*- coding: utf-8 -*-
# file: login.py
# author: Lyndon

import urllib
import urllib2
import sys
import ssl
import json

# 这段代码是用于解决中文报错的问题
reload(sys)
sys.setdefaultencoding("utf8")

ssl._create_default_https_context = ssl._create_unverified_context


class dataPost(object):

    def __init__(self):
        self.baseUrl = ''

    def setSiteInfo(self, url):
        '''设置用户登录信息'''
        self.baseUrl = url

    def dataQuerySummary(self):
        '''获取企业简介'''
        url = self.baseUrl + '/QuerySummary'
        params = {}
        params['AreaCode'] = '420000'
        params['Limit'] = '50'
        params['Page'] = '1'
        params['Q'] = '武汉百石通达'
        headers = {
            "User-Agent": "Mozilla/5.0 (Ios;9.3.2;iPhone;iPhone);Version/1.4.0;ISN_GSXT",
            "Cookie": "B0494235-B0DB-407C-8B67-6EEF6C49343D"}
        postData = urllib.urlencode(params)
        req = urllib2.Request(url, postData, headers)
        response = urllib2.urlopen(req)
        thePage = response.read()
        return thePage

    def dataQueryGSInfo(self):
        '''获取企业详情'''
        url = self.baseUrl + '/QueryGSInfo'
        params = {}
        params['AreaCode'] = '420000'
        params['EntId'] = '420000000010030385'
        params['EntNo'] = '420115600365437'
        params['Info'] = 'All'
        params['Limit'] = '50'
        params['Page'] = '1'
        params['Q'] = '武汉百石通达'
        headers = {
            "User-Agent": "Mozilla/5.0 (Ios;9.3.2;iPhone;iPhone);Version/1.4.0;ISN_GSXT",
            "Cookie": "B0494235-B0DB-407C-8B67-6EEF6C49343D"}
        postData = urllib.urlencode(params)
        req = urllib2.Request(url, postData, headers)
        response = urllib2.urlopen(req)
        thePage = response.read()
        return thePage


if __name__ == '__main__':
    dataRead = dataPost()
    url = 'https://120.52.121.75:8443'
    dataRead.setSiteInfo(url)
    record = dataRead.dataQuerySummary()
    detail = dataRead.dataQueryGSInfo()
    print record
    print detail
    # print token
    # print type(token)
    # space = userlogin.getSpaceList()
    # data = json.loads(space)
    # print data
    # print type(data)
    # pass
