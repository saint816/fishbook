from sqlalchemy import Column
from sqlalchemy import String, Boolean
from sqlalchemy import Integer, Float
from werkzeug.security import generate_password_hash, check_password_hash

from app.libs.help import is_isbn_or_key
from app.models.base import Base

# 必须继承,因为里面需要混入很多属性
from flask_login import UserMixin

from app import login_manager
from app.models.gift import Gift
from app.models.wish import Wish
from app.spider.yushu_book import YushuBook


class User(Base, UserMixin):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    nickname = Column(String(24), nullable=False)
    phone_number = Column(String(18), unique=True)
    _password = Column('password', String(128), nullable=False)  # 属性名与表的字段名不一致的话这样处理就好
    email = Column(String(50), unique=True, nullable=False)
    confirmed = Column(Boolean, default=False)
    beans = Column(Float, default=0)
    send_counter = Column(Integer, default=0)
    receive_counter = Column(Integer, default=0)

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, raw_pwd):
        self._password = generate_password_hash(raw_pwd)

    def check_password(self, raw):
        return check_password_hash(self._password, raw)

    def can_saveto_list(self, isbn):
        if is_isbn_or_key(isbn) != 'isbn':
            return False
        yushu_book = YushuBook()
        yushu_book.search_by_isbn(isbn)
        if not yushu_book.first:
            return False

        # 不允许同一用户同时赠送多本相同图书
        gifting = Gift.query.filter_by(uid = self.id, isbn=isbn, launched=False).first

        # 一个用户不能同时成为赠送者和索要者
        wishing = Wish.query.filter_by(uid = self.id, isbn=isbn, launched=False).first

        # 既不在赠送清单,又不在心愿清单才能添加
        if not gifting and not wishing:
            return True
        else:
            return False

    def get_id(self):
        return self.id

# 这个函数把告诉了login_manager哪个是用户模型
@login_manager.user_loader
def get_user(uid):
    return User.query.get(int(uid))
