# -*- coding: utf-8 -*-
# file: uploader.py
# author: Lyndon

import sys
import uuid
from qiniu import Auth, put_file, etag,
import qiniu.config


# 这段代码是用于解决中文报错的问题
reload(sys)
sys.setdefaultencoding("utf8")


class Uploader(object):

    def __init__(self):
        self.key = str(uuid.uuid1()) + '.png'
        self.token = ''
        self.file = ''

    def fileUpload(self, localfile, token):
        self.file = localfile
        self.token = token
        ret, info = put_file(self.token, self.key, self.file)
        print(info)
