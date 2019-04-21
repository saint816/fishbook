# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     config
   Description :   不要上传到Git, 机密信息
   Author :       pengsheng
   date：          2019-04-18
-------------------------------------------------
"""

DEBUG = True
# 必须要用这个变量, 数据库类型+连接数据库的驱动://用户名:密码
# 支持分布式数据库
SQLALCHEMY_DATABASE_URI = 'mysql+cymysql://root:123@127.0.0.1:8889/fisher'