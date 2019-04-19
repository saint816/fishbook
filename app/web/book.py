# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     book
   Description :   视图函数
   Author :       pengsheng
   date：          2019-04-18
-------------------------------------------------
"""

# 视图函数(Controller) API的难点在于设计
from app.web.blue_print import web
from help import is_isbn_or_key
from yushu_book import YushuBook
from flask import jsonify, request


# 视图函数 => 注册到蓝图 => 蓝图注册到flask核心对象(App)
@web.route('/book/search')
def search():
    """
    Request Response Http请求头 POST内容
    """
    # 注意, request是通过http请求触发的才会有正确的值;
    q = request.args['q']
    page = request.args['page']

    isbn_or_key = is_isbn_or_key(q)

    if isbn_or_key == 'isbn':
        result = YushuBook.serch_by_isbn(q)
    else:
        result = YushuBook.serch_by_keyword(q)

    return jsonify(result)
