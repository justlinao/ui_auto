import os

from Public.connect_devices import connect
import time
'''
反复启动杀进程操作，测试保活SDK的crash
'''


def start():
    d = connect()
    d.app_start("com.hellogeek.fycleanking")
    cold = d(resourceId='com.hellogeek.fycleanking:id/tvNewPlusCleanTitle')
    if cold.wait(True, timeout=15):
        time.sleep(1)
        d(resourceId="com.hellogeek.fycleanking:id/tv_clean_up").click()
        time.sleep(1)
        d.app_stop("com.hellogeek.fycleanking")
    else:
        time.sleep(5)
        d.app_stop("com.hellogeek.fycleanking")


if __name__ == '__main__':
    for i in range(100):
        start()
        print("-------已执行 %s 次-------" % i)
