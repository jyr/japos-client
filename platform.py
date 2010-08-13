#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

class Platform:
    def __init__(self, str):
        self.string = self.check(str)

    def check(self, str):
        PROJECT_DIR = os.getcwd()
        if sys.platform == "darwin" or sys.platform != "win32":
            str = PROJECT_DIR + str.replace("\\","/")
        else:
            str = PROJECT_DIR + str.replace("/","\\")

        return str