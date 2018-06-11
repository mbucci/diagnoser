#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from __future__ import print_function

import os

from flask.ext.script import Manager, Server

from diagnoser.app import create_app


key = 'APP_ENVIRONMENT'
default_env = 'Local'
key_set = True

if key not in os.environ:
    key_set = False
    print("%s is not set, defaulting to %s." % (key, default_env))
    os.environ.setdefault(key, default_env)

env_name = os.environ[key].capitalize()
print("Environment variable: %s=%s" % (key, env_name))
settings = __import__('diagnoser.settings', fromlist=[env_name])
settings = getattr(settings, env_name)
print("Imported %s settings!" % env_name)

app = create_app(_config=settings())
manager = Manager(app)
server = Server(port=5000, threaded=True)
manager.add_command('runserver', server)


@manager.command
def test():
    import subprocess
    command = 'nosetests'
    return subprocess.call(command)


if __name__ == "__main__":
    manager.run()
