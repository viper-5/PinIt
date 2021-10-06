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


def auth_login(email, password, set_cookie: bool = False):
    try:
        if User.is_login_valid(email, password):
            session['email'] = email
            flash(f'Welcome {email}', "success")
            if(set_cookie is True and session['rememberMe'] == '1'):
                print("remember me is true")
                resp = make_response(redirect(url_for('create')))
                resp.set_cookie('email', email, max_age=COOKIE_TIME_OUT)
                resp.set_cookie('password', password,
                                max_age=COOKIE_TIME_OUT)
                resp.set_cookie('rememberMe', '1',
                                max_age=COOKIE_TIME_OUT)
                return resp
                return redirect(url_for('create'))
            return redirect(url_for('create'))

        else:
            flash(f'Invalid credentials. Please try again.')
            return redirect(url_for('users.login_user'))

    except UserErrors.UserError as e:
        flash(e.message, 'error')
        return redirect(url_for('users.login_user'))


@user_blueprint.route('/login', methods=['GET', 'POST'])
def login_user():

    if session.get('email') is not None:
        flash("Already Logged in", "info")
        return redirect(url_for('create'))
    print("email in cookies: ", request.cookies.get('email'))
    print("something useful in cookies: ", request.cookies.get('rememberMe'))
    print(request.cookies)
    if 'email' in request.cookies:
        email = request.cookies.get('email')
        password = request.cookies.get('password')
        return auth_login(email, password, set_cookie=False)

    if request.method == 'POST':
        email = escape(request.form['email'])
        password = escape(request.form['password'])
        print(request.form.getlist('rememberMe'))
        print(request.form.getlist('rememberMe') == ['1'])
        if(request.form.getlist('rememberMe') == ['1']):
            session['rememberMe'] = '1'
        else:
            session['rememberMe'] = '0'
        return auth_login(email, password, set_cookie=True)

    return render_template('users/login.html')


@ user_blueprint.route('/logout')
def logout(isSessionExpired=False):
    if session['email'] is not None:
        session['email'] = None
        res = make_response(redirect(url_for('.login_user')))
        res.set_cookie('email', 'foo', max_age=0)
        res.set_cookie('password', 'bar', max_age=0)
        res.set_cookie('rememberMe', 'lorem', max_age=0)
        if(isSessionExpired is not True):
            flash('Successfully logged out', 'success')
        return res

    else:
        if(isSessionExpired is not True):
            flash('User is not logged in to logout', 'warning')
    session['remember'] = None
    return redirect(url_for('.login_user'))
