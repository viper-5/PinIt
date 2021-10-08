import datetime
import json
import os
from datetime import timedelta

import jinja2
from dotenv import load_dotenv
from flask import Flask, flash, render_template, request, session
# from flask_login import LoginManager
from flask_paranoid import Paranoid
from flask_socketio import SocketIO, emit

from models.user import requires_login
from views.users import logout, user_blueprint

global COOKIE_TIME_OUT

load_dotenv()
COOKIE_TIME_OUT = int(os.environ.get('COOKIE_TIME'))  # 7 days
print('COOKIE_TIME_OUT', COOKIE_TIME_OUT)


def create_app() -> Flask:
    app = Flask(__name__)
    app.secret_key = os.urandom(64)
    app.config.update(
        ADMIN=os.environ.get('ADMIN'),
        SESSION_COOKIE_SECURE=True,
        # PERMANENT_SESSION_LIFETIME=timedelta(seconds=COOKIE_TIME_OUT)
    )
    # socketio = SocketIO(app)

    paranoid = Paranoid(app)
    paranoid.redirect_view = 'users.register'

    # login_manager = LoginManager()
    # login_manager.session_protection = None
    # login_manager.init_app(app)

    jinja2.Environment(autoescape=True).filters['tojson'] = json.dumps
    app.register_blueprint(user_blueprint, url_prefix="/users")

    @app.route('/')
    def home():
        return render_template('index.html')

    @app.route('/create')
    @requires_login
    def create():
        if request.method == 'POST':
            return ("<h1>Create Note Form Submitted</h1>")
        # request.get_json()['toggle-bootstrap-theme']
        return render_template('create-note.html')

    @paranoid.on_invalid_session
    def invalid_session():
        return flash("Invalid Session Please Login")

    @app.before_request
    def before_request():

        now = datetime.datetime.now(datetime.timezone.utc)
        try:
            last_active = session['last_active']
            # print("Last Active ", last_active, type(last_active))
            delta = now - last_active
            if delta.seconds > COOKIE_TIME_OUT:
                print("\n\n\nTIMED OUT\n\n")
                session['last_active'] = now
                flash(
                    f'Your session has expired after {COOKIE_TIME_OUT} seconds, you have been logged out',
                    category='warning')
                logout(isSessionExpired=True)
                return
        except Exception as e:
            print(e)
        try:
            session['last_active'] = now
        except Exception as e:
            print(e)

    return app
