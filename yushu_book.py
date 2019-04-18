# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     yushu_book
   Description :
   Author :       pengsheng
   date：          2019-04-18
-------------------------------------------------
"""

from http import HTTP


class YushuBook:
    isbn_url = 'http://t.yushu.im/v2/book/isbn/{}'
    keyword_url = 'http://t.yushu.im/v2/book/search?q={}&count={}&start={}'

    @classmethod
    def serch_by_isbn(cls, isbn):
        url = cls.isbn_url.format(isbn)
        result = HTTP.get(url)
        return result

    @classmethod
    def serch_by_keyword(cls, keyword, count=15, start=0):
        url = cls.keyword_url.format(keyword, count, start)
        result = HTTP.get(url)
        return result
