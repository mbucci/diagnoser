# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from __future__ import print_function

import os
import logging
import uuid

MAJOR = 0
MINOR = 1
PATCH = 0


class Common(object):
    VERSION = "{major}.{minor}.{patch}".format(major=MAJOR, minor=MINOR, patch=PATCH)

    THREADS_PER_PAGE = 8
    LOGGING_LEVEL = logging.INFO
    LOGGING_STDOUT = True

    SYMPTOMS_FILE = "symptoms.csv"


class Local(Common):
    DEBUG = True


class Development(Common):
    DEBUG = True


class Staging(Common):
    pass


class Production(Common):
    pass


class Test(Common):
    LOGGING_LEVEL = logging.CRITICAL
    LOGGING_STDOUT = False

