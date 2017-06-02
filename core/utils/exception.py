#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    Exception module to deal with errors
    @author Juan Liu
    @date 2016
"""

from selenium.common.exceptions import WebDriverException
import logging

logger = logging.getLogger(__name__)


class CartierEJException(WebDriverException):
    pass


class UICoreBaseException(CartierEJException):
    pass
