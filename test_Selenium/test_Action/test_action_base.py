import os

from selenium import webdriver


class TestAction():
    def setup(self):
        # 使用action时，不支持w3c，在setup方法中定义各driver的option，
        option_chrome = webdriver.ChromeOptions()
        option_chrome.add_experimental_option('w3c', False)
        option_ie = webdriver.IeOptions()
        option_ie.add_additional_option('w3c', False)

        # 定义用于执行用例的浏览器
        browser = os.getenv("browser")
        if browser == "ie":
            self.driver = webdriver.Ie(options=option_ie)
        elif browser == "friefox":
            self.driver = webdriver.Firefox()
        else:
            self.driver = webdriver.Chrome(options=option_chrome)
        # 窗口最大化
        self.driver.maximize_window()
        # 隐式等待3s
        self.driver.implicitly_wait(3)

    def teardown(self):
        # 浏览器退出
        self.driver.quit()
