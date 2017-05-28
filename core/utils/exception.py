#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""自动化测试框架异常模块"""

from selenium.common.exceptions import WebDriverException
import logging

logger = logging.getLogger(__name__)


class CartierException(WebDriverException):
    pass


class UICoreBaseException(CartierException):
    pass
