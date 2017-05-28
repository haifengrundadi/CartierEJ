#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    登录后的首页
"""

import logging
import time
from core.pv.pages import BasePage

logger = logging.getLogger(__name__)


class HomePage(BasePage):
    """
        登录之后的第一个界面--》主界面
    """
    PAGE_NAME = u"登录后的主页--"

    def __init__(self, driver):
        super(HomePage, self).__init__(driver)
        self.driver = driver

    def get_upload_pictures(self):
        """
            上传图片按钮
        """
        logger.info(self.PAGE_NAME + u"获取右上角上传图片按钮")
        el = self.ui_locator.find_element_by_id("com.xingin.xhs:id/photo_button")
        return el

    def get_btn_tab_shop(self):
        """
            获得进入后首页下方的tab中的购买tab
        """
        logger.info(self.PAGE_NAME + u"获取购买按钮")
        return self.ui_locator.find_element_by_id('com.xingin.xhs:id/btnTabShop')

    def get_iv_imgs(self):
        """
            单击 购买tab ---推荐页 下面的商品图片
        """
        logger.info(self.PAGE_NAME + u"每个商品的图片")
        iv_img = None
        count = 0
        while iv_img is None or len(iv_img) == 0:
            if count > 10:
                break
            self.swipe_screen_up()
            time.sleep(1)
            iv_img = self.driver.find_elements_by_android_uiautomator\
                ('new UiSelector().resourceId("com.xingin.xhs:id/iv_img")')
            logger.info(self.PAGE_NAME+u"第 "+str(count)+u" 查找！")
            count += 1

        if iv_img is not None and len(iv_img) > 0:
            logger.info(self.PAGE_NAME+u"找到了iv_img")
        else:
            logger.error(self.PAGE_NAME+u"没有找到iv_img")
            # 需要进一步处理
        return iv_img

    def get_screen_size(self):
        """
            获得机器屏幕大小x,y
        """
        logger.info(self.PAGE_NAME+u"获得机器屏幕大小x,y")
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        return (x,y)

    def swipe_screen_up(self, duration=1000):
        """
            屏幕向上滑动
        """
        logger.info(self.PAGE_NAME+ u"屏幕向上滑动")
        l = self.get_screen_size()
        logger.info(self.PAGE_NAME+ u"屏幕的宽和高为：" + str(l[0]) + " "+ str(l[1]))
        x1 = int(l[0] * 0.5)
        y1 = int(l[1] * 0.7)
        y2 = int(l[1] * 0.2)
        self.driver.swipe(x1, y1, x1, y2, duration)