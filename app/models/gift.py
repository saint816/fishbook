from flask import current_app
from sqlalchemy import Column, String, Integer, ForeignKey, Boolean, desc
from sqlalchemy.orm import relationship
from app.models.base import Base
from app.spider.yushu_book import YushuBook


class Gift(Base):
    __tablename__ = 'gift'

    id = Column(Integer, primary_key=True)
    uid = Column(Integer, ForeignKey('user.id'), nullable=False)
    user = relationship('User')
    isbn = Column(String(13))
    launched = Column(Boolean, default=False)

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
