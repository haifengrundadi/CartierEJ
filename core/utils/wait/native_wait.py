#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Function：Used to set wait when find elements(references code from common module)
    @date 2016/10
    @author Juan Liu
"""
import logging
import time

from selenium.common.exceptions import NoSuchElementException, TimeoutException

from core.utils.tools import screen_shot
from core.utils.white_list.native_white_list import run_all_methods

logger = logging.getLogger(__name__)
POLL_FREQUENCY = 0.5  # time to sleep inbetween calls to the method
IGNORED_EXCEPTIONS = (NoSuchElementException,)  # exceptions ignored during calls to the method


class Wait(object):
    """
        Native find element wait
    """

    CLASS_NAME = "Native_wait___"

    def __init__(self, driver, timeout, poll_frequency=POLL_FREQUENCY, ignored_exceptions=None):
        """
        Constructor, takes a WebDriver instance and timeout in seconds.

           :Args:
            - Waitdriver - Instance of WebDriver (Ie, Firefox, Chrome or Remote)
            - timeout - Number of seconds before timing out
            - poll_frequency - sleep interval between calls
              By default, it is 0.5 second.
            - ignored_exceptions - iterable structure of exception classes ignored during calls.
              By default, it contains NoSuchElementException only.

           Example:
            from selenium.webdriver.support.ui import WebDriverWait \n
            element = WebDriverWait(driver, 10).until(lambda x: x.find_element_by_id("someId")) \n
            is_disappeared = WebDriverWait(driver, 30, 1, (ElementNotVisibleException)).\ \n
                        until_not(lambda x: x.find_element_by_id("someId").is_displayed())
        """
        self._driver = driver
        self._timeout = timeout
        self._poll = poll_frequency
        # avoid the divide by zero
        if self._poll == 0:
            self._poll = POLL_FREQUENCY
        exceptions = list(IGNORED_EXCEPTIONS)
        if ignored_exceptions is not None:
            try:
                exceptions.extend(iter(ignored_exceptions))
            except TypeError:  # ignored_exceptions is not iterable
                exceptions.append(ignored_exceptions)
        self._ignored_exceptions = tuple(exceptions)

    def __repr__(self):
        return '<{0.__module__}.{0.__name__} (session="{1}")>'.format(
            type(self), self._driver.session_id)

    def until(self, method, message=''):
        """
            Calls the method provided with the driver as an argument until the \
            return value is not False.
        """
        screen = None
        stacktrace = None

        end_time = time.time() + self._timeout
        value = None
        while True:
            try:
                value = method(self._driver)
                if value:
                    return value
            except self._ignored_exceptions as exc:
                screen = getattr(exc, 'screen', None)
                stacktrace = getattr(exc, 'stacktrace', None)
            time.sleep(self._poll)
            if time.time() > end_time:
                logger.exception(self.CLASS_NAME + " cannot find elements after wait-time-out!")
                try:
                    res = run_all_methods(self._driver)
                except NoSuchElementException:
                    logger.error(self.CLASS_NAME+" occur error when run white list")
                    screen_shot(driver=self._driver, filename=self.CLASS_NAME + ".png")
                    raise NoSuchElementException(message, screen, stacktrace)
                value = method(self._driver)
                if value:
                    return value
                elif not value and not res:
                    return self.until(method, message='')
                elif not value and res:
                    logger.error(self.CLASS_NAME + " cannot find element and don't exist in white list")
                    screen_shot(driver=self._driver, filename=self.CLASS_NAME + ".png")
                    raise NoSuchElementException(message, screen, stacktrace)
        return value

    def until_not(self, method, message=''):
        """
            Calls the method provided with the driver as an argument until the \
            return value is False.
        """
        end_time = time.time() + self._timeout
        while True:
            try:
                value = method(self._driver)
                if not value:
                    return value
            except self._ignored_exceptions:
                return True
            time.sleep(self._poll)
            if time.time() > end_time:
                break
        raise TimeoutException(message)
