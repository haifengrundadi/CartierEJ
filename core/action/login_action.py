#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    Login case
    @Author  Juan Liu
    @Date 2016
"""

from core.action import BaseAction
from core.pv.pages.login_page import FirstLoginPage, LoginPage, PasswordLoginPage, CheckCodeLoginPage
from core.pv.pages.home_page import HomePage
import logging

logger = logging.getLogger(__name__)


class LoginAction(BaseAction):
    """
        Login action
    """
    ACTION_NAME = "Login action--->"

    def __init__(self, driver):
        self.driver = driver

    def action(self):
        """
            click login button
        """
        first_login_page = FirstLoginPage(self.driver)
        id = "com.xingin.xhs:id/btn_login"
        login_button = first_login_page.get_login_button_by_id(id=id)
        assert login_button is not None
        logger.info(self.ACTION_NAME + "click login button.")
        login_button.click()

    def login_action(self):
        """
            login page after click password login button
        """
        login_page = LoginPage(self.driver)
        id = "com.xingin.xhs:id/tv_login_psw"
        login_psw_button = login_page.get_login_psw_button_by_id(id=id)
        assert login_psw_button is not None
        logger.info(self.ACTION_NAME + "click login button.")
        login_psw_button.click()

    def with_password_login_action(self, phone_number=None, password=None):
        """
            login with phone number and password
        """
        if phone_number is None or password is None:
            logger.info(self.ACTION_NAME + " please input phone number and password.")
            return
        self.action()
        self.login_action()
        password_login_page = PasswordLoginPage(self.driver)

        et_phone_id = "com.xingin.xhs:id/et_phone"
        phone_number_text_view = password_login_page.get_phone_number_textview_by_id(id=et_phone_id)
        logger.info(self.ACTION_NAME + "input phone number:" + phone_number)
        assert phone_number_text_view is not None
        phone_number_text_view.send_keys(phone_number)

        pwd_id = "com.xingin.xhs:id/et_psd"
        password_text_view = password_login_page.get_password_textview_by_id(id=pwd_id)
        logger.info(self.ACTION_NAME + "input password:" + password)
        assert password_text_view is not None
        password_text_view.send_keys(password)

        login_btn_id = "com.xingin.xhs:id/btn_login"
        password_login_button = password_login_page.get_password_login_button_by_id(id=login_btn_id)
        logger.info(self.ACTION_NAME + "click login button.")
        assert password_login_button is not None
        password_login_button.click()

        self.check_if_login_success()

    def with_check_code_login_action(self, phone_number=None, code=None):
        """
            login with mobile phone and check code.
        """
        self.action()
        login_page = LoginPage(self.driver)

        et_phone_id = "com.xingin.xhs:id/et_phone"
        login_phone_txt = login_page.get_et_phone_txt_by_id(id=et_phone_id)
        assert login_phone_txt is not None
        logger.info(self.ACTION_NAME + "input mobile phone number.")
        login_phone_txt.send_keys(phone_number)

        next_btn_id = "com.xingin.xhs:id/btn_next"
        next_btn = login_page.get_next_btn_by_id(id=next_btn_id)
        logger.info(self.ACTION_NAME + "click next button.")
        assert next_btn is not None
        next_btn.click()

        check_code_page = CheckCodeLoginPage(self.driver)
        check_code_txt = "com.xingin.xhs:id/et_ver_code"
        check_code_txt = check_code_page.get_check_code_txt_by_id(id=check_code_txt)
        assert check_code_txt is not None
        logger.info(self.ACTION_NAME + "input check code.")
        check_code_txt.send_keys(code)

        code_login_btn_id = "com.xingin.xhs:id/btn_login"
        login_btn = check_code_page.get_login_btn_by_id(id=code_login_btn_id)
        assert login_btn is not None
        logger.info(self.ACTION_NAME + "click and enter main page.")
        login_btn.click()

        self.check_if_login_success()

    def check_if_login_success(self):
        """
            check if login success
        """
        logger.info(self.ACTION_NAME + " through finding shop tab on main page \t\n "
                                       " to check if login success.")
        home_page = HomePage(self.driver)
        shop_tab_id = 'com.xingin.xhs:id/btnTabShop'
        shop_tab = home_page.get_shop_tab_by_id(id=shop_tab_id)
        assert shop_tab is not None
        logger.info(self.ACTION_NAME + " login success!")
