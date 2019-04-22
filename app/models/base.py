# class BaseMixin(object):
#     def __getitem__(self, key):
#         return getattr(self, key)
from datetime import datetime

from flask_sqlalchemy import SQLAlchemy as _SQLAlchemy, BaseQuery
from sqlalchemy import Column, SmallInteger, Integer

from contextlib import contextmanager


class SQLAlchemy(_SQLAlchemy):
    @contextmanager
    def auto_commit(self):
        """
        自动处理数据的commit与异常回滚
        """
        try:
            yield
            self.session.commit()
        except Exception as a:
            self.session.rollback()
            raise a


class Query(BaseQuery):
    def filter_by(self, **kwargs):
        if 'status' not in kwargs.keys():
            kwargs['status'] = 1
        super(Query, self).filter_by(**kwargs)


db = SQLAlchemy(query_class=Query)


class Base(db.Model):
    __abstract__ = True
    create_time = Column('create_time', Integer)
    # 此项目没有用到物理删除(指的是数据库删除), 仅仅用这个标志位来标记是否删除了记录
    status = Column(SmallInteger, default=1)

    # 给create_time赋值
    def __init__(self):
        self.create_time = int(datetime.now().timestamp())

    # 对有key的属性赋值;id不用管,sqlalchemy动态管理;
    def set_attrs(self, attrs):
        for key, value in attrs.items():
            if hasattr(self, key) and key != 'id':
                setattr(self, key, value)

    @property
    def create_datetime(self):
        if self.create_time:
            return datetime.fromtimestamp(self.create_time)
        else:
            return None
