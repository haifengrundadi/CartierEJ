#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    功能：白名单主要是用来处理弹出的messagebox，包括一些操作确认，和授权确认信息，以便
    程序可以不受这些影响跑完一个业务，并对每一个异常进行截图
    @date 2016/10
    @author Juan Liu
"""
import logging
from selenium.common.exceptions import NoSuchElementException
from core.utils.tools import screen_shot
logger = logging.getLogger(__name__)


class NativeWhiteList(object):
    """
        Native_APP的白名单
    """

    CLASS_NAME = u"Native_APP白名单--->"

    def __init__(self, driver):
        self.driver = driver

    def action(self):
        pass


class UpgradeMessageBox(NativeWhiteList):
    """
        出现更新消息框
    """
    CLASS_NAME = u"Native_APP白名单--->出现更新消息框"

    def __init__(self, driver):
        super(UpgradeMessageBox, self).__init__(driver)

    def action(self, decision=False):
        """
            点击最新版本按钮
        """
        try:
            upgrade_button, cancel_button = self.get_msg_btns()
        except NoSuchElementException:
            raise NoSuchElementException()
        if upgrade_button is None or cancel_button is None:
            return False
        else:
            screen_shot(driver=self.driver, filename=self.CLASS_NAME + ".png")
        if decision and upgrade_button:
            logger.info(self.CLASS_NAME + u"点击更新按钮")
            upgrade_button.click()
        elif not decision and cancel_button:
            logger.info(self.CLASS_NAME + u"点击取消按钮")
            cancel_button.click()
        else:
            pass
        return True

    def get_msg_btns(self):
        """
            获取消息框中的控件
        """
        try:
            upgrade_button = self.driver.find_element_by_id("android:id/button1")
            cancel_button = self.driver.find_element_by_id("android:id/button2")
        except NoSuchElementException:
            raise NoSuchElementException()
        return upgrade_button, cancel_button


class AuthorizeMessageBox(NativeWhiteList):
    """
        出现授权消息框
    """
    CLASS_NAME = u"Native_APP白名单--->出现授权消息框"

    def __init__(self, driver):
        super(AuthorizeMessageBox, self).__init__(driver)

    def action(self, decision=False):
        """
            点击最新版本按钮
        """
        try:
            next_button = self.get_msg_btns()
        except NoSuchElementException:
            raise NoSuchElementException()
        if next_button is None:
            return False
        else:
            screen_shot(driver=self.driver, filename=self.CLASS_NAME + ".png")
            logger.info(self.CLASS_NAME + u"点击下一步按钮")
            next_button.click()
            return True

    def get_msg_btns(self):
        """
            获取消息框中的控件
        """
        try:
            next_button = self.driver.find_element_by_id("android:id/button1")
            return next_button
        except NoSuchElementException:
            raise NoSuchElementException()


def run_all_methods(driver):
    """
        运行白名单中的所有方法
        :return
        False 代表没有运行完所有白名单就找到了处理的情况
        True 代表运行完所有白名单没有找到处理的情况
    """
    logger.info(u"运行白名单中已知的消息框处理")
    white_list = []
    upgrade_msg_box = UpgradeMessageBox(driver)
    authorize_msg_box = AuthorizeMessageBox(driver)
    white_list.append(upgrade_msg_box)
    white_list.append(authorize_msg_box)
    for x in white_list:
        logger.info(x.CLASS_NAME)
        try:
            res = x.action()
        except NoSuchElementException:
            raise NoSuchElementException()
        if res and white_list.index(x) != len(white_list):
            return False
    return True
