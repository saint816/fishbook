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
from flask_login import LoginManager

login_manager = LoginManager()


def create_app():
    app = Flask(__name__)  # 默认是statics
    app.config.from_object('app.secure')
    app.config.from_object('app.setting')
    # 把数据库对象挂在到核心对象
    db.init_app(app)
    # 创建数据库表
    db.create_all(app=app)
    # 初始化login_manager
    login_manager.init_app(app)
    login_manager.login_view = 'web.login'
    login_manager.login_message = '请先登录或注册'

    register_blueprint(app)
    return app


def register_blueprint(app):
    # 这里要注意时序问题
    from app.web.book import web
    app.register_blueprint(web)
