# -*- coding: utf-8 -*-
# file: login.py
# author: Lyndon

import sys
import urllib2
import cookielib
import json

# 这段代码是用于解决中文报错的问题
reload(sys)
sys.setdefaultencoding("utf8")

# 登录giant



class Login(object):

    def __init__(self):
        self.name = ''
        self.pwd = ''
        self.token = ''
        self.spaceId = ''
        self.baseUrl = ''

        self.cj = cookielib.LWPCookieJar()
        self.opener = urllib2.build_opener(
            urllib2.HTTPCookieProcessor(self.cj))
        urllib2.install_opener(self.opener)

    def setLoginInfo(self, url, username, password):
        '''设置用户登录信息'''
        self.name = username
        self.pwd = password
        self.baseUrl = url

    def login(self):
        '''登录网站'''
        loginurl = self.baseUrl + '/api/v1/login'
        loginparams = 'login=' + self.name + '&' + 'password=' + self.pwd
        headers = {
            'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 9_3 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Mobile/13E234 Html5Plus/1.0'}
        req = urllib2.Request(loginurl, loginparams, headers)
        response = urllib2.urlopen(req)
        self.operate = self.opener.open(req)
        thePage = response.read()
        self.token = str(json.loads(thePage)['authentication_token'])
        return self.token

    def getSpaceList(self):
        '''获取空间列表'''
        getUrl = url + '/api/v1/spaces?token=' + self.token
        req = urllib2.urlopen(getUrl)
        s = req.read()
        return s


if __name__ == '__main__':
    userlogin = Login()
    url = 'http://yunlu.iok.la:81'
    username = '13036134958'
    password = '87894248'
    userlogin.setLoginInfo(url, username, password)
    token = userlogin.login()
    print token
    print type(token)
    space = userlogin.getSpaceList()
    print space
    print type(space)
