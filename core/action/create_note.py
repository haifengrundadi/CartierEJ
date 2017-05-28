#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""创建一篇笔记"""

from core.action import BaseAction
from core.pv.pages.home import HomePage
from core.pv.pages.pictures import PicturesPage, EditPicturesPage, DeliverNotePage, TakePicturePage
import logging
import time

logger = logging.getLogger(__name__)
SLEEP_TIME = 5


class CreateNoteAction(BaseAction):
    """
        创建一篇笔记
    """
    ACTION_NAME = u"创建笔记--->"

    def __init__(self, driver):
        self.driver = driver
        self.home_page = HomePage(self.driver)

    def upload_pics_action(self):
        """
            点击上传图片
        """
        pho_btn = self.home_page.get_upload_pictures()
        logger.info(self.ACTION_NAME + u"点击右上角上传图片按钮")
        pho_btn.click()

    def select_pics_action(self, select_list=None):
        """
            从相册中选择图片
        """
        self.upload_pics_action()
        picture_page = PicturesPage(self.driver)
        els = picture_page.get_all_pictures()
        if len(els) > 0:
            if select_list is None:
                logger.info(self.ACTION_NAME + u"选择相册中默认的图片")
                els[0].click()
            else:
                # 待处理 @Juan
                logger.info(self.ACTION_NAME + u"选择相册中指定的图片")
                pass
        else:
            logger.info(self.ACTION_NAME + u"点击拍摄图标")
            picture_page.get_take_pictures_image_view().click()
            take_picture_page = TakePicturePage(self.driver)
            logger.info(self.ACTION_NAME + u"点击拍照页面拍摄按钮")
            take_picture_page.get_take_pictures_button().click()
        logger.info(self.ACTION_NAME + u"点击继续按钮")
        picture_page.get_continue_text_view().click()

    def edit_pics_action(self):
        """
            编辑照片
        """
        self.select_pics_action(select_list=None)
        edit_pictures = EditPicturesPage(self.driver)
        logger.info(self.ACTION_NAME + u"点击继续按钮")
        edit_pictures.get_continue_text_view().click()

    def deliver_note_action(self, note_title="echo-first-note"):
        """
            发布笔记
        """
        self.edit_pics_action()
        deliver_note_page = DeliverNotePage(self.driver)
        deliver_note_page.get_title_text_view().click()
        click_title_edit_page = deliver_note_page.ClickEditTextOccurPage(self.driver)
        title_edit = click_title_edit_page.get_title_text_edit()
        logger.info(self.ACTION_NAME + u" 输入笔记标题 " + note_title)
        title_edit.send_keys(note_title)
        # assert title_edit.text() == note_title
        confirm_button = click_title_edit_page.get_confirm_button()
        logger.info(self.ACTION_NAME + u"点击确定按钮")
        confirm_button.click()
        logger.info(self.ACTION_NAME + u"点击取消微信按钮")
        deliver_note_page.get_weixin_share_image_view().click()
        logger.info(self.ACTION_NAME + u"点击发布笔记按钮")
        deliver_note_page.get_deliver_button().click()
        # 休眠一段时间，用于发送数据
        time.sleep(SLEEP_TIME)
