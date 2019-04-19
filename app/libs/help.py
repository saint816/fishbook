# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     help
   Description :  常用工具
   Author :       pengsheng
   date：          2019-04-18
-------------------------------------------------
"""


def is_isbn_or_key(word):
    """
    判断是关键字还是isbn编号
    :param word:
    :return:
    """
    # 13位的isbn
    isbn_or_key = 'key'
    if len(word) == 13 and word.isdigit():
        isbn_or_key = 'isbn'
    # 10个数字和一些-的isbn
    short_word = word.replace('-', '')
    if '-' in word and len(short_word) == 10 and short_word.isdigit:
        isbn_or_key = 'isbn'
    return isbn_or_key
