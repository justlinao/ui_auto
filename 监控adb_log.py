import os, threading, datetime

# 获取当前文件所在目录，拼接出LOG路径
import subprocess

abs_path = os.path.abspath(__file__)  # 打印此文件的绝对路径
path = os.path.dirname(abs_path)  # 返回此文件的上级目录
log_path = os.path.join(path, "log")  # 拼接一个目录 E:\Code\uiautomator\log

# 配置需要监控的关键字
keywords = ["finished inst ", "NullPointerException", "CRASH", "Force Closed"]

# 控制开启和关闭
STOP_LOGCAT = True

# 指令对应具体操作
INSTRUCTION = {"1": "filter_keywords", "2": "stop_filter_keywords", "3": "exit"}


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


# 监控关键字主函数，
def filter_keywords():
    global STOP_LOGCAT
    STOP_LOGCAT = False
    devices = get_devices()  # 先获取所有连接的设备
    print("开始监控关键字")
    for device in devices:
        t = threading.Thread(target=filter_keyword, args=(device,))
        t.start()


def stop_filter_keywords():
    global STOP_LOGCAT
    if STOP_LOGCAT:
        print("没有正在执行的任务\n")
    else:
        STOP_LOGCAT = True
        print("正在停止关键字监控\n")

# 通过 subprocess.Popen 创建进程执行命令，持续输出日志到 stdout


def logcat(device):
    """
    logcat持续输出日志
    :param device:
    :return:
    """
    command = "adb -s " + str(device) + " logcat -v time"
    sub = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    print(sub.stdout)
    return sub


# 获取日志存放路径，如果不存在则按日期创建
def get_log_path(tag):
    year = datetime.datetime.now().strftime('%Y')
    month = datetime.datetime.now().strftime('%m')
    day = datetime.datetime.now().strftime('%d')
    path = os.path.join(log_path, tag, year, month, day)
    if not os.path.exists(path):
        os.makedirs(path)
    return path


# 打包下载所有日志到当前目录
def bugreport(device, path):
    os.chdir(path)  # bugreport会下载日志到当前文件夹，所以需要先切换到已经创建的目录
    command = "adb -s " + str(device) + " bugreport"
    subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, bufsize=-1)
    print("设备：%s 日志路径：%s" % (str(device), path))


def filter_keyword(device):
    print("设备%s关键字监控已开启" % str(device))
    sub = logcat(device)
    with sub:
        for line in sub.stdout:  # 子进程会持续输出日志，对子进程对象.stdout进行循环读取
            for key in keywords:
                if line.decode("utf-8").find(key) != -1:  # stdout输出为字节类型，需要转码
                    message = "设备：%s 检测到：%s\n" % (device, key)  # 设备：192.168.56.104:5555 检测到：ANR
                    path = get_log_path("bugreport")  # 根据时间创建文件夹
                    bugreport(device, path)  # 拉取完整日志压缩包到创建的文件夹内
                    # send_message(message)  # 这里可以换成自己要做的事情，比如发送邮件或钉钉通知
                else:
                    bugreport(device, path)
            if STOP_LOGCAT:
                break

        print("设备%s关键字监控已停止" % str(device))
        sub.kill()


def main():
    while True:
        print("-" * 100)
        print("1：开启关键字监控\n2：停止关键字监控\n3：退出")
        print("-" * 100)
        instruction = str(input("\n\n请输入要进行的操作号：\n"))
        print("-" * 100)
        while instruction not in INSTRUCTION.keys():
            instruction = str(input("\n\n输入无效，请重新输入:"))
        if int(instruction) == 9:
            exit()  # TODO 退出前需要判断是否有正在执行的monkey任务和关键字监控任务

        eval(INSTRUCTION[str(instruction)] + "()")


if __name__ == '__main__':
    main()
