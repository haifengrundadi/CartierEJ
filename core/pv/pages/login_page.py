#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    login page:
    Including using mobile phone number login,
    using wechat ,qq, Sina and so on login
    @author Juan Liu
    @date 2017/06/01
"""

import logging

from core.pv.pages import BasePage

logger = logging.getLogger(__name__)


class FirstLoginPage(BasePage):
    """
       Flow： Main page login
    """
    PAGE_NAME = "First login page---"

    def __init__(self, driver):
        super(FirstLoginPage, self).__init__(driver)

    def get_login_button_by_id(self, id=None):
        """
            Get login button by id
        """
        logger.info(self.PAGE_NAME + " get login button")
        return self.ui_locator.find_element_by_id(id)


class LoginPage(BasePage):
    """
        Login with password
    """
    PAGE_NAME = "Login page with smart phone number--"

    def __init__(self, driver):
        super(LoginPage, self).__init__(driver)

    def get_login_psw_button_by_id(self, id=None):
        """
            get login button
        """
        logger.info(self.PAGE_NAME + " get login button.")
        return self.ui_locator.find_element_by_id(id)

    def get_et_phone_txt_by_id(self, id=None):
        """
            get phone textview
        """
        logger.info(self.PAGE_NAME + " get phone textview.")
        return self.ui_locator.find_element_by_id(id)

    def get_next_btn_by_id(self, id=None):
        """
            get next button
        """
        logger.info(self.PAGE_NAME + " get next button.")
        return self.ui_locator.find_element_by_id(id)


class PasswordLoginPage(BasePage):
    """
        Flow：input phone number and password -> click login button
    """
    PAGE_NAME = "Login page with password--"

    def __init__(self, driver):
        super(PasswordLoginPage, self).__init__(driver)

    def get_phone_number_textview_by_id(self,id=id):
        """
            get mobile phone text view
        """
        logger.info(self.PAGE_NAME + " get mobile phone text view")
        return self.ui_locator.find_element_by_id(id)

    def get_password_login_button_by_id(self,id=id):
        """
            get login button
        """
        logger.info(self.PAGE_NAME + " get login button.")
        return self.ui_locator.find_element_by_id(id)

    def get_password_textview_by_id(self,id=id):
        """
            get password textview
        """
        logger.info(self.PAGE_NAME + " get password textview.")
        return self.ui_locator.find_element_by_id(id)


class CheckCodeLoginPage(BasePage):
    """
        Flow：input phome number ->input check code--->enter app home
    """
    PAGE_NAME = "Login page with check code--"

    def __init__(self, driver):
        super(CheckCodeLoginPage, self).__init__(driver)

    def get_check_code_txt_by_id(self,id=id):
        """
            get check code text view
        """
        logger.info(self.PAGE_NAME + " get check code text view.")
        return self.ui_locator.find_element_by_id(id)

    def get_login_btn_by_id(self, id=id):
        """
            Get Login button
        """
        logger.info(self.PAGE_NAME + " click and enter home page.")
        return self.ui_locator.find_element_by_id(id)
