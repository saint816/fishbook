# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     __init__
   Description :
   Author :       pengsheng
   date：          2019-04-18
-------------------------------------------------
"""

from flask import Flask

from app.models.base import db
from app.web.book import web


def create_app():
    app = Flask(__name__)  # 默认是statics
    app.config.from_object('app.secure')
    app.config.from_object('app.setting')
    register_blueprint(app)
    # 把数据库对象挂在到核心对象
    db.init_app(app)
    # 创建数据库表
    db.create_all(app=app)
    return app


def register_blueprint(app):
    app.register_blueprint(web)
