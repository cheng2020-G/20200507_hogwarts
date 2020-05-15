from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class TestBase():
    def setup(self):
        # 复用浏览器
        options = Options()
        options.debugger_address = "127.0.0.1:9333"
        self.driver = webdriver.Chrome(options=options)
        # 不复用浏览器
        # self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(3)

    def teardown(self):
        self.driver.quit()
