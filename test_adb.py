import subprocess
import os

# 控制开启和关闭
STOP_LOGCAT = True
# 配置需要监控的关键字
keywords = ["getBoolean", "NullPointerException", "CRASH", "Force Closed", "ENTER"]
# 指令对应具体操作
INSTRUCTION = {"1": "filter_keyword", "2": "stop_filter_keywords", "3": "exit"}


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


# 获取log_path
def log_path(tag):
    ab_path = os.path.abspath(__file__)  # 根目录
    parent_path = os.path.dirname(ab_path)  # 上级目录
    path = os.path.join(parent_path, "log", tag)
    if not os.path.exists(path):
        os.makedirs(path)
    return path


def logcat():
    """
    logcat持续输出日志
    :param :
    :return:
    """
    device = get_devices()
    command = "adb logcat | findstr com.hellogeek.fycleanking"
    sub = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    # print(sub.stdout)
    return sub


# 打包下载所有日志到当前目录
def bugreport(device, path):
    os.chdir(path)  # bugreport会下载日志到当前文件夹，所以需要先切换到已经创建的目录
    command = "adb logcat | findstr com.hellogeek.fycleanking > " + path + "log.log"
    subprocess.Popen([command, ], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, bufsize=-1)
    print("设备：%s 日志路径：%s" % (str(device), path))


def filter_keyword():
    global STOP_LOGCAT
    STOP_LOGCAT = False
    device = get_devices()
    print("设备%s关键字监控已开启" % str(device))
    sub = logcat()
    with sub:
        for line in sub.stdout:  # 子进程会持续输出日志，对子进程对象.stdout进行循环读取
            print(line.decode("utf-8"))
            for key in keywords:
                if line.decode("utf-8").find(key) != -1:  # stdout输出为字节类型，需要转码    find 方法 没有找到就返回-1
                    message = "设备：%s 检测到：%s\n" % (device, key)  # 设备： 检测到：
                    print(message)
                    path = log_path("bugreport")
                    bugreport(device, path)
                    os.killpg(os.getpgid(sub.pid), 9)
                    print("设备%s关键字监控已停止")
                    break
            if STOP_LOGCAT:
                break

        print("设备%s关键字监控已停止" % str(device))
        os.killpg(os.getpgid(sub.pid), 9)


def stop_filter_keywords():
    global STOP_LOGCAT
    if STOP_LOGCAT:
        print("没有正在执行的任务\n")
    else:
        STOP_LOGCAT = True
        print("正在停止关键字监控\n")


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
