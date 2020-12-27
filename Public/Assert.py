#!/user/bin/env python
# coding:utf-8
from Public.connect_devices import connect
import time
d = connect()
import os


def assert_i(element, msg, screenshotname):
    nowtime = time.strftime("%Y-%m-%d %H-%M-%S", time.localtime())
    path = os.getcwd()
    path = os.path.dirname(path) + '\\Screenshot\\'
    screenpath = path + screenshotname + ' ' + nowtime
    if element.wait(timeout=10):
        print(msg + ' ......pass......')
    else:
        d.screenshot(screenpath + '.png')
        raise AssertionError(msg + ' ......fail......')
