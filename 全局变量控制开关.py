stop_t = True
instraction = {"1": "fuc", "2": "stop"}


def fuc():
    count = 0
    global stop_t
    stop_t = False
    for i in range(1000):
        count += 1
        print("hello world")
        if count == 100:
            pass
        if stop_t:
            print('我被停止了')
            break


def stop():
    global stop_t
    if stop_t:
        print('1')
    else:
        stop_t = True
        print('2')


if __name__ == '__main__':
    while True:
        print("-" * 100)
        print("1：开启关键字监控\n2：停止关键字监控\n3：退出")
        print("-" * 100)
        instrac = int(input("请输入你的指令："))
        eval(instraction[str(instrac)]+"()")
