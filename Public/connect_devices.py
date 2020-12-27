import uiautomator2 as u2
import os
'''
存放设备ID，并连接到设备
'''


# 获取所有device
def get_devices():
    command = "adb devices"
    res = os.popen(command).read()
    devices = []
    res = res.split("\n")
    for i in res:
        if i.endswith("device"):
            devices.append(i.split('\t')[0])
    return devices


# 获取单个device
def get_device():
    command = "adb devices"
    res = os.popen(command).read()
    devices = []
    res = res.split("\n")
    for i in res:
        if i.endswith("device"):
            device = i.split('\t')[0]
            return device


def connect():
    d = u2.connect_usb(get_device())
    return d




