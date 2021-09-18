import json
import os
import jinja2
from flask import Flask, render_template


def create_app() -> Flask:
    app = Flask(__name__)
    app.secret_key = os.urandom(64)
    app.config.update(
        ADMIN=os.environ.get('ADMIN')
    )
    jinja2.Environment(autoescape=True).filters['tojson'] = json.dumps

    @app.route('/')
    def home():
        return render_template('index.html')

    @app.route('/register')
    def signUp():
        return render_template('register.html')

    @app.route('/login')
    def login():
        return render_template('login.html')

    @app.route('/create')
    def create():
        return render_template('create-note.html')

    return app
