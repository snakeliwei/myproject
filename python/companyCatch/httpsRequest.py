# -*- coding: utf-8 -*-
# file: httpspost.py
# author: Lyndon

import requests


class dataPost(object):

    def __init__(self):
        self.baseUrl = ''

    def setSiteInfo(self, url):
        '''设置用户登录信息'''
        self.baseUrl = url

    def dataQuerySite(self):
        '''取得反扒验证'''
        url = self.baseUrl + '/QuerySite'
        params = {}
        params['IMEI'] = 'B0494235-B0DB-407C-8B67-6EEF6C49343D'
        params['OS'] = 'iPhone'
        headers = {'User-Agent': 'Mozilla/5.0 (Ios;9.3.1;iPhone;iPhone);Version/1.5.1;ISN_GSXT',
                   'Cookie': 'B0494235-B0DB-407C-8B67-6EEF6C49343D'}
        req = requests.post(url, params=params, headers=headers, verify=False)

        return req.json()

    def dataQueryAutoname(self, areacode, q):
        '''获取企业简介'''
        url = self.baseUrl + '/QueryAutoName?'
        params = {}
        params['AreaCode'] = areacode
        params['Size'] = '20'
        params['Q'] = q
        headers = {'User-Agent': 'Mozilla/5.0 (Ios;9.3.1;iPhone;iPhone);Version/1.4.0;ISN_GSXT',
                   'Cookie': 'B0494235-B0DB-407C-8B67-6EEF6C49343D'}
        req = requests.post(url, params=params, headers=headers, verify=False)

        return req.json()

    def dataQuerySummary(self, areacode, q):
        '''获取企业简介'''
        url = self.baseUrl + '/QuerySummary'
        params = {}
        params['AreaCode'] = areacode
        params['Limit'] = '50'
        params['Page'] = '1'
        params['Q'] = q
        headers = {'User-Agent': 'Mozilla/5.0 (Ios;9.3.1;iPhone;iPhone);Version/1.4.0;ISN_GSXT',
                   'Cookie': 'B0494235-B0DB-407C-8B67-6EEF6C49343D'}
        req = requests.post(url, params=params, headers=headers, verify=False)

        return req.json()

    def dataQueryGSInfo(self, areacode, regid, regno, q):
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
        headers = {'User-Agent': 'Mozilla/5.0 (Ios;9.3.1;iPhone;iPhone);Version/1.4.0;ISN_GSXT',
                   'Cookie': 'B0494235-B0DB-407C-8B67-6EEF6C49343D'}
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
    zoneRec = dataRead.dataQuerySite()
    for zone in zoneRec.keys():
        for keyword in keywords:
            names = dataRead.dataQueryAutoname(zone, keyword)
            print json.dumps(names, ensure_ascii=False)
            for name in names:
                record = dataRead.dataQuerySummary(zone, name)
                print json.dumps(record['RESULT'], ensure_ascii=False)
                detail = dataRead.dataQueryGSInfo(
                    zone, record['ID'], record['REGNO'], name)
                datasaver.dataInsert(record['RESULT'])
