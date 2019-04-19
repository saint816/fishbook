# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     book
   Description :  表单校验
   Author :       pengsheng
   date：          2019-04-19
-------------------------------------------------
"""
from wtforms import Form, StringField, IntegerField
from wtforms.validators import Length, NumberRange, DataRequired


class SearchForm(Form):
    q = StringField(validators=[DataRequired(message='字段q是必录项'), Length(min=1, max=30, message='字段q格式不正确')])
    page = IntegerField(validators=[NumberRange(min=1, max=99)], default=1)