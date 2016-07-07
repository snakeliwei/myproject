# -*- coding: utf-8 -*-
# file: dataCatch.py
# author: Lyndon

import time
import sys
import json
import uuid
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
    for keyword in keywords:
        imei = str(uuid.uuid1()).upper()
        zoneRec = dataRead.dataQuerySite(imei)
        for zone in zoneRec.keys():
            names = dataRead.dataQueryAutoname(zone, keyword, imei)
            print json.dumps(names, ensure_ascii=False)
            if (names):
                for name in names:
                    record = dataRead.dataQuerySummary(zone, name, imei)
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
