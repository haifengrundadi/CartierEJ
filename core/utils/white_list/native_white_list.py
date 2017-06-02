#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Functions：White list is used to deal with exception situations
    @date 2016/10
    @author Juan Liu
"""
import logging

from selenium.common.exceptions import NoSuchElementException

from core.utils.tools import screen_shot

logger = logging.getLogger(__name__)


class NativeWhiteList(object):
    """
        Native white list
    """

    CLASS_NAME = "Native white lists---"

    def __init__(self, driver):
        self.driver = driver

    def action(self):
        pass


class UpgradeMessageBox(NativeWhiteList):
    """
        Upgrade Message Box
    """
    CLASS_NAME = "Native white list--->upgrade message box"

    def __init__(self, driver):
        super(UpgradeMessageBox, self).__init__(driver)

    def action(self, decision=False):
        """
        click elements on pop message box
        """
        try:
            upgrade_button_id = "android:id/button1"
            cancel_button_id = "android:id/button2"
            upgrade_button = self.get_upgrade_btn_by_id(id=upgrade_button_id)
            cancel_button = self.get_cancel_btn_by_id(id=cancel_button_id)
        except NoSuchElementException:
            upgrade_button = None
            cancel_button = None

        assert upgrade_button is not None
        assert cancel_button is not None

        screen_shot(driver=self.driver, filename=self.CLASS_NAME + ".png")

        if decision and upgrade_button:
            logger.info(self.CLASS_NAME + " click upgrade button.")
            upgrade_button.click()
        elif not decision and cancel_button:
            logger.info(self.CLASS_NAME + " click cancel button.")
            cancel_button.click()
        else:
            pass

    def get_upgrade_btn_by_id(self, id=None):
        """
            get upgrade message box on upgrade message box
        """
        logger.info(self.CLASS_NAME + " get upgrade btn")
        return self.driver.find_element_by_id(id)

    def get_cancel_btn_by_id(self, id=None):
        """
            get cancel message box on upgrade message box
        """
        logger.info(self.CLASS_NAME + " get cancel btn")
        return self.driver.find_element_by_id(id)


def run_all_methods(driver):
    """
        run white list

        return：
        False ： represents find and deal with
        True : don't deal with
    """
    logger.info("Run all known message box to deal with the situation.")
    white_list = []
    upgrade_msg_box = UpgradeMessageBox(driver)
    white_list.append(upgrade_msg_box)
    for x in white_list:
        logger.info(x.CLASS_NAME)
        try:
            res = x.action()
        except NoSuchElementException:
            raise NoSuchElementException()
        if res and white_list.index(x) != len(white_list):
            return False
    return True
