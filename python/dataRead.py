# -*- coding: utf-8 -*-
# file: dataRead.py
# author: Lyndon

import xlrd
import sys


# 这段代码是用于解决中文报错的问题
reload(sys)
sys.setdefaultencoding("utf-8")


class dataRead(object):
    """初始化读取表"""

    def __init__(self, arg):
        try:
            self.data = xlrd.open_workbook(arg)
        except Exception, e:
            print str(e)

    # 根据名称获取Excel表格中的数据  参数:file：Excel文件路径
    # colnameindex：表头列名所在行的所以，by_name：Sheet1名称
    def excel_table_byname(self):
        colnameindex = 0
        by_name = u'Sheet1'
        table = self.data.sheet_by_name(by_name)
        nrows = table.nrows  # 行数
        colnames = table.row_values(colnameindex)  # 某一行数据
        list = []
        for rownum in range(1, nrows):
            row = table.row_values(rownum)
            if row:
                app = {}
                for i in range(len(colnames)):
                    app[colnames[i]] = row[i]
                list.append(app)
        return list


if __name__ == "__main__":
    # filename = u'data.xls'
    # tables = dataRead(filename)
    # data = tables.excel_table_byname()
    # print type(data)
    # for row in data:
    #     print row['mobile']
    #     print row['name']
    #     print row['address']
    #     print row['email']
    pass
