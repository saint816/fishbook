# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     test1
   Description :  多线程实现
   Author :       pengsheng
   date：          2019-04-20
-------------------------------------------------
"""

import threading

def worker():
    print('i am thread')
    t = threading.current_thread()
    print(t.getName())

new_thread = threading.Thread(target=worker, name='new_thread')
new_thread.start()

# 更加充分利用CPU的性能优势(线程执行是异步的)
# 异步编程多用于解决性能问题,一般问题能够用同步就用同步

t = threading.current_thread()
print(t.getName())