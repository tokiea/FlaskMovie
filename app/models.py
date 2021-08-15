# !/usr/bin/python3
# -*- coding: utf-8 -*-
from werkzeug.security import generate_password_hash, check_password_hash

from app.exts import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nick = db.Column(db.String(20))
    username = db.Column(db.String(20))  # 用户名
    mobile = db.Column(db.String(20))  # 手机号
    password_hash = db.Column(db.String(128))  # 密码散列值

    def set_password(self, password):  # 用来设置密码的方法，接受密码作为参数
        self.password_hash = generate_password_hash(password)  # 将生成的密码保持到对应字段

    def validate_password(self, password):  # 用于验证密码的方法，接受密码作为参数
        return check_password_hash(self.password_hash, password)  # 返回布尔值


class Role(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20),unique=True)  # 用户  管理员  超级管理员
    permissions = db.Column(db.Integer, commit="权限总值")
    a = 0x02


class Permission():
    # 查看
    # 修改
    # 增加
    # 删除
    pass