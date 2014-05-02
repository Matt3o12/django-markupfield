#!/usr/bin/env python

"""
This script only runs if django 1.7 is installed.
"""

import django, os, sys
from subprocess import call


if django.VERSION <= (1, 7):
    print("No migrations have been made (django 1.7+ required)")
else:
    call(sys.argv[1:])