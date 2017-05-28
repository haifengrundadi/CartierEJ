#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    登录操作
"""

from core.action import BaseAction
from core.pv.pages.login import FirstLoginPage, LoginPage, PasswordLoginPage,CheckCodeLoginPage
import logging

logger = logging.getLogger(__name__)


class LoginAction(BaseAction):

    """
        登录操作
    """
    ACTION_NAME = u"登录操作--->"

    def __init__(self, driver):
        self.driver = driver

    def action(self):
        """
        :return:
        """
        first_login_page = FirstLoginPage(self.driver)
        login_button = first_login_page.get_login_button()
        logger.info(self.ACTION_NAME + u"点击登录")
        login_button.click()

    def login_action(self):
        """
            点击密码登录 之后 登录
            :return:
        """
        login_page = LoginPage(self.driver)
        login_psw_button = login_page.get_login_psw_button()
        logger.info(self.ACTION_NAME + u"点击登录")
        login_psw_button.click()

    def with_password_login_action(self, phone_number=None, password=None):
        """
            使用手机号和密码登录
            @author juan 01/08（之后需要把这个测试账号给去掉）
            :return:
        """
        self.action()
        self.login_action()
        password_login_page = PasswordLoginPage(self.driver)
        # 填写手机号 密码
        phone_number_text_view = password_login_page.get_phone_number_textview()
        logger.info(self.ACTION_NAME + u"输入手机号码:" + phone_number)
        phone_number_text_view.send_keys(phone_number)
        password_text_view = password_login_page.get_password_textview()
        logger.info(self.ACTION_NAME + u"输入密码:" + password)
        password_text_view.send_keys(password)
        password_login_button = password_login_page.get_password_login_button()
        logger.info(self.ACTION_NAME + u"点击登录")
        password_login_button.click()

    def with_check_code_login_action(self, phone_number=None, code=None):
        """
            使用手机号获取验证码登录
        """
        self.action()
        login_page = LoginPage(self.driver)
        login_phone_txt = login_page.get_et_phone_txt()
        logger.info(self.ACTION_NAME + u"输入手机号码")
        login_phone_txt.send_keys(phone_number)
        next_btn = login_page.get_next_btn()
        logger.info(self.ACTION_NAME + u"点击下一步按钮")
        next_btn.click()
        check_code_page = CheckCodeLoginPage(self.driver)
        check_code_txt = check_code_page.get_check_code_txt()
        logger.info(self.ACTION_NAME + u"输入验证码")
        check_code_txt.send_keys(code)
        login_btn = check_code_page.get_login_btn()
        logger.info(self.ACTION_NAME + u"点击进入小红书按钮")
        login_btn.click()