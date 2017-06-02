# #!/usr/bin/env python
# # -*- coding: utf-8 -*-
# import pytest
# from appium.webdriver.webdriver import WebDriver as Driver
# from core.utils.log import LOGGER
# import logging
# import os
# import sys
#
# LOGGER.info("*********Begin**********")
# logger = logging.getLogger(__name__)
#
#
# @pytest.fixture(scope="session")
# def desired_caps(request):
#     """用于测试手机的效果"""
#     desired_caps = {}
#     desired_caps['platformName'] = 'Android'
#     try:
#         version = os.environ.get("PLATFORM_VERSION")
#         app_name = os.environ.get("APP_NAME")
#         devices_name = os.environ.get("DEVICES_NAME")
#     except KeyError:
#         logger.error("No environment variables for desired caps")
#         return None
#     if version is None or app_name is None or devices_name is None:
#         return None
#     desired_caps['platformVersion'] = version
#     desired_caps['app'] = app_name
#     desired_caps['deviceName'] = devices_name
#     desired_caps['newCommandTimeout'] = 60
#     desired_caps['unicodeKeyboard'] = 'true'
#     desired_caps['resetKeyboard'] = 'true'
#     desired_caps['noReset'] = 'false'
#     return desired_caps
#
#
# @pytest.fixture(scope="session")
# def appium_driver(request, desired_caps):
#     """启动appium"""
#     if desired_caps is None or len(desired_caps) <= 0:
#         logger.info(u"没有所需要的设备")
#         return
#
#     appium_web_driver = Driver('http://appium:4723/wd/hub', desired_caps)
#
#     def fin():
#         """销毁并退出当前session"""
#         appium_web_driver.close_app()
#         appium_web_driver.quit()
#
#     request.addfinalizer(fin)
#     return appium_web_driver
#
#
# # @pytest.mark.hookwrapper
# # def pytest_runtest_makereport(item, call):
# #     pytest_html = item.config.pluginmanager.getplugin('html')
# #     outcome = yield
# #     report = outcome.get_result()
# #     extra = getattr(report, 'extra', [])
# #     if report.when == 'call':
# #         if report.failed is True:
# #             _driver = item.funcargs['driver']
# #             extra.append(pytest_html.extras.url(_driver.current_url))
# #             extra.append(pytest_html.extras.image(_driver.get_screenshot_as_base64(), "screenshot"))
# #         report.extra = extra


"""
-------------test use-----------------------
used to develop
"""

import logging
import pytest
from appium.webdriver.webdriver import WebDriver as Driver
from core.utils.log import LOGGER

LOGGER.info("*********Begin**********")
logger = logging.getLogger(__name__)


@pytest.fixture(scope="session")
def desired_one_cap(request):
    """
    used to test one device
    :param request:
    :return:
    """
    desired_caps = {}
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '5.0'
    desired_caps['app'] = '/Users/red/temp/appium/com.xingin.xhs-test-4.20.apk'
    desired_caps['deviceName'] = 'cdf1b667'
    desired_caps['newCommandTimeout'] = 120
    desired_caps['unicodeKeyboard'] = True
    desired_caps['resetKeyboard'] = True
    desired_caps['noReset'] = False
    desired_caps['recreateChromeDriverSessions'] = True
    return desired_caps


@pytest.fixture(scope="session")
def appium_driver(request, desired_one_cap):
    """
    start appium driver
    :param request:
    :param desired_one_cap:  one device info
    :return:
    """

    appium_web_driver = Driver('http://0.0.0.0:4723/wd/hub', desired_one_cap)

    def fin():
        """quit current session"""
        appium_web_driver.close_app()
        appium_web_driver.quit()

    request.addfinalizer(fin)
    return appium_web_driver