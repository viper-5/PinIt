import os
from flask import (
    Blueprint, escape, flash, redirect, render_template,
    request, session, url_for
)
from flask.helpers import make_response
from models.user import User, UserErrors

user_blueprint = Blueprint('users', __name__)

COOKIE_TIME_OUT = int(os.environ.get('COOKIE_TIME'))


@user_blueprint.route('/register', methods=['GET', 'POST'])
def register_user():
    if request.method == 'POST':
        email = escape(request.form['email'])
        password = escape(request.form['password'])

        try:
            User.register_user(email, password)
            session['email'] = email
            flash(f'Welcome {email}', "success")
            return redirect(url_for('create'))
        except UserErrors.UserError as e:
            flash(e.message, 'error')
            return render_template('users/register.html')

    return render_template('users/register.html')


@user_blueprint.route('/login', methods=['GET', 'POST'])
def login_user():

    print("email in cookies: ", request.cookies.get('email'))
    print(request.cookies)
    if 'email' in request.cookies:
        email = request.cookies.get('email')
        password = request.cookies.get('password')

        try:
            if User.is_login_valid(email, password):
                session['email'] = email
                flash(f'Welcome {email}', "success")
                return redirect(url_for('create'))
            flash(f'Invalid credentials. Please try again.')
            return redirect(url_for('users.login_user'))

        except UserErrors.UserError as e:
            flash(e.message, 'error')
            return redirect(url_for('users.login_user'))

    if request.method == 'POST':
        email = escape(request.form['email'])
        password = escape(request.form['password'])
        print(request.form.getlist('rememberMe'))
        if(request.form.getlist('rememberMe') is not None):
            session['rememberMe'] = True
        try:
            if User.is_login_valid(email, password):
                session['email'] = email
                flash(f'Welcome {email}', "success")
                if session['rememberMe'] is True:
                    print("remember me is true")
                    resp = make_response(redirect('home'))
                    resp.set_cookie('email', email, max_age=COOKIE_TIME_OUT)
                    resp.set_cookie('password', password,
                                    max_age=COOKIE_TIME_OUT)
                    resp.set_cookie('rememberMe', '1',
                                    max_age=COOKIE_TIME_OUT)
                    return redirect(url_for('create'))
            flash(f'Invalid credentials. Please try again.')
            return redirect(url_for('users.login_user'))
        except UserErrors.UserError as e:
            flash(e.message, 'error')
            return redirect(url_for('users.login_user'))

    return render_template('users/login.html')


@ user_blueprint.route('/logout')
def logout(isSessionExpired=False):
    if 'email' in session:
        session['email'] = None
        if(isSessionExpired is not True):
            flash('Successfully logged out', 'success')
    else:
        if(isSessionExpired is not True):
            flash('User is not logged in to logout', 'warning')
    session['remember'] = None
    return redirect(url_for('.login_user'))
