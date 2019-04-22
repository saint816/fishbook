from app.web.blue_print import web


__author__ = '七月'


@web.route('/')
def index():
    return 'Hello Index'


@web.route('/personal')
def personal_center():
    pass
