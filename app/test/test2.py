# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     test2
   Description : 使用Local对象进行线程隔离
   Author :       pengsheng
   date：          2019-04-20
-------------------------------------------------
"""
import threading
import time

from werkzeug.local import Local

new_obj = Local()
new_obj.name = '张三'


def worker():
    new_obj.name = '张三风'
    print('new thread name = ' + new_obj.name)


new_thread = threading.Thread(target=worker, name='new thread')
new_thread.start()

time.sleep(1)
print('main thread name = ' + new_obj.name)
