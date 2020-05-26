from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestWebView():
    def setup(self):
        desired_caps = {
            "platformName": "android",
            "deviceName": "127.0.0.1：7555",
            "appPackage": "com.xueqiu.android",
            "appActivity": ".view.WelcomeActivityAlias",
            "noReset": True,
            "unicodeKeyBoard": True,
            "chromedriverExcutable":"",
            "skip":""
        }
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)

    def teardown(self):
        self.driver.quit()

    def test_xueqiu_webview(self):
        # 点击交易
        # 获取context
        contexts = self.driver.contexts
        # 切换上下文
        self.driver.switch_to.context(self.driver.contexts[-1])
        # 点击‘A股开户’ 加显示等待
        A_location = (MobileBy.XPATH, "")
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(A_location))
        self.driver.find_element(*A_location).click()
        # 输入手机号
        # 输入验证码
        # 点击登录
