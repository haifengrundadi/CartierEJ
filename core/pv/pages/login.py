#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    登录界面（除了手机号，也支持包含第三方（微信，qq，微博等）登录方式）
"""

from core.pv.pages import BasePage
import logging

logger = logging.getLogger(__name__)


class FirstLoginPage(BasePage):
    """
       流程： 主界面登录按钮
    """
    PAGE_NAME = u"首个登录界面--->"

    def __init__(self, driver):
        super(FirstLoginPage, self).__init__(driver)

    def get_login_button(self):
        """
            获取登录按钮
        """
        logger.info(self.PAGE_NAME + u"获取登录按钮")
        btn_login = self.ui_locator.find_element_by_id("com.xingin.xhs:id/btn_login")
        assert btn_login is not None
        return btn_login


class LoginPage(BasePage):
    """
    --》使用密码登录
    """
    PAGE_NAME = u"手机号码快速登录界面--"

    def __init__(self, driver):
        super(LoginPage, self).__init__(driver)

    def get_login_psw_button(self):
        """
            获取登录按钮
        """
        logger.info(self.PAGE_NAME + u"获取登录按钮")
        return self.ui_locator.find_element_by_id("com.xingin.xhs:id/tv_login_psw")

    def get_et_phone_txt(self):
        """
            获取手机号填写框
        """
        logger.info(self.PAGE_NAME + u"获取手机号填写框")
        return self.ui_locator.find_element_by_id("com.xingin.xhs:id/et_phone")

    def get_next_btn(self):
        """
            获取下一步按钮
        """
        logger.info(self.PAGE_NAME + u"获取下一步按钮")
        return self.ui_locator.find_element_by_id("com.xingin.xhs:id/btn_next")


class PasswordLoginPage(BasePage):
    """
        流程：填写手机号和密码 -》点击登录按钮
    """
    PAGE_NAME = u"使用密码登录界面--"

    def __init__(self, driver):
        super(PasswordLoginPage, self).__init__(driver)

    def get_phone_number_textview(self):
        """
        获取密码登录界面的手机号填写文本框
        :return:
        """
        logger.info(self.PAGE_NAME + u"获取手机号填写文本框")
        return self.ui_locator.find_element_by_id("com.xingin.xhs:id/et_phone")

    def get_password_login_button(self):
        """
        获取使用密码登录按钮
        :return:
        """
        logger.info(self.PAGE_NAME + u"获取登录按钮")
        return self.ui_locator.find_element_by_id("com.xingin.xhs:id/btn_login")

    def get_password_textview(self):
        """
        获取密码登录界面，密码文本个框
        :return:
        """
        logger.info(self.PAGE_NAME + u"获取密码登录文本框")
        return self.ui_locator.find_element_by_id("com.xingin.xhs:id/et_psd")


class CheckCodeLoginPage(BasePage):
    """
       流程：填写手机号 -》填写验证码---》进入小红书
    """
    PAGE_NAME = u"使用验证码登录界面--"

    def __init__(self, driver):
        super(CheckCodeLoginPage, self).__init__(driver)

    def get_check_code_txt(self):
        """
        获取密码登录界面，密码文本个框
        :return:
        """
        logger.info(self.PAGE_NAME + u"获取验证码登录文本框")
        return self.ui_locator.find_element_by_id("com.xingin.xhs:id/et_ver_code")

    def get_login_btn(self):
        """
        获取登录按钮
        """
        logger.info(self.PAGE_NAME+u"点击进入小红书")
        return self.ui_locator.find_element_by_id("com.xingin.xhs:id/btn_login")