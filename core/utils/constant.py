#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import platform
import logging

logger = logging.getLogger(__name__)

# 项目路径抽象
PROJECT_PATH = os.path.abspath(os.path.join(__file__, os.path.pardir,
                                            os.path.pardir, os.path.pardir))
RESOURCE_PATH = os.path.join(PROJECT_PATH, "resources")

# Andorid package 名字
PACKAGE_NAME = "com.xingin.xhs"

# 在本地客户端的地址
SCREEN_SHOT_PC_PATH = os.path.join(PROJECT_PATH, "logs/screenshot")
# 在devices上的临时存储地点
# SCREEN_SHOT_MOBILE_PATH = '/data/local/tmp/tmp.png'
# 在容器中的地址
# SCREEN_SHOT_CONTAINER_PATH = '/opt/node/screenshot/'

# 登录名
PHONE_NUMBER = ""
PASSWORD = ""
CODE = ''
