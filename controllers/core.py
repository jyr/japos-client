#!/usr/bin/env python

import sys, os
PROJECT_DIR = os.getcwd()

sys.path.append(PROJECT_DIR)

from django.core.management import setup_environ
from japos import settings

setup_environ(settings)

from japos.openings.models import Opening

if __name__ == '__main__':
    print Opening.objects.all()