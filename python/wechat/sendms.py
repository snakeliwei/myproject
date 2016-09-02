# -*- coding: utf-8 -*-
# file: sendms.py
# author: Lyndon

import requests
import json
import sys


class weChatMs(object):

    def __init__(self):
        pqyload = {
            'corpid': 'wx906d385179a4f813',
            'corpsecret': 'pKT_A3rm-RTaKOJId5p2BzpT5MqaqHm0yuCv8oDv-R0o6vmYXXLhNKejT4YMejDV'}
        res = requests.get(
            'https://qyapi.weixin.qq.com/cgi-bin/gettoken', params=pqyload)
        self.token = res.json()['access_token']

    def sendMessage(self, content):
        '''发送消息接口'''
        url = 'https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token=' + self.token

        data = {
            "touser": "@all",
            "toparty": "",
            "totag": "",
            "msgtype": "text",
            "agentid": "2",
            "text": {
                "content": ""
            },
            "safe": "0"
        }

        data['text']['content'] = content

        req = requests.post(url, data=json.dumps(data))

        if req.json()['errcode'] == 0:
            print "Send sucess!!"
        else:
            print req.json()['errmsg']


if __name__ == '__main__':
    message = sys.argv[1]
    wechat = weChatMs()
    wechat.sendMessage(message)
