#!/usr/bin/env python
# -*- coding: utf-8 -*-
import logging

from core.action.login import LoginAction
from core.utils.config import PHONE_NUMBER, PASSWORD

logger = logging.getLogger(__name__)


class TestLogin(object):
    """
        Test login
    """

    def test_run_one_create_note(self, appium_driver):
        """
        appium_driver
        """
        if appium_driver is None:
            logger.info(" all devices inuse or no devices.")
            return

        logger.info("Begin to login")
        login_action = LoginAction(appium_driver)
        login_action.with_password_login_action(phone_number=PHONE_NUMBER, password=PASSWORD)