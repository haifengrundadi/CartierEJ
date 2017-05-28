#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    功能：本模块定义了一些函数工具，用于其他类的使用
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
        截取当前app的屏幕，用于排除异常情况
        参数:
        filename: 保存截图的地址
    """
    logger.info(u" 开始截屏")
    if driver is None:
        logger.info(u"没有driver，截屏失败")
        return False
    if not os.path.isdir(SCREEN_SHOT_PC_PATH):
        os.makedirs(SCREEN_SHOT_PC_PATH)
    time_tag = time.strftime('%Y-%m-%d-%H:%M:%S', time.localtime(time.time()))
    if filename is None:
        filename = time.strftime('%Y-%m-%d-%H:%M:%S', time.localtime(time.time())) + ".png"
    else:
        filename = time_tag + filename
    filename = os.path.join(SCREEN_SHOT_PC_PATH, filename)
    logger.info(u"存储在容器中的地址为：" + filename)
    png = driver.get_screenshot_as_png()
    try:
        with open(filename, 'wb') as f:
            f.write(png)
    except IOError:
        return False
    finally:
        del png
    logger.info(u"截屏成功")
    return True


def switch_context(driver, context=u"WEBVIEW_com.xingin.xhs"):
    """
        1：环境不同，Native->To->Webview  or Webview->to->Native
        2：如果环境相同则不切换
    """
    contexts = driver.contexts
    if context in contexts:
        logger.info(u"切换到相应的环境下面")
        driver.switch_to.context(context)
        return True
    else:
        logger.error(u"没有切换到相应的环境下面，当前的环境为" + str(driver.context))
        return False
