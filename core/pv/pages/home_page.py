#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    home page
"""

import logging

from core.pv.pages import BasePage

logger = logging.getLogger(__name__)


class HomePage(BasePage):
    """
        login page --> main page
    """
    PAGE_NAME = "main page --"

    def __init__(self, driver):
        super(HomePage, self).__init__(driver)
        self.driver = driver

    def get_shop_tab_by_id(self, id=id):
        """
        shop tab on footer bar
        """
        logger.info(self.PAGE_NAME + " get shop tab on footer bar")
        return self.ui_locator.find_element_by_id(id)
