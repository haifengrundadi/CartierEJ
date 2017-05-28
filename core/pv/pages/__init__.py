#!/usr/bin/env python
# -*- coding: utf-8 -*-
from core.utils.uilocator import UiLocator

import logging

logger = logging.getLogger(__name__)


class BasePage(object):

    """页面类的基类"""

    def __init__(self, driver):
        self.driver = driver
        self.ui_locator = UiLocator(self.driver)
