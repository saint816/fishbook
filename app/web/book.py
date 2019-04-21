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
import json

from app.forms.book import SearchForm
from app.view_models.book import BookCollection, BookViewModel
from app.web.blue_print import web
from app.libs.help import is_isbn_or_key
from app.spider.yushu_book import YushuBook
from flask import jsonify, request, flash, render_template


# 视图函数 => 注册到蓝图 => 蓝图注册到flask核心对象(App)
@web.route('/book/search')
def search():
    """
    Request Response Http请求头 POST内容
    """
    # 注意, request是通过http请求触发的才会有正确的值;
    form = SearchForm(request.args)
    books = BookCollection()

    if form.validate():
        q = form.q.data.strip()  # 去掉前后空格
        page = form.page.data
        isbn_or_key = is_isbn_or_key(q)

        yushu_book = YushuBook()

        if isbn_or_key == 'isbn':
            yushu_book.serch_by_isbn(q)
        else:
            yushu_book.serch_by_keyword(q, page)

        books.fill(yushu_book, q)
        # return json.dumps(books, default=lambda obj: obj.__dict__)
    else:
        flash('搜索关键字格式不合要求,请重新输入')
        # return jsonify(form.errors)

    return render_template('search_result.html', books=books)


@web.route('/book/<isbn>/detail')
def book_detail(isbn):
    yushu_book = YushuBook()
    yushu_book.serch_by_isbn(isbn)
    book = BookViewModel(yushu_book.first)
    return render_template('book_detail.html', book=book, wishes=[], gifts=[])
