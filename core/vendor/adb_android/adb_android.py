# -*- coding: utf-8 -*-

"""封装adb的常用命令"""

import tempfile
import core.vendor.adb_android.var as v
import re
import logging
import os
import time
from core.utils.constant import PROJECT_PATH
from subprocess import check_output, CalledProcessError, call

logger = logging.getLogger(__name__)


def connect_remote_devices(remote_address=None):
    """
    adb remote-devices
    :param remote_address:
    :return:
    """
    logger.info(" start remote adb server ")
    if remote_address is None:
        logger.info(" remote address cannot empty ")
        return
    adb_connect_remote_devices_cmd = [v.ADB_COMMAND_PREFIX, v.ADB_COMMAND_CONNECT, remote_address]
    return _exec_command(adb_cmd=adb_connect_remote_devices_cmd)


def get_phone_version():
    """
    get phone version
    """
    cmd = [v.ADB_COMMAND_PREFIX, v.ADB_COMMAND_SHELL, 'getprop ro.build.version.release']
    return _exec_command(cmd)


def screen_shot(pics_name=None):
    """
    设备截图
    如果是远程，这个函数只实现本地的adb
    ############--流程--###########
    发命令给  appium（container 中）-》adb（container 中）-》device（保存在devices上）
    然后
    通过命令拷贝流程， 从 device-》container-》本地
    """
    logger.info(" start screen shot")
    pc_path = os.path.join(PROJECT_PATH, "logs/screenshot")  # 本地保存地点
    mobile_path = '/data/local/tmp/tmp.png'  # 在devices上的临时存储地点
    if not os.path.isdir(pc_path):
        os.makedirs(pc_path)
    logger.info(" save path:" + pc_path)
    if pics_name is None:
        pics_name = time.strftime('%Y-%m-%d-%H:%M:%S', time.localtime(time.time()))
    wait_for_device()
    adb_screen_cap_cmd = v.ADB_COMMAND_SCREENCAP + " " + v.ADB_COMMAND_PARAMETERS_P + " " + mobile_path
    shell(adb_screen_cap_cmd)
    pull(mobile_path, os.path.join(pc_path, pics_name + ".png"))
    os.popen("adb shell rm /data/local/tmp/tmp.png")
    adb_rm_cmd = v.ADB_COMMAND_RM + " " + mobile_path
    shell(adb_rm_cmd)
    logger.info(" success screen shot")
    return True


def find_devices():
    """
    find devices
    """
    adb_full_cmd = [v.ADB_COMMAND_PREFIX, v.ADB_COMMAND_DEVICES]
    rst = _exec_command(adb_full_cmd)
    devices = re.findall('r(.*?)\s+device', rst)
    if len(devices) > 1:
        deviceIds = devices[1:]
        logger.info('total find %s devices' % str(len(devices) - 1))
        for i in deviceIds:
            logger.info('ID is %s' % i)
        return deviceIds
    else:
        logger.info('cannot find devices，please check')
        return


def _is_device_available():
    """
    Private Function to check if device is available;
    To be used by only functions inside module
    :return: True or False
    """
    result = get_serial_no()
    if result[1].strip() == "unknown":
        return False
    else:
        return True


def version():
    """
    Display the version of adb
    :return: result of _exec_command() execution
    """
    adb_full_cmd = [v.ADB_COMMAND_PREFIX, v.ADB_COMMAND_VERSION]
    return _exec_command(adb_full_cmd)


def bug_report(dest_file="default.log"):
    """
    Prints dumpsys, dumpstate, and logcat data to the screen, for the purposes of bug reporting
    :return: result of _exec_command() execution
    """
    adb_full_cmd = [v.ADB_COMMAND_PREFIX, v.ADB_COMMAND_BUGREPORT]
    try:
        dest_file_handler = open(dest_file, "w")
    except IOError:
        print "IOError: Failed to create a log file"

    # We have to check if device is available or not before executing this command
    # as adb bugreport will wait-for-device infinitely and does not come out of 
    # loop
    # Execute only if device is available only
    if _is_device_available():
        result = _exec_command_to_file(adb_full_cmd, dest_file_handler)
        return result, "Success: Bug report saved to: " + dest_file
    else:
        return 0, "Device Not Found"


def push(src, dest):
    """
    Push object from host to target
    :param src: string path to source object on host
    :param dest: string destination path on target
    :return: result of _exec_command() execution
    """
    adb_full_cmd = [v.ADB_COMMAND_PREFIX, v.ADB_COMMAND_PUSH, src, dest]
    return _exec_command(adb_full_cmd)


def pull(src, dest):
    """
    Pull object from target to host
    :param src: string path of object on target
    :param dest: string destination path on host
    :return: result of _exec_command() execution
    """
    adb_full_cmd = [v.ADB_COMMAND_PREFIX, v.ADB_COMMAND_PULL, src, dest]
    return _exec_command(adb_full_cmd)


def devices(opts=[]):
    """
    Get list of all available devices including emulators
    :param opts: list command options (e.g. ["-r", "-a"])
    :return: result of _exec_command() execution
    """
    adb_full_cmd = [v.ADB_COMMAND_PREFIX, v.ADB_COMMAND_DEVICES, _convert_opts(opts)]
    return _exec_command(adb_full_cmd)


def shell(cmd):
    """
    Execute shell command on target
    :param cmd: string shell command to execute
    :return: result of _exec_command() execution
    """
    adb_full_cmd = [v.ADB_COMMAND_PREFIX, v.ADB_COMMAND_SHELL, cmd]
    return _exec_command(adb_full_cmd)


def install(apk, opts=[]):
    """
    Install *.apk on target
    :param apk: string path to apk on host to install
    :param opts: list command options (e.g. ["-r", "-a"])
    :return: result of _exec_command() execution
    """
    adb_full_cmd = [v.ADB_COMMAND_PREFIX, v.ADB_COMMAND_INSTALL, _convert_opts(opts), apk]
    return _exec_command(adb_full_cmd)


def uninstall(app, opts=[]):
    """
    Uninstall app from target
    :param app: app name to uninstall from target (e.g. "com.example.android.valid")
    :param opts: list command options (e.g. ["-r", "-a"])
    :return: result of _exec_command() execution
    """
    adb_full_cmd = [v.ADB_COMMAND_PREFIX, v.ADB_COMMAND_UNINSTALL, _convert_opts(opts), app]
    return _exec_command(adb_full_cmd)


def get_serial_no():
    """
    Get serial number for all available target devices
    :return: result of _exec_command() execution
    """
    adb_full_cmd = [v.ADB_COMMAND_PREFIX, v.ADB_COMMAND_GETSERIALNO]
    return _exec_command(adb_full_cmd)


def wait_for_device():
    """
    Block execution until the device is online
    :return: result of _exec_command() execution
    """
    adb_full_cmd = [v.ADB_COMMAND_PREFIX, v.ADB_COMMAND_WAITFORDEVICE]
    return _exec_command(adb_full_cmd)


def sync():
    """
    Copy host->device only if changed
    :return: result of _exec_command() execution
    """
    adb_full_cmd = [v.ADB_COMMAND_PREFIX, v.ADB_COMMAND_SHELL, v.ADB_COMMAND_SYNC]
    return _exec_command(adb_full_cmd)


def start_server():
    """
    Startd adb server daemon on host
    :return: result of _exec_command() execution
    """
    adb_full_cmd = [v.ADB_COMMAND_PREFIX, v.ADB_COMMAND_START_SERVER]
    return _exec_command(adb_full_cmd)


def kill_server():
    """
    Kill adb server daemon on host
    :return: result of _exec_command() execution
    """
    adb_full_cmd = [v.ADB_COMMAND_PREFIX, v.ADB_COMMAND_KILL_SERVER]
    return _exec_command(adb_full_cmd)


def get_state():
    """
    Get state of device connected per adb
    :return: result of _exec_command() execution
    """
    adb_full_cmd = [v.ADB_COMMAND_PREFIX, v.ADB_COMMAND_GET_STATE]
    return _exec_command(adb_full_cmd)


def _convert_opts(opts):
    """
    Convert list with command options to single string value
    with 'space' delimeter
    :param opts: list with space-delimeted values
    :return: string with space-delimeted values
    """
    return ' '.join(opts)


def list_granted_permissions(package_name):
    """
    获取移动端的制定app的已有权限
    @author 这个函数没没有测过，如果使用，请先测试
    :return:
    """
    granted_permissions = []
    result = _exec_command([v.ADB_COMMAND_PREFIX, v.ADB_COMMAND_SHELL,
                            v.ADB_COMMAND_PM, v.ADB_COMMAND_LIST, v.ADB_COMMAND_PERMISSIONS])[1]

    logger.info("result:", result)
    for x in result.split("\r"):
        if x("permission:" + package_name + ".permission"):
            granted_permissions.append(x)
    return granted_permissions


def grant_permissions(permissions, package_name):
    """
    给移动端授权（android）
    :param adb_cmds: 权限列表
    :return:
    """
    results = []
    for p in permissions:
        results.append(_exec_command(
            [v.ADB_COMMAND_PREFIX, v.ADB_COMMAND_SHELL, v.ADB_COMMAND_PM, v.ADB_COMMAND_GRANT, package_name, p]))
    return results


def _exec_command(adb_cmd):
    """
    Format adb command and execute it in shell
    :param adb_cmd: list adb command to execute
    :return: string '0' and shell command output if successful, otherwise
    raise CalledProcessError exception and return error code
    """
    t = tempfile.TemporaryFile()
    final_adb_cmd = []
    for e in adb_cmd:
        if e != '':  # avoid items with empty string...
            final_adb_cmd.append(e)  # ... so that final command doesn't
            # contain extra spaces
    logger.info(' --- Executing adb command : ' + ' '.join(adb_cmd))

    try:
        output = check_output(final_adb_cmd, stderr=t)
    except CalledProcessError as e:
        logger.exception(e.message)
        t.seek(0)
        result = e.returncode, t.read()
    else:
        result = 0, output
        logger.info(u' 运行正确：' + result[1])

    return result


def _exec_command_to_file(adb_cmd, dest_file_handler):
    """
    Format adb command and execute it in shell and redirects to a file
    :param adb_cmd: list adb command to execute
    :param dest_file_handler: file handler to which output will be redirected
    :return: string '0' and writes shell command output to file if successful, otherwise
    raise CalledProcessError exception and return error code
    """
    t = tempfile.TemporaryFile()
    final_adb_cmd = []
    for e in adb_cmd:
        if e != '':  # avoid items with empty string...
            final_adb_cmd.append(e)  # ... so that final command doesn't
            # contain extra spaces
    print('*** Executing ' + ' '.join(adb_cmd) + ' ' + 'command')

    try:
        output = call(final_adb_cmd, stdout=dest_file_handler, stderr=t)
    except CalledProcessError as e:
        t.seek(0)
        result = e.returncode, t.read()
    else:
        result = output
        dest_file_handler.close()

    return result
