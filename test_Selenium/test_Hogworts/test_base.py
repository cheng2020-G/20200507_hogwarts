# 基础类
import os

from selenium import webdriver


class TestBase():
    def setup(self):
        # 定义多浏览器变量，获取虚拟环境brower，用于浏览器driver判断
        browser = os.getenv("browser")
        if browser == "chrome":
            self.driver = webdriver.Ie()
        elif browser == "firefox":
            self.driver = webdriver.Firefox()
        else:
            self.driver = webdriver.Chrome()

        self.driver.maximize_window()
        self.driver.implicitly_wait(3)

    def teardown(self):
        self.driver.quit()
