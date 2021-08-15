from flask import Blueprint, render_template, request

users = Blueprint('users', __name__)


@users.route('/')
def home():
    return 'user.home'


@users.route('/login')
def login():
    return render_template('login.html', request=request)
