from Public.connect_devices import connect
import os
d = connect()
import unittest
from Public.Assert import assert_i


class TestOpen(unittest.TestCase):
    def setUp(self) -> None:
        print("start......")

    def test_001_star(self):
        d.app_start("com.geek.xyweather")

    def test_002_coldstartad(self):
        clodad = d(resourceId="com.geek.xyweather:id/tt_splash_skip_btn")
        assert_i(clodad, "冷启动页面", "冷启动")

    def tearDown(self) -> None:
        print("end......")


if __name__ == '__main__':
    unittest.main()
