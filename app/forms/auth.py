# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     auth
   Description :
   Author :       pengsheng
   date：          2019-04-21
-------------------------------------------------
"""
from wtforms import StringField, PasswordField, Form
from wtforms.validators import DataRequired, Length, Email, ValidationError

from app.models.user import User


class RegisterForm(Form):
    nickname = StringField('昵称', validators=[DataRequired(), Length(2, 10, message='昵称至少需要两个字符，最多10个字符')])
    password = PasswordField('密码', validators=[DataRequired(), Length(6, 20)])
    email = StringField('邮箱', validators=[DataRequired(), Length(8, 64), Email(message='电子邮箱格式不规范')])

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise  ValidationError('邮件已被注册')

    def validate_nickname(self, field):
        if User.query.filter_by(nickname=field.data).first():
            raise  ValidationError('昵称已被注册')


class LoginForm(Form):
    email = StringField('邮箱', validators=[DataRequired(), Length(8, 64), Email(message='电子邮箱格式不规范')])
    password = PasswordField('密码', validators=[DataRequired(), Length(6, 20)])
