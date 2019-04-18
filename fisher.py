# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     fisher
   Description :
   Author :       pengsheng
   date：          2019-04-18
-------------------------------------------------
"""
from flask import Flask, make_response

app = Flask(__name__)


# 视图函数(Controller)
@app.route('/hello')
def hello():
    # 视图函数的返回, 和普通函数并不同, 额外返回如下内容
    # status code:
    # content-type = text/html 默认格式
    # http headers
    # 返回其实是Response对象
    headers = {
        'content-type': 'text/plain',
        'location': 'https://www.baidu.com'
    }
    # 状态码不会影响展示的内容
    # response = make_response('<html></html>', 301)
    # response.headers = headers
    # return response
    return '<html></html>', 301, headers
# 导入模块路径; 配置模块;
# !!! 这样导入,Flask要求变量必须全部大写
app.config.from_object('config')
# 四个0代表接受外网访问

# 在生产环境,所有模块都是使用uwsgi去加载模块进行启动正式服务器. 而不是`python modle.py`的方式; 这样写保证了在生产环境,Flask自带的服务不会被启动
if __name__ == '__main__':
    # 生产环境使用 nginx转发请求+uwsgi加载模块(加载模块的时候__name__就是模块名,而不是__main__), 不需要flask去启动自带的服务器
    app.run(host='0.0.0.0', debug=app.config['DEBUG'])
