#!/usr/bin/env python

import sys, os

sys.path.append("/Users/jyr/Desarrollo/git-projects/japos-client")

from django.core.management import setup_environ
from japos import settings

setup_environ(settings)

from django.contrib.auth.models import check_password
from japos.crews.models import *
from japos.openings.models import Opening

if __name__ == '__main__':
    print Opening.objects.all()