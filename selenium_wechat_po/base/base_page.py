from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webdriver import WebDriver


class BasePage():
    driver = None
    base_url = ""

    def __init__(self, driver: WebDriver = None):
        if driver is None:
            chrome_option = Options()
            chrome_option.debugger_address = "127.0.0.1:9666"
            self.driver = webdriver.Chrome(options=chrome_option)
            self.driver.maximize_window()
            self.driver.implicitly_wait(3)
        else:
            self.driver = driver
        if self.base_url != None:
            self.driver.get(self.base_url)

    def find(self, by, location):
        return self.driver.find_element(by, location)

    def finds(self, by, location):
        return self.driver.find_elements(by, location)
