# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     fisher
   Description :
   Author :       pengsheng
   date：          2019-04-18
-------------------------------------------------
"""
from flask import Flask, make_response, jsonify
from help import is_isbn_or_key
from yushu_book import YushuBook

app = Flask(__name__)


# 视图函数(Controller) API的难点在于设计
@app.route('/book/search/<q>/<page>')
def search(q, page):
    isbn_or_key = is_isbn_or_key(q)

    if isbn_or_key == 'isbn':
        result = YushuBook.serch_by_isbn(q)
    else:
        result = YushuBook.serch_by_keyword(q)

    return jsonify(result)


app.config.from_object('config')

if __name__ == '__main__':
    # 生产环境使用 nginx转发请求+uwsgi加载模块(加载模块的时候__name__就是模块名,而不是__main__), 不需要flask去启动自带的服务器
    app.run(host='0.0.0.0', debug=app.config['DEBUG'])
