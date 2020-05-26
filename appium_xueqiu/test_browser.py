from appium import webdriver


class TestBrowser():
    def setup(self):
        desired_caps = {
            "platformName": "android",
            "deviceName": "127.0.0.1：7555",
            "browserName": "Browser",
            "noReset": True,
            "unicodeKeyBoard": True,
            # "chromedriverExecutable":"E:\hogwarts\hogwarts_soft\appium-driver"
        }
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)

    def teardown(self):
        self.driver.quit()

    def test_browser_bai_du(self):
        self.driver.get("http://m.baidu.com")