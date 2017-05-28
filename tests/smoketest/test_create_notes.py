#!/usr/bin/env python
# -*- coding: utf-8 -*-
from core.action.login import LoginAction
from core.action.create_note import CreateNoteAction
from core.utils.constant import PHONE_NUMBER, PASSWORD
import logging
import time

logger = logging.getLogger(__name__)


class TestCreateNte(object):
    """测试创建笔记"""

    def test_run_one_create_note(self, appium_driver):
        """
        :param appium_driver:
        :return:
        """
        # time.sleep(5)
        if appium_driver is None:
            logger.info(u"所有的设备都在使用或者没有设备")
            return
        appium_driver = appium_driver
        logger.info('Test create note')
        login_action = LoginAction(appium_driver)
        logger.info("Begin to login")
        login_action.with_password_login_action(phone_number=PHONE_NUMBER, password=PASSWORD)
        logger.info('Begin to test upload pictures')
        upload_action = CreateNoteAction(appium_driver)
        upload_action.deliver_note_action()
        logger.info('End test the upload pictures')
        # time.sleep(5)