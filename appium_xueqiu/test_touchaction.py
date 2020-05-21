import pytest
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction


class TestTouchAction():
    def setup(self):
        desried_caps = {
            "platformName": "android",
            "deviceName": "127.0.0.1:7555",
            "appPackage": "com.xueqiu.android",
            "appActivity": ".view.WelcomeActivityAlias",
            "noReset": True,
            "unicodeKeyBoard": True
        }
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desried_caps)
        self.driver.implicitly_wait(3)

    def teardown(self):
        self.driver.quit()

    @pytest.mark.skip
    def test_touch_action(self):
        action = TouchAction(self.driver)
        # 坐标点不建议写死
        # action.press(x=371, y=1018).wait(300).move_to(x=371, y=421).wait(300).release().perform()
        # 坐标点变量化
        # print(self.driver.get_window_rect())
        window_rect = self.driver.get_window_rect()
        width = window_rect['width']
        height = window_rect['height']
        x_begin = int(width/2)
        y_begin = int(height * 4/5)
        y_end = int(height * 1/5)
        action.press(x=x_begin, y=y_begin).move_to(x=x_begin, y=y_end).release().perform()

    # @pytest.mark.skip
    def test_touch_action_case02(self):
        action = TouchAction(self.driver)

