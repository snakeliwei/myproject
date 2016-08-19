# -*- coding: utf-8 -*-
# file: restful.py
# author: Lyndon
#

from flask import Flask, jsonify, abort
from dbSave import datasave

app = Flask(__name__)
datasaver = datasave()
companys = datasaver.dataRead()


@app.route('/v1.0/companys/<string:company_id>', methods=['GET'])
def get_company(company_id):
    company = filter(lambda t: t['ID'] == company_id, companys)
    if len(company) == 0:
        abort(404)
    return jsonify({'companys': company[0]})

if __name__ == '__main__':
    app.run(debug=True)
