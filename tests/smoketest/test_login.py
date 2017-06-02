#!/usr/bin/env python
# -*- coding: utf-8 -*-
import logging
import os
from core.action.login_action import LoginAction

logger = logging.getLogger(__name__)


class TestLogin(object):
    """
        Test login
    """

    def test_run_login(self, appium_driver):
        """
            test login
        """

        logger.info("Test login.")
        if appium_driver is None:
            logger.info(" all devices inuse or no devices.")
            return

        logger.info("Begin to login")
        login_action = LoginAction(appium_driver)

        mobile_phone_number = os.environ.get('MOBILE_PHONE_NUMBER')
        code = os.environ.get('CODE')

        login_action.with_check_code_login_action(
            phone_number=mobile_phone_number, code=code)