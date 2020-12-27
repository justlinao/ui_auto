from Public.connect_devices import connect

d = connect()
import time


def test():
    starttime = time.time()
    try:
        d.implicitly_wait(5)
        d.xpath("//*[@resource-id='com.geek.xycalendar:id/iv_feed_lis']").click()
    except:
        print('没找到')
    endtime = time.time()
    count_time = endtime - starttime
    print(count_time)



test()