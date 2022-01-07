from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_user, logout_user, login_required
from werkzeug.security import generate_password_hash, check_password_hash
from .models import User, Bio
from . import db

auth = Blueprint('auth', __name__)


# signup section
@auth.route('/signup', methods=['POST', 'GET'])
def signup_post():
    username = request.form.get('username')
    password = request.form.get('password')
    confirm_password = request.form.get('confirm_password')

    user = User.query.filter_by(username=username).first()

    if password != confirm_password:
        print("password wrong")
        flash('password are not the same, try again')
        return redirect(url_for('auth.signup'))

    if user:
        flash("User already exist")
        return redirect(url_for('auth.signup'))

    new_user = User(username=username,
                    password=generate_password_hash(password, method='sha256'))

    db.session.add(new_user)
    db.session.commit()

    login_user(new_user)
    return redirect(url_for('main.welcome'))


# login section
@auth.route('/login')
def login():
    error = 0
    return "create login page here"


@auth.route('/login', methods=['POST', 'GET'])
def login_post():
    username = request.form.get('username')
    password = request.form.get('password')

    user = User.query.filter_by(username=username).first()

    if not user or not check_password_hash(user.password, password):
        flash('Wrong password or User. Please check your login details and try again.')
        return redirect(url_for('auth.login'))

    login_user(user)
    return redirect(url_for('main.profile'))


# main section
@auth.route('/')
def signup():
    return render_template("index.html")


# logout
@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return render_template("index.html")
