# -*- coding: utf-8 -*-
# file: test.py
# author: Lyndon

from userInsert import userInsert
from dataRead import dataRead
from login import Login
from getfilepath import getPath


if __name__ == "__main__":
    filename = u'data.xls'
    tables = dataRead(filename)
    data = tables.excel_table_byname()
    # userdata = userInsert()
    # userdata.insertData(data)
    userlogin = Login()
    url1 = 'http://api.yunlu6.com'
    url2 = 'http://api.360stones.com'
    password = '88888888'
    for user in data:
        userlogin.setLoginInfo(url1, url2, user['mobile'], password)
        token = userlogin.login()
        print token
        userlogin.createCoSpace(user)
        # filespath = u"D:\\data\\公司图片\\" + user['company']
        # path = getPath(filespath)
        # filelist = path.getFileList()
        # if filelist:
        #     print filelist
        #     userlogin.upLoader(filelist)
        #     photoList = userlogin.getPhotoList()
        #     teamId = userlogin.getTeamId()[0]
        #     userlogin.createDoc(teamId, photoList)
