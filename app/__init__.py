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
from app.web.book import web

def create_app():
    app = Flask(__name__)
    app.config.from_object('config')
    register_blueprint(app)
    return app

def register_blueprint(app):
    app.register_blueprint(web)