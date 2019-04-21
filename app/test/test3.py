# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     test3
   Description :   Local Stack对栈的操作
   Author :       pengsheng
   date：          2019-04-21
-------------------------------------------------
"""
from werkzeug.local import LocalStack

s = LocalStack()
s.push(1)
print(s.top)
print(s.pop())
print(s.top)

s.push(1)
s.push(2)
print(s.top)
print(s.top)
print(s.pop())
print(s.top)

