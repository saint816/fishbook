from flask import flash, redirect, url_for
from flask_login import current_user

from app import db
from app.models import Wish
from app.web.blue_print import web

__author__ = '七月'


@web.route('/my/wish')
def my_wish():
    pass


@web.route('/wish/book/<isbn>')
def save_to_wish(isbn):
    if current_user.can_saveto_list(isbn):
        with db.auto_commit():
            wish = Wish()
            wish.isbn = isbn
            wish.uid = current_user.id
            db.session.add(wish)
    else:
        flash('这本书已存在于你的心愿单或者赠送清单,请勿重复添加')
    # 视图函数必须要返回值
    return redirect(url_for('web.book_detail', isbn=isbn))
    pass




@web.route('/satisfy/wish/<int:wid>')
def satisfy_wish(wid):
    pass


@web.route('/wish/book/<isbn>/redraw')
def redraw_from_wish(isbn):
    pass
