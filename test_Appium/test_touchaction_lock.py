from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction


class TestTouchActionLock():
    def setup(self):
        desried_caps = {
            "platformName": "android",
            "deviceName": "127.0.0.1:7555",
            "appPackage": "cn.kmob.screenfingermovelock",
            "appActivity": "com.samsung.ui.MainActivity",
            "noReset": True,
            "unicodeKeyBoard": True
        }
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desried_caps)
        self.driver.implicitly_wait(3)

    def teardown(self):
        self.driver.quit()

    def test_touch_action_lock(self):
        # self.driver.find_element_by_xpath("//*[@resource_id='cn.kmob.screenfingermovelock:id/lockerCheckBox' and @class='android.widget.ImageView']").click()
        action = TouchAction(self.driver)
        action.press(x=120, y=180).wait(200).move_to(x=360, y=180).wait(200).move_to(x=600, y=180).wait(200).move_to(
            x=600, y=420).wait(200).move_to(x=600, y=660).release().perform()
