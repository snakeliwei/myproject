# -*- coding: utf-8 -*-
# file: uploader.py
# author: Lyndon

import sys
from qiniu import Auth, put_file, etag,
import qiniu.config


# 这段代码是用于解决中文报错的问题
reload(sys)
sys.setdefaultencoding("utf8")

key = 'my-python-logo.png'

localfile = './sync/bbb.jpg'

ret, info = put_file(token, key, localfile)
print(info)
