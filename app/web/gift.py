from flask import current_app, flash, redirect, url_for
from flask_login import login_required, current_user
from sqlalchemy import desc

from app.models.base import db
from app.models.gift import Gift
from app.view_models.gift import MyGifts
from app.web.blue_print import web

__author__ = '七月'


@web.route('/my/gifts')
@login_required
def my_gifts():
    uid = current_user.id
    # 所有礼物
    gifts_of_mine = Gift.query.filter_by(uid=uid, launched=False).group_by(
        Gift.isbn).order_by(
        desc(Gift.create_time)).distinct().all()
    # (isbn: want_count, ...)
    isbn_list = [gift.isbn for gift in gifts_of_mine]

    wish_count_list = Gift.get_wish_counts(isbn_list=isbn_list)
    # view modes 合成数据
    # [{
    #     'wishes_count': count,
    #     'book': BookViewModel(gift.book),
    #     'id': gift.id
    # },
    # ...
    # ]
    view_models = MyGifts(gifts_of_mine, wish_count_list)
    from flask import render_template
    return render_template('my_gifts.html', gifts=view_models.my_gifts)


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
