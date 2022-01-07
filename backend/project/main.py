from flask import Blueprint, render_template
from . import db
from flask_login import login_required, current_user


main = Blueprint('main', __name__)


@main.route('/profile')
@login_required
def profile():
    return render_template('profile.html', name=current_user.username)


@main.route('/welcome')
@login_required
def welcome():
    return render_template("welcome.html", name=current_user.username)
