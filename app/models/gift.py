from flask import current_app
from sqlalchemy import Column, String, Integer, ForeignKey, Boolean, desc, func
from sqlalchemy.orm import relationship

from app.models.wish import Wish
from app.models.base import Base, db
from app.spider.yushu_book import YushuBook


class Gift(Base):
    __tablename__ = 'gift'

    id = Column(Integer, primary_key=True)
    uid = Column(Integer, ForeignKey('user.id'), nullable=False)
    user = relationship('User')
    isbn = Column(String(13))
    launched = Column(Boolean, default=False)

    @classmethod
    def get_user_gifts(cls, uid):
        gifts = Gift.query.filter_by(uid=uid, launched=False).order_by(desc(Gift.create_time)).all()
        return gifts

    @classmethod
    def get_wish_counts(cls, isbn_list):
        # 到Wish表中检索出某个礼物的心愿数量
        # 分组统计, 得到的数据结构[(1, '2882928989'), (2, '88288829393)]
        # db.session.query适合跨表查询,或者比较复杂的查询
        count_list = db.session.query(func.count(Wish.id), Wish.isbn).filter(Wish.launched == False,
                                                                             Wish.isbn.in_(isbn_list),
                                                                             Wish.status == 1).group_by(Wish.isbn).all()

        return [{'count': w[0], 'isbn': w[1]} for w in count_list]

    @property
    def book(self):
        yushu_book = YushuBook()
        yushu_book.serch_by_isbn(self.isbn)
        return yushu_book.first

    @classmethod
    def recent(cls):
        # 注意:
        #   1. distinct: 去重,必须要用到group_by才行;
        #   2. limit要写在最后面
        #   3. 这里要注意解决SQL group_by的报错 https://stackoverflow.com/questions/23921117/disable-only-full-group-by
        recent_gift = Gift.query.filter_by(
            launched=False).group_by(
            Gift.isbn).order_by(
            desc(Gift.create_time)).limit(
            current_app.config['RECENT_BOOK_COUNT']).distinct().all()
        return recent_gift
