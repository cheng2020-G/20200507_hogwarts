from selenium import webdriver


class TestAction():
    def setup(self):
        # 使用action时，不支持w3c，再setup方法中定义option，
        option = webdriver.ChromeOptions()
        option.add_experimental_option('w3c', False)
        self.driver = webdriver.Chrome(options=option)
        self.driver.maximize_window()
        self.driver.implicitly_wait(3)

    def teardown(self):
        self.driver.quit()
