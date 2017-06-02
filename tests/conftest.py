#!/usr/bin/env python
# -*- coding: utf-8 -*-
import logging
import os
import pytest
from collections import defaultdict
from appium.webdriver.webdriver import WebDriver as Driver
from core.utils.log import LOGGER

LOGGER.info("*********Begin**********")
logger = logging.getLogger(__name__)


@pytest.fixture(scope="session")
def desired_caps(request):
    """
    Used to test multi devices
    """
    desired_caps = defaultdict(list)
    desired_caps['platformName'] = 'Android'
    try:
        version = os.environ.get("PLATFORM_VERSION")
        app_name = os.environ.get("APK_NAME")
        devices_name = os.environ.get("DEVICES_NAME")
    except KeyError:
        logger.error("No environment variables for desired caps")
        return None
    if version is None or app_name is None or devices_name is None:
        return None
    desired_caps['platformVersion'] = version
    desired_caps['app'] = app_name
    desired_caps['deviceName'] = devices_name
    desired_caps['newCommandTimeout'] = os.environ.get("NEW_COMMAND_TIME_OUT")
    desired_caps['unicodeKeyboard'] = True
    desired_caps['resetKeyboard'] = True
    desired_caps['noReset'] = False
    return desired_caps


@pytest.fixture(scope="session")
def appium_driver(request, desired_caps):
    if desired_caps is None or len(desired_caps) <= 0:
        logger.info("No devices found.")
        return

    appium_web_driver = Driver('http://appium:4723/wd/hub', desired_caps)

    def fin():
        """quit current session"""
        appium_web_driver.close_app()
        appium_web_driver.quit()

    request.addfinalizer(fin)
    return appium_web_driver


#
# """
# -------------test use-----------------------
# used to develop
# """
#
# import logging
# import pytest
# from appium.webdriver.webdriver import WebDriver as Driver
# from core.utils.log import LOGGER
# from core.utils.config import NEW_COMMAND_TIME_OUT
#
# LOGGER.info("*********Begin**********")
# logger = logging.getLogger(__name__)
#
#
# @pytest.fixture(scope="session")
# def desired_one_cap(request):
#     """
#     used to test one device
#     :param request:
#     :return:
#     """
#     desired_caps = {}
#     desired_caps['platformName'] = 'Android'
#     desired_caps['platformVersion'] = '5.0'
#     desired_caps['app'] = '/Users/red/temp/appium/com.xingin.xhs-test-4.20.apk'
#     desired_caps['deviceName'] = 'cdf1b667'
#     desired_caps['newCommandTimeout'] = NEW_COMMAND_TIME_OUT
#     desired_caps['unicodeKeyboard'] = True
#     desired_caps['resetKeyboard'] = True
#     desired_caps['noReset'] = False
#     desired_caps['recreateChromeDriverSessions'] = True
#     return desired_caps
#
#
# @pytest.fixture(scope="session")
# def appium_driver(request, desired_one_cap):
#     """
#     start appium driver
#     :param request:
#     :param desired_one_cap:  one device info
#     :return:
#     """
#
#     appium_web_driver = Driver('http://0.0.0.0:4723/wd/hub', desired_one_cap)
#
#     def fin():
#         """quit current session"""
#         appium_web_driver.close_app()
#         appium_web_driver.quit()
#
#     request.addfinalizer(fin)
#     return appium_web_driver