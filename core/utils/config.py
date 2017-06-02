#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import logging

logger = logging.getLogger(__name__)

PROJECT_PATH = os.path.abspath(os.path.join(__file__, os.path.pardir,
                                            os.path.pardir, os.path.pardir))
RESOURCE_PATH = os.path.join(PROJECT_PATH, "resources")

PACKAGE_NAME = "com.xingin.xhs"

SCREEN_SHOT_PC_PATH = os.path.join(PROJECT_PATH, "logs/screenshot")

PHONE_NUMBER = ""
PASSWORD = ""
CODE = ''
