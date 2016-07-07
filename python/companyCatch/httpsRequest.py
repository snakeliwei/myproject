# -*- coding: utf-8 -*-
# file: httpspost.py
# author: Lyndon

import requests
import uuid


class dataPost(object):

    def __init__(self):
        self.baseUrl = ''

    def setSiteInfo(self, url):
        '''设置用户登录信息'''
        self.baseUrl = url

    def dataQuerySite(self, imei):
        '''取得反扒验证'''
        url = self.baseUrl + '/QuerySite'
        params = {}
        params['IMEI'] = imei
        params['OS'] = 'iPhone'
        headers = {}
        headers[
            'User-Agent'] = 'Mozilla/5.0 (Ios;9.3.1;iPhone;iPhone);Version/1.5.1;ISN_GSXT'
        headers['Cookie'] = imei
        req = requests.post(url, params=params, headers=headers, verify=False)

        return req.json()

    def dataQueryAutoname(self, areacode, q, imei):
        '''获取企业简介'''
        url = self.baseUrl + '/QueryAutoName?'
        params = {}
        params['AreaCode'] = areacode
        params['Size'] = '20'
        params['Q'] = q
        headers = {}
        headers[
            'User-Agent'] = 'Mozilla/5.0 (Ios;9.3.1;iPhone;iPhone);Version/1.5.1;ISN_GSXT'
        headers['Cookie'] = imei
        req = requests.post(url, params=params, headers=headers, verify=False)

        return req.json()

    def dataQuerySummary(self, areacode, q, imei):
        '''获取企业简介'''
        url = self.baseUrl + '/QuerySummary'
        params = {}
        params['AreaCode'] = areacode
        params['Limit'] = '50'
        params['Page'] = '1'
        params['Q'] = q
        headers = {}
        headers[
            'User-Agent'] = 'Mozilla/5.0 (Ios;9.3.1;iPhone;iPhone);Version/1.5.1;ISN_GSXT'
        headers['Cookie'] = imei
        req = requests.post(url, params=params, headers=headers, verify=False)

        return req.json()

    def dataQueryGSInfo(self, areacode, regid, regno, q, imei):
        '''获取企业详情'''
        url = self.baseUrl + '/QueryGSInfo'
        params = {}
        params['AreaCode'] = areacode
        params['EntId'] = regid
        params['EntNo'] = regno
        params['Info'] = 'All'
        params['Limit'] = '50'
        params['Page'] = '1'
        params['Q'] = q
        headers = {}
        headers[
            'User-Agent'] = 'Mozilla/5.0 (Ios;9.3.1;iPhone;iPhone);Version/1.5.1;ISN_GSXT'
        headers['Cookie'] = imei
        req = requests.post(url, params=params, headers=headers, verify=False)
        return req.json()

if __name__ == '__main__':
    # file_object = open('keywords.txt')
    # try:
    #     keywords = file_object.readlines()
    # finally:
    #     file_object.close()
    dataRead = dataPost()
    url = 'https://120.52.121.75:8443'
    dataRead.setSiteInfo(url)
    imei = str(uuid.uuid1()).upper()
    zoneRec = dataRead.dataQuerySite(imei)
    print zoneRec

