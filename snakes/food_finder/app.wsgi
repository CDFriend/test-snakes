#!/usr/bin/python3

import os
import sys

# Change dir so relative paths still work
sys.path.append(os.path.dirname(os.path.realpath(__file__)))

# Provide application object for mod_wsgi
from snake import app
application = app
