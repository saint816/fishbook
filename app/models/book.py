# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     book
   Description : 模型层
   Author :       pengsheng
   date：          2019-04-19
-------------------------------------------------
"""

# sqlalchemy
# Flask_SQLAlchemy 对 sqlalchemy进行封装
from sqlalchemy import Column, String, Integer

from app.models.base import Base


class Book(Base):
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(50), nullable=False)
    _author = Column('author', String(30), default='未名')
    binding = Column(String(20))
    publisher = Column(String(50))
    price = Column(String(20))
    pages = Column(Integer)
    pubdate = Column(String(20))
    isbn = Column(String(15), nullable=False, unique=True)
    summary = Column(String(1000))
    image = Column(String(50))

    # ORM 和 Code First
    # ORM 范围更广,涉及到表的各种操作