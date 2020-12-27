from Public.connect_devices import connect

d = connect()
list = ["我不是针对谁", "我是指在座的各位都是垃圾", "我出来混的要给谁交代", "今天就是耶稣来了也留不住他", "啊伟已经死了", "你选的嘛偶像"]


def auto_chat():
    for j in range(2):
        for i in list:
            d.click(0.638, 0.966)
            d.xpath("//*[@resource-id='com.tencent.mm:id/g78']").set_text(i)
            # d(resourceId="com.tencent.mm:id/g78").send_keys('hello world')
            d(resourceId="com.tencent.mm:id/anv").click()


auto_chat()
