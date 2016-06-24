# -*- coding: utf-8 -*-
# file: dataCatch.py
# author: Lyndon

import time
import sys
import json
from httpsRequest import dataPost
from dbSave import datasave


# 这段代码是用于解决中文报错的问题
reload(sys)
sys.setdefaultencoding("utf8")


if __name__ == '__main__':

    file_object = open('keywords.txt')
    try:
        keywords = file_object.readlines()
    finally:
        file_object.close()
    print keywords
    datasaver = datasave()
    dataRead = dataPost()
    url = 'https://120.52.121.75:8443'
    dataRead.setSiteInfo(url)
    zoneRec = dataRead.dataQuerySite()
    for zone in zoneRec.keys():
        for keyword in keywords:
            names = dataRead.dataQueryAutoname(zone, keyword)
            print json.dumps(names, ensure_ascii=False)
            if (names):
                for name in names:
                    record = dataRead.dataQuerySummary(zone, name)
                    if (record):
                        print json.dumps(record['RESULT'], ensure_ascii=False)
                        company = record['RESULT']
                        # regid = company['ID']
                        print type(company)
                        # detail = dataRead.dataQueryGSInfo(
                        #     zone, str(company['ID']), str(company['REGNO']), name)
                        # datasaver.dataInsert(detail['RESULT'])
            time.sleep(2)
                    # detail = dataRead.dataQueryGSInfo(
                    #     zone, str(company['ID']), str(company['REGNO']), name)
                    # datasaver.dataInsert(detail['RESULT'])
