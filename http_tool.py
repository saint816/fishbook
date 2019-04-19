# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     http
   Description :
   Author :       pengsheng
   date：          2019-04-18
-------------------------------------------------
"""
import requests

# Python2 最好写object 代表新式类
class HTTP(object):
    @staticmethod
    def get(url, return_json=True):
        pass
        '''
        使用requests发送get请求
        '''
        r = requests.get(url)
        if r.status_code != 200:
            return {} if return_json else ''
        return r.json() if return_json else r.text
