from Public.connect_devices import connect
import time
d = connect()


def send_gift():

    gift_three = d.xpath(
        '//*[@resource-id="com.xiaoniu.showlive:id/recyler_view"]/android.view.ViewGroup[3]'
        '/android.widget.ImageView[1]')
    if gift_three.exists:
        for i in range(10000):
            gift_three.click()  # 送第三个礼物
            time.sleep(0.2)
            print("----------已送礼 %s 次------------" % i)
    else:
        d.click(0.486, 0.258)  # 点击空白区域，收起礼物面板
        d.xpath('//*[@resource-id="com.xiaoniu.showlive:id/oper_bottom_view"]/'
                'android.widget.LinearLayout[1]/android.widget.RelativeLayout[1]').click()  # 打开礼物面板
        for i in range(10000):
            gift_three.click()  # 送第三个礼物
            time.sleep(0.2)
            print("----------已送礼 %s 次------------" % i)


send_gift()
