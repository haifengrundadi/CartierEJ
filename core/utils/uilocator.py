#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    功能：目前封装Native元素定位
    Reference Link https://github.com/appium/python-client
    @date 2016/10
    @author Juan Liu
"""

import logging

from core.utils.wait.native_wait import Wait

logger = logging.getLogger(__name__)


class UiLocator(object):
    """
        封装元素定位
    """

    CLASS_NAME = u"元素定位--->"
    TIME_OUT_TIME = 10

    def __init__(self, appium_driver):
        self.driver = appium_driver

    def find_element_by_name(self, name):
        """
            通过name查找元素
            :param name:
            :return:
        """
        el = (self.driver, self.TIME_OUT_TIME). \
            until(lambda x: x.find_element_by_name(id))
        return el

    def find_element_by_id(self, id):
        """
            通过id查找元素
            :param id:
            :return:
        """
        el = Wait(self.driver, self.TIME_OUT_TIME). \
            until(lambda x: x.find_element_by_id(id))
        return el

    def find_elements_by_accessibility_id(self, els_id):
        """
            通过id查找所有元素
        """
        els = Wait(self.driver, self.TIME_OUT_TIME). \
            until(lambda x: x.find_elements_by_accessibility_id(els_id))
        return els

    def find_elements_by_android_uiautomator(self, ui_query):
        """
            通过uiatomator查找多个元素
            :param ui_query:
            :return:
        """
        if 'com.xingin.xhs:id/img_select' in ui_query:
            # 此处的逻辑是 找不到图片 就返回一个None; 而不是 抛出一个异常
            els = self.driver.find_elements_by_android_uiautomator(ui_query)
        else:
            els = Wait(self.driver, self.TIME_OUT_TIME). \
                until(lambda x: x.find_elements_by_android_uiautomator(ui_query))
        return els

    def find_element_by_android_uiautomator(self, ui_query):
        """
            通过uiatomator查找元素
            :param ui_query:
            :return:
        """
        el = Wait(self.driver, self.TIME_OUT_TIME). \
            until(lambda x: x.find_element_by_android_uiautomator(ui_query))
        return el

    def swipe(self, start_x, start_y, end_x, end_y, duration=None):
        """
            Swipe from one point to another point, for an optional duration.
            :Args:
             - start_x - x-coordinate at which to start
             - start_y - y-coordinate at which to start
             - end_x - x-coordinate at which to stop
             - end_y - y-coordinate at which to stop
             - duration - (optional) time to take the swipe, in ms.
            :Usage:
                driver.swipe(100, 100, 100, 400)
        """
        # `swipe` is something like press-wait-move_to-release, which the server
        # will translate into the correct action
        self.driver.swipe(start_x, start_y, end_x, end_y, duration)
