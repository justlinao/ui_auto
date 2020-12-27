from Public.connect_devices import connect
d = connect()

# 私聊发言


def call():
    d(resourceId='com.xiaoniu.showlive:id/msg_edt_input').send_keys('啊啦啦啦啦啦啦啦啦啦')
    d(resourceId='com.xiaoniu.showlive:id/iv_send').click()


if __name__ == '__main__':
    for i in range(1000):
        call()
