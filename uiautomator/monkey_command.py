# -*-coding:utf-8-*-
"""
@Author:LN
"""

import os


def monkey(**kwargs):  # 缺省方法
    command = "adb shell monkey"
    try:
        command += " -p "+kwargs["packageName"]
    except:
        print("没有指定包")
    command += " -v "
    try:
        command += kwargs["count"]
    except:
        print("没有指定次数")
    try:
        command += " -s " + kwargs["seed"]
    except:
        print("没有指定种子数")
    try:
        command += " --throttle " + kwargs["throttle"]
        if kwargs["random"]==True:
            command += " --randomize-throttle"
        else:
            pass
    except:
        print("没有指定时间间隔")
    #print (command)
    report = os.popen(command).read()  # os.popen() 方法用于从一个命令打开一个管道。在Unix，Windows中有效
    return report