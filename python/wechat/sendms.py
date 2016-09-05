# -*- coding: utf-8 -*-
# file: sendms.py
# author: Lyndon

import requests
import json
import sys
import yaml


class weChatMs(object):

    def __init__(self):

        try:
            data = open('config.yml')
        except Exception, e:
            print str(e)

        pqyload = yaml.load(data)['wechat']
        data.close()

        res = requests.get(
            'https://qyapi.weixin.qq.com/cgi-bin/gettoken', params=pqyload)
        if ('access_token' in res.json()):
            self.token = res.json()['access_token']
        else:
            print res.json()

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
