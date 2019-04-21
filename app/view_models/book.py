# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     book
   Description :
   Author :       pengsheng
   date：          2019-04-21
-------------------------------------------------
"""


class BookViewModel(object):
    @classmethod
    def package_single(cls, data, keyword):
        returnd = {
            'books': [],
            'total': 0,
            'keyword': keyword
        }

        if data:
            returnd['total'] = 1
            returnd['books'] = [cls.__cut_book_data(data)]
        return returnd

    @classmethod
    def package_collection(cls, data, keyword):
        returnd = {
            'books': [],
            'total': 0,
            'keyword': keyword
        }
        if data:
            returnd['total'] = data['total']
            # 列表推导式
            returnd['books'] = [cls.__cut_book_data(book) for book in data['books']]
        return returnd

    @classmethod
    def __cut_book_data(cls, data):
        book = {
            'title': data['title'],
            'publisher': data['publisher'],
            'pages': data['pages'] or '无',
            'author': ','.join(data['author']),
            'price': data['price'],
            'summary': data['summary'] or '无',
            'image': data['image'],
        }
        return book
