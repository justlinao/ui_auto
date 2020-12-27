from Public.connect_devices import connect
import time
d = connect()


def click():
    d.click(0.627, 0.073)  # 点击用户头像
    time.sleep(0.5)
    d.click(0.557, 0.434)  # 关闭头像弹框
    d.xpath('//*[@resource-id="com.xiaoniu.showlive:id/oper_bottom_view"]/'
            'android.widget.LinearLayout[1]/android.widget.RelativeLayout[1]').click()  # 打开礼物面板
    gift_three = d.xpath(
        '//*[@resource-id="com.xiaoniu.showlive:id/recyler_view"]/android.view.ViewGroup[3]'
        '/android.widget.ImageView[1]')
    gift_three.click()
    d.click(0.557, 0.434)  # 关闭礼物面板
    d(resourceId="com.xiaoniu.showlive:id/iv_wx").click()  # 点开微信分享
    time.sleep(1)
    d.click(0.557, 0.434)  # 关闭微信分享

    d.xpath('//*[@resource-id="com.xiaoniu.showlive:id/oper_bottom_view"]/'
            'android.widget.LinearLayout[1]/android.widget.RelativeLayout[1]').click()  # 打开礼物面板
    time.sleep(0.2)


for i in range(1000):
    click()
