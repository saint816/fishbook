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
from flask import jsonify

# 创建蓝图

# 视图函数 => 注册到蓝图 => 蓝图注册到flask核心对象(App)
@web.route('/book/search/<q>/<page>')
def search(q, page):
    isbn_or_key = is_isbn_or_key(q)

    if isbn_or_key == 'isbn':
        result = YushuBook.serch_by_isbn(q)
    else:
        result = YushuBook.serch_by_keyword(q)

    return jsonify(result)
