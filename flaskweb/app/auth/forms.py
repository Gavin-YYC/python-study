# coding=utf-8

from flask_wtf import FlaskForm
from wtforms import ValidationError, StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import Required, Length, Email, EqualTo
from ..models import User

class LoginForm( FlaskForm ):
    email = StringField('Email', validators=[Required(), Length(1, 64), Email()])
    password = PasswordField('Password', validators=[Required()])
    remember_me = BooleanField('Keep me logged in')
    submit = SubmitField('Log In')

class RegistrationForm( FlaskForm ):
    email = StringField('Email', validators=[Required(), Length(1, 64), Email()])
    username = StringField('Username', validators=[Required(), Length(1, 64)])
    password = PasswordField('Password', validators=[Required(), EqualTo('password2', message="Passwords must match.")])
    password2 = PasswordField('Confirm password', validators=[Required()])
    submit = SubmitField('Register')

    # 如果方法为validate_开头，后面跟着字段名
    # 则在提交的时候一起进行验证
    def validate_email( self, field ):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Email already registered.')

    def validate_username( self, field ):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('username already in use.')
