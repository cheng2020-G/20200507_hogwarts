import yaml
from appium import webdriver

from po_change.page.base_page import BasePage
from po_change.page.main import Main


class App(BasePage):
    _package = "com.xueqiu.android"
    _activity = ".common.MainActivity"

    def start(self):
        if self._driver is None:
            caps = {
                "platformName": "android",
                "deviceName": "127.0.0.1：7555",
                "appPackage": self._package,
                "appActivity": self._activity,
                "noReset": True,
                "unicodeKeyBoard": True,
                # 配置的数据驱动
                # "udid": yaml.safe_load(open("D:\PycharmProject/20200507_pytest_calc\po_change/test_case\Config.yaml"))["caps"]["udid"]
            }
            self._driver = webdriver.Remote("127.0.0.1:4723/wd/hub", caps)
        else:
            self._driver.start_activity(self._package, self._activity)

        self._driver.implicitly_wait(3)

        return self

    def main(self) -> Main:
        return Main(self._driver)
