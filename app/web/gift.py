from flask import current_app, flash
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
    if current_user.can_saveto_list:
        try:
            gift = Gift()
            gift.isbn = isbn
            # 当前登录的用户id
            current_user.beans += current_app.config['BEANS_UPLOAD_ONE_BOOK']
            gift.uid = current_user.id
            db.session.add(gift)
            db.session.commit()
        except Exception as e:
            db.session.rollback() # 如果数据库操作异常不回滚的话,后续数据库的操作都会失败
            raise e
    else:
        flash('这本书已存在于你的心愿单或者赠送清单,请勿重复添加')


@web.route('/gifts/<gid>/redraw')
def redraw_from_gifts(gid):
    pass
