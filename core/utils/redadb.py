#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    封装一下 https://github.com/google/python-adb
"""

# 解析一下ANDROID_HOME是否存在,并且已经添加到了PATH中

import sys
from subprocess import check_output, STDOUT
import core.vendor.adb_android.adb_android as ad_vendor
from core.utils.constant import PACKAGE_NAME
import logging

logger = logging.getLogger(__name__)

try:
    # 有个坑，需要配置PATH(系统的PATH和Pycharm的不同）记录在quip中 @author --Juan  这个是用pycharm
    check_output(['adb', 'version'], stderr=STDOUT)
except OSError as e:
    if e.strerror == "No such file or directory":
        print u"Error - 请设置正确的系统PATH,确保adb可以执行"
        sys.exit(-1)


class BaseAdbWrapper(object):
    def grant_permissions(self, permissions):
        raise NotImplemented


class UsbAdb(BaseAdbWrapper):
    def __init__(self, desired_caps):
        """
            :param desired_caps: standard appium desired_caps
        """
        self.desired_caps = desired_caps
        assert "deviceName" in desired_caps
        self.serial_no = desired_caps["deviceName"]

    def grant_permissions(self, permissions):
        """
            给移动端设置权限
            :param permissions:权限列表
            :return:
        """
        # adbVendor.list_granted_permisions()
        ad_vendor.grant_permissions(permissions, PACKAGE_NAME)


if __name__ == "__main__":
    pass
