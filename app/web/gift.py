from flask import current_app, flash, redirect, url_for
from flask_login import login_required, current_user

from app.models.base import db
from app.models.gift import Gift
from app.web.blue_print import web

__author__ = '七月'


@web.route('/my/gifts')
@login_required
def my_gifts():
    return 'MyGift'


@web.route('/gifts/book/<isbn>')
@login_required
def save_to_gifts(isbn):
    if current_user.can_saveto_list(isbn):
        with db.auto_commit():
            gift = Gift()
            gift.isbn = isbn
            current_user.beans += current_app.config['BEANS_UPLOAD_ONE_BOOK']
            gift.uid = current_user.id
            db.session.add(gift)
    else:
        flash('这本书已存在于你的心愿单或者赠送清单,请勿重复添加')
    # 视图函数必须要返回值
    return redirect(url_for('web.book_detail', isbn=isbn))


@web.route('/gifts/<gid>/redraw')
def redraw_from_gifts(gid):
    pass
