# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from __future__ import print_function

import json

from flask import url_for
from mock import patch, Mock, MagicMock
from diagnoser.core.tests.utils import ViewsTestCase


class APIViewsTestCase(ViewsTestCase):
    def setUp(self):
        super(APIViewsTestCase, self).setUp()
        self.pma_xp_patch = patch('kapy.pma_xp.create_api', return_value=MagicMock())
        self.mock_pma_xp = self.pma_xp_patch.start()
        self.addCleanup(self.pma_xp_patch.stop)
