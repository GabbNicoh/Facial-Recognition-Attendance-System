# logins

from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        id_num = request.form.get('id_num')
        password = request.form.get('password')

        user = User.query.filter_by(id_num=id_num).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Logged in successful!', category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash('Incorrect password', category='error')
        else:
            flash('ID Number does not exist', category='error')

    return render_template('login.html', users=current_user) 

@auth.route('/logout')
# @login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        id_num = request.form.get('id_num')
        password = request.form.get('password')

        user = User.query.filter_by(id_num=id_num).first()
        if user:
            flash('user already exists', category='error')
        else:
            new_user = User(id_num=id_num, password=generate_password_hash(password, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            flash('Account created!', category='success')
            return redirect(url_for('views.home'))

    return render_template("sign_up.html", user=current_user)