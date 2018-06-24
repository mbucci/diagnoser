# -*- coding: utf-8 -*-


from __future__ import unicode_literals
from __future__ import print_function

from flask.ext.testing import TestCase

from diagnoser.app import create_app


class BaseTestCase(TestCase):

    def create_app(self):
        settings = __import__('diagnoser.settings', fromlist='Test')
        test_config = getattr(settings, 'Test')
        app = create_app(_config=test_config())

        self.diagnoser_api = app.diagnoser_api

        return app
