#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Function：define some functions
    @date 2017/05/23
    @author Juan Liu
"""
import logging
import os
import time

from constant import SCREEN_SHOT_PC_PATH

logger = logging.getLogger(__name__)


def screen_shot(driver=None, filename=None):
    """
        screen shot
        Args:
        filename: the path to save pictures
    """
    logger.info(" begin screen shot ")
    if driver is None:
        logger.info("no driver to used screen shot.")
        return False
    if not os.path.isdir(SCREEN_SHOT_PC_PATH):
        os.makedirs(SCREEN_SHOT_PC_PATH)
    time_tag = time.strftime('%Y-%m-%d-%H:%M:%S', time.localtime(time.time()))
    if filename is None:
        filename = time.strftime('%Y-%m-%d-%H:%M:%S', time.localtime(time.time())) + ".png"
    else:
        filename = time_tag + filename
    filename = os.path.join(SCREEN_SHOT_PC_PATH, filename)
    logger.info("The screen shot pictures saved in container path is :" + filename)
    png = driver.get_screenshot_as_png()
    try:
        with open(filename, 'wb') as f:
            f.write(png)
    except IOError:
        return False
    finally:
        del png
    logger.info(" success screen shot.")
    return True


def switch_context(driver, context="WEBVIEW_com.xingin.xhs"):
    """
    if context different current context
        Native->To->Webview  or Webview->to->Native
    else
        donn't change
    """
    contexts = driver.contexts
    if context in contexts:
        logger.info("change to " + context + " context.")
        driver.switch_to.context(context)
        return True
    else:
        logger.error("cannot change context and current context is " + str(driver.context))
        return False
