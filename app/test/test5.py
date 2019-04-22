# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     test5
   Description :
   Author :       pengsheng
   date：          2019-04-22
-------------------------------------------------
"""
from contextlib import contextmanager


@contextmanager
def book_name():
    print('《', end='')
    yield
    print('》', end='')

with book_name():
    print('思考快与慢', end='')
    # 《思考快与慢》