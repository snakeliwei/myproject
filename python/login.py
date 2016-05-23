# -*- coding: utf-8 -*-
# file: login.py
# author: Lyndon

import urllib
import urllib2
import cookielib
import sys
import json
import uuid
from qiniu import Auth, put_file, etag
import qiniu.config


# 这段代码是用于解决中文报错的问题
reload(sys)
sys.setdefaultencoding("utf8")


class Login(object):

    def __init__(self):
        self.name = ''
        self.pwd = ''
        self.token = ''
        self.baseUrl1 = ''
        self.baseUrl2 = ''

        self.cj = cookielib.LWPCookieJar()
        self.opener = urllib2.build_opener(
            urllib2.HTTPCookieProcessor(self.cj))
        urllib2.install_opener(self.opener)

    def setLoginInfo(self, url1, url2, username, password):
        '''设置用户登录信息'''
        self.name = username
        self.pwd = password
        self.baseUrl1 = url1
        self.baseUrl2 = url2

    def login(self):
        '''登录网站'''
        loginurl = self.baseUrl1 + '/api/v1/login'
        loginparams = {}
        loginparams['login'] = self.name
        loginparams['password'] = self.pwd
        headers = {
            'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 9_3 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Mobile/13E234 Html5Plus/1.0'}
        postData = urllib.urlencode(loginparams)
        req = urllib2.Request(loginurl, postData, headers)
        response = urllib2.urlopen(req)
        self.operate = self.opener.open(req)
        thePage = response.read()
        self.token = str(json.loads(thePage)['authentication_token'])
        return self.token

    def getTeamId(self):
        '''获取企业空间id'''
        getUrl = self.baseUrl1 + '/api/v1/spaces?token=' + self.token
        req = urllib2.urlopen(getUrl)
        s = req.read()
        data = json.loads(s)

        def getid(x):
            if x['owner_class'] == 'master':
                return x['organization_id']

        id = map(getid, data)
        return id

    def createCoSpace(self, coData):
        '''创建企业空间'''
        createUrl = self.baseUrl1 + '/api/v1/spaces/organization'
        createParams = {}
        createParams['token'] = self.token
        createParams['name'] = coData['shortname']
        createParams['company'] = coData['company']
        createParams['service_id'] = coData['service_id']
        createParams['address'] = coData['address']
        createParams['email'] = coData['email']
        createParams['website'] = coData['website']
        createParams['mobile'] = coData['mobile']
        if coData['name'] != '':
            createParams['linkman'] = coData['name']
        else:
            createParams['linkman'] = coData['mobile']

        print createParams
        headers = {
            'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 9_3 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Mobile/13E234 Html5Plus/1.0'}
        postData = urllib.urlencode(createParams)
        req = urllib2.Request(createUrl, postData, headers)
        response = urllib2.urlopen(req)
        self.operate = self.opener.open(req)
        thePage = response.read()
        print thePage

    def upLoader(self, filesPath):
        '''上传图片到云库'''
        # 获取云库上传token
        upLoaderUrl = self.baseUrl1 + \
            '/api/v1/upload_token?mode=personal_catalog&id=0&token=' + self.token
        req = urllib2.urlopen(upLoaderUrl)
        data = req.read()
        upLoaderToken = str(json.loads(data)['uptoken'])
        print upLoaderToken
        for file in filesPath:
            key = str(uuid.uuid1()) + '.png'
            ret, info = put_file(upLoaderToken, key, file)
            print(info)

    def getPhotoList(self):
        '''获取云库文件列表'''
        getUrl = self.baseUrl1 + \
            '/api/v1/galleries/0/photos?page=1&per_page=24&token=' + self.token
        req = urllib2.urlopen(getUrl)
        data = req.read()
        photodata = json.loads(data)['photos']

        def getid(x):
            return x['id']

        photolist = map(getid, photodata)
        return photolist

    def createDoc(self, teamId, fileId):
        '''创建公司档'''
        createUrl = self.baseUrl2 + '/api/v1/team/' + str(teamId) + '/archives'
        createParams = {}
        createParams['token'] = self.token
        createParams['name'] = u'公司介绍'
        createParams['type'] = 'other'
        createParams['published'] = 'true'
        createParams['certificate_class_id'] = ''
        filelist = map(str, fileId)
        files = ''
        for file in filelist:
            files = files + '&file_ids[]=' + file

        headers = {
            'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 9_3 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Mobile/13E234 Html5Plus/1.0'}
        postData = urllib.urlencode(createParams) + files

        req = urllib2.Request(createUrl, postData, headers)
        response = urllib2.urlopen(req)
        self.operate = self.opener.open(req)
        thePage = response.read()
        print thePage

if __name__ == '__main__':
    # userlogin = Login()
    # url = 'http://dev.yunlu6.com'
    # username = '13036134958'
    # password = '87894248'
    # userlogin.setLoginInfo(url, username, password)
    # token = userlogin.login()
    # print token
    # print type(token)
    # space = userlogin.getSpaceList()
    # data = json.loads(space)
    # print data
    # print type(data)
    pass
