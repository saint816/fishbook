# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     yushu_book
   Description :
   Author :       pengsheng
   date：          2019-04-18
-------------------------------------------------
"""
from flask import current_app

from app.libs.http_tool import HTTP


class YushuBook:
    per_page = 15
    isbn_url = 'http://t.yushu.im/v2/book/isbn/{}'
    keyword_url = 'http://t.yushu.im/v2/book/search?q={}&count={}&start={}'

    @classmethod
    def serch_by_isbn(cls, isbn):
        url = cls.isbn_url.format(isbn)
        result = HTTP.get(url)

        # 缓存数据到本地数据库,不用频繁的去请求API
        # book = query_from_mysql(isbn
        # if book :
        #   return book
        # else
        #  save(result)


        return result

    @classmethod
    def serch_by_keyword(cls, keyword, page=1):
        url = cls.keyword_url.format(keyword, current_app.config['PER_PAGE'], cls.calculate_start(page))
        result = HTTP.get(url)
        return result

    @staticmethod
    def calculate_start(page):
        return (page - 1) * current_app.config['PER_PAGE']
