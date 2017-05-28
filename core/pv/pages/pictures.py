#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    发布笔记过程中，关于照片的选择，处理，笔记的编写等中间各个流程
"""

from core.pv.pages import BasePage
import logging

logger = logging.getLogger(__name__)


class PicturesPage(BasePage):
    """发布笔记时候，点击的照片页面"""
    PAGE_NAME = u"发布笔记选择照片界面--->"

    def __init__(self, driver):
        super(PicturesPage, self).__init__(driver)

    def get_all_pictures(self):
        """获取所有的图片"""
        logger.info(self.PAGE_NAME + u"获取所有图片")
        return self.ui_locator.find_elements_by_android_uiautomator('new UiSelector().resourceId('
                                                                    '"com.xingin.xhs:id/img_select")')

    def get_take_pictures_image_view(self):
        """获得拍照按钮"""
        logger.info(self.PAGE_NAME + u"获取拍照按钮")
        select_str = 'new UiSelector().resourceId("com.xingin.xhs:id/rv").' \
                     'childSelector(new UiSelector().className("android.widget.RelativeLayout"))'
        return self.ui_locator.find_element_by_android_uiautomator(select_str)

    def get_continue_text_view(self):
        """获得继续action"""
        logger.info(self.PAGE_NAME + u"获取继续按钮")
        return self.ui_locator.find_element_by_android_uiautomator('new UiSelector().text("继续")')


class TakePicturePage(BasePage):
    """拍摄照片（摄像头）界面"""
    PAGE_NAME = u"摄像头页面--->"

    def __init__(self, driver):
        super(TakePicturePage, self).__init__(driver)

    def get_take_pictures_button(self):
        """获取拍摄按钮"""
        return self.ui_locator.find_element_by_id("com.xingin.xhs:id/takepicture")


class EditPicturesPage(BasePage):
    """编辑照片的界面"""

    PAGE_NAME = u"编辑照片页面--->"

    def __init__(self, driver):
        super(EditPicturesPage, self).__init__(driver)

    def get_continue_text_view(self):
        """获得继续action"""
        logger.info(self.PAGE_NAME + u"获取继续按钮")
        return self.ui_locator.find_element_by_android_uiautomator('new UiSelector().text("继续")')


class DeliverNotePage(BasePage):
    """发布笔记页面"""

    PAGE_NAME = u"发布笔记页面--->"

    def __init__(self, driver):
        super(DeliverNotePage, self).__init__(driver)

    def get_title_text_view(self):
        """获得发布笔记的标题"""
        logger.info(self.PAGE_NAME + u"获取发布笔记标题文本框")
        return self.ui_locator.find_element_by_id("com.xingin.xhs:id/title_tv")

    class ClickEditTextOccurPage(BasePage):
        """点击发布笔记中文本框出现的界面"""
        PAGE_NAME = u"点击发布笔记中文本框出现的界面--->"

        def get_title_text_edit(self):
            """获取标题文本框"""
            logger.info(self.PAGE_NAME + u"获取点击之后的发布笔记标题的文本框")
            return self.ui_locator.find_element_by_id("com.xingin.xhs:id/title_et")

        def get_confirm_button(self):
            """获取确认按钮"""
            logger.info(self.PAGE_NAME+u"获取确认按钮")
            return self.ui_locator.find_element_by_android_uiautomator('new UiSelector().text("确定")')

    def get_deliver_button(self):
        """获得发布笔记按钮"""
        logger.info(self.PAGE_NAME + u"获取发布笔记按钮")
        return self.ui_locator.find_element_by_id("com.xingin.xhs:id/postBtn")

    def get_weixin_share_image_view(self):
        """获得分享按钮"""
        logger.info(self.PAGE_NAME + u"获取微信分享图标")
        return self.ui_locator.find_element_by_id("com.xingin.xhs:id/share_weixin")
