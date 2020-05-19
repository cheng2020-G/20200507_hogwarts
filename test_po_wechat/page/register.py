from selenium.webdriver.remote.webdriver import WebDriver


class Register():
    def __init__(self, driver: WebDriver):
        self.driver = driver
    def register(self):
        self.driver.find_element_by_id("corp_name").send_keys("hogwarts")
        self.driver.find_element_by_id("manager_name").send_keys("tester")
        self.driver.find_element_by_id("register_tel").send_keys("15800000000")
        self.driver.quit()
        return True