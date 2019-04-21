# class BaseMixin(object):
#     def __getitem__(self, key):
#         return getattr(self, key)
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, SmallInteger, Integer

db = SQLAlchemy()


class Base(db.Model):
    __abstract__ = True
    create_time = Column('create_time', Integer)
    # 是否被物理删除
    status = Column(SmallInteger, default=1)
