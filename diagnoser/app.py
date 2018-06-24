# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from __future__ import print_function

import re

from flask import Flask, current_app, Markup

from diagnoser import settings as config
from diagnoser.api.diagnoser_api import DiagnoserAPI


def create_app(_config=config.Local):
    app = Flask(__name__)
    app.config.from_object(_config)

    register_blueprints(app)

    with open(_config.SYMPTOMS_FILE, 'r') as symptoms_file:
        app.diagnoser_api = DiagnoserAPI(symptoms_file)

    @app.before_request
    def set_logging_context():
        pass

    @app.before_request
    def set_monitoring_context():
        pass

    app.version = _config.VERSION
    return app


def register_blueprints(app):
    # Import and register blueprints here.
    from diagnoser.core import views as coreViews
    app.register_blueprint(coreViews.CORE)
    from diagnoser.api import views as apiViews
    app.register_blueprint(apiViews.API)

    return None
