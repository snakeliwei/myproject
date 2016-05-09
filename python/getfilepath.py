#!/usr/bin/python
# -*- coding: utf-8 -*-
# file: getfilepath.py
# author: Lyndon

import os
import sys


# 这段代码是用于解决中文报错的问题
reload(sys)
sys.setdefaultencoding("utf8")


class getPath(object):
    """docstring for getPath"""

    def __init__(self, arg):
        super(getPath, self).__init__()
        self.path = arg
        self.filelist = []

    def getFileList(self):
        for i in os.walk(self.path.decode('utf-8')):
            for file in i[2]:
                self.filelist.append(os.path.join(i[0], file))
        return self.filelist

if __name__ == '__main__':
    path = getPath('D:\data\公司图片')
    filelist = path.getFileList()
    print filelist
