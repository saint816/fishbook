# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     test4
   Description :   LocalStack线程隔离特性
   Author :       pengsheng
   date：          2019-04-21
-------------------------------------------------
"""
import threading
import time

from werkzeug.local import LocalStack

my_stack = LocalStack()
my_stack.push(1)
print('main after push: ' + str(my_stack.top))


def worker():
    print('child thread before push: ' + str(my_stack.top))
    my_stack.push(2)
    print('child thread after push: ' + str(my_stack.top))


child_thread = threading.Thread(target=worker, name='child_thread')
child_thread.start()
time.sleep(1)

print('finally value at main thread: ' + str(my_stack.top))
