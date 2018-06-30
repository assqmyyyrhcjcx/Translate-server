#encoding: utf-8

from exts import db
from datetime import datetime

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(20), nullable=False, unique=True)
    password = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(30), nullable=False, unique=True)
    # now()获取的是服务器第一次运行的时间
    # now就是每次创建一个模型的时候，获取当前时间
    createtime = db.Column(db.DateTime, default=datetime.now())

class Language(db.Model):
    __tablename__ = 'language'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(20), nullable=False)
    alias = db.Column(db.String(20), nullable=False)