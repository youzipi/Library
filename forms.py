# -*- coding: utf-8 -*- 
# __author__ = 'youzipi'
from flask_wtf import Form
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Email
class searchForm(Form):
    keyword = StringField('keyword',validators=[DataRequired])