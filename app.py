import json
import os

import jinja2
from flask import Flask, render_template, flash
from flask_paranoid import Paranoid

from views.users import user_blueprint


def create_app() -> Flask:
    app = Flask(__name__)
    app.secret_key = os.urandom(64)
    app.config.update(
        ADMIN=os.environ.get('ADMIN'),
        SESSION_COOKIE_SECURE=True
    )
    paranoid = Paranoid(app)
    paranoid.redirect_view = 'users.register'
    jinja2.Environment(autoescape=True).filters['tojson'] = json.dumps
    app.register_blueprint(user_blueprint, url_prefix="/users")

    @app.route('/')
    def home():
        return render_template('index.html')

    # @app.route('/register')
    # def signUp():
    #     return render_template('register.html')

    # @app.route('/login')
    # def login():
    #     return render_template('login.html')

    @app.route('/create')
    def create():
        return render_template('create-note.html')

    @paranoid.on_invalid_session
    def invalid_session():
        return flash("Session Expired Please Login")

    return app
