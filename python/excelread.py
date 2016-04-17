# -*- coding: utf-8 -*-
# file: pgconn.py
# author: Lyndon

import xlrd
import sys
import json


# 这段代码是用于解决中文报错的问题
reload(sys)
sys.setdefaultencoding("utf-8")


def open_excel(file='data.xls'):
    try:
        data = xlrd.open_workbook(file)
        return data
    except Exception, e:
        print str(e)


# 根据名称获取Excel表格中的数据  参数:file：Excel文件路径
# colnameindex：表头列名所在行的所以，by_name：Sheet1名称
def excel_table_byname(file='data.xls', colnameindex=1, by_name=u'Sheet1'):
    data = open_excel(file)
    table = data.sheet_by_name(by_name)
    nrows = table.nrows  # 行数
    colnames = table.row_values(colnameindex)  # 某一行数据
    list = []
    for rownum in range(2, nrows):
        row = table.row_values(rownum)
        if row:
            app = {}
            for i in range(len(colnames)):
                app[colnames[i]] = row[i]
            list.append(app)
    return list


def main():
    tables = excel_table_byname()
    for row in tables:
        data = json.loads(json.dumps(row, ensure_ascii=False))['mobile']
        print data

if __name__ == "__main__":
    main()
