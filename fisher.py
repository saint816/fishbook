# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     fisher
   Description :
   Author :       pengsheng
   date：          2019-04-18
-------------------------------------------------
"""
from app import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=app.config['DEBUG'])
