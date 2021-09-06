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
        return render_template('base.html')
    return app
