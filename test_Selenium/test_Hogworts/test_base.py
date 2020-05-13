# 基础类
import os

from selenium import webdriver


class TestBase():
    # 定义setup方法，初始化driver,get
    # 初始化driver,可以用chrome Firefox IE 等
    # 如果没有配置环境变量，可以用executable_path="driver path",例如：self.driver = webdriver.Chrome(executable_path="D:/chromedriver_win32")
    def setup(self):
        # 定义多浏览器变量，获取虚拟环境brower传值，用于浏览器driver判断
        browser = os.getenv("browser")
        if browser == "chrome":
            self.driver = webdriver.Ie()
        elif browser == "firefox":
            self.driver = webdriver.Firefox()
        else:
            self.driver = webdriver.Chrome()

        # 窗口最大化
        self.driver.maximize_window()
        # 隐式等待
        self.driver.implicitly_wait(2)

    # 定义teardown方法，执行用例后退出
    def teardown(self):
        self.driver.quit()
