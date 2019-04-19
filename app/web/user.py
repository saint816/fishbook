# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     user
   Description :
   Author :       pengsheng
   date：          2019-04-19
-------------------------------------------------
"""

from app.web.blue_print import web

@web.route('/login')
def login():
    return '登录页面'