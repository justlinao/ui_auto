from Public.connect_devices import connect
d = connect()
import unittest
from Public.Assert import assert_i


class HomePage(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def test_homepage(self):
        zongheyubao = d.xpath(
            '//me.majiajie.pagerbottomtabstrip.internal.CustomItemLayout/android.widget.FrameLayout[1]'
            '/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.ImageView[1]')
        assert_i(zongheyubao, "综合预报tab", "综合预报tab")
        fifteen = d.xpath('//me.majiajie.pagerbottomtabstrip.internal.CustomItemLayout/android.widget.'
                          'FrameLayout[2]/android.widget.LinearLayout[1]/android.widget.'
                          'FrameLayout[1]/android.widget.ImageView[1]')
        assert_i(fifteen, "15天预报tab", "15天预报tab")
        airquality = d.xpath('//me.majiajie.pagerbottomtabstrip.internal.CustomItemLayout/'
                             'android.widget.FrameLayout[3]/android.widget.LinearLayout[1]/android.widget.'
                             'FrameLayout[1]/android.widget.ImageView[1]')
        assert_i(airquality, "空气质量tab", "空气质量tab")
        samllvedio = d.xpath('//me.majiajie.pagerbottomtabstrip.internal.CustomItemLayout/android.widget.'
                             'FrameLayout[4]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/'
                             'android.widget.ImageView[1]')
        assert_i(samllvedio, "小视频tab", "小视频tab")

    def tearDown(self) -> None:
        pass


if __name__ == '__main__':
    unittest.main()
