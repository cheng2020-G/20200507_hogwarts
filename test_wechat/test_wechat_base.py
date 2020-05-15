from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class TestBase():
    def setup(self):
        # 复用浏览器
        chrome_options = Options()
        chrome_options.debugger_address = "127.0.0.1:9666"
        # self.driver = webdriver.Chrome(options=chrome_options)
        # 不复用浏览器
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(3)

    def teardown(self):
        self.driver.quit()
