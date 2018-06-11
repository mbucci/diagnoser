# -*- coding: utf-8 -*-


from __future__ import unicode_literals
from __future__ import print_function

import flask
import json
import os


from flask import current_app

CORE = flask.Blueprint('main', __name__, url_prefix='')


@CORE.route('/status', methods=['GET'])
def get_status():
    env = os.environ.get("APP_ENVIRONMENT").lower()
    dependencies = []

    response = {
        "name": "diagnoser",
        "version": current_app.version,
        "environment": env,
        "dependencies": dependencies,
    }

    return flask.jsonify(response), 200


@CORE.route('/home', methods=['GET'])
def home():
    all_symptoms = json.dumps(current_app.diagnoser_api.get_all_symptoms())
    return flask.render_template('index.html',
                                 symptoms=all_symptoms,
                                 app_name='Diagnoser')

