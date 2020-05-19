from selenium.webdriver.remote.webdriver import WebDriver

from test_po_wechat.page.register import Register


class Login():
    # 复用driver
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def scanf(self):
        pass

    def goto_register(self):
        self.driver.find_element_by_xpath("//*[@id='wework_admin.loginpage_wx_$']/main/div[2]/a").click()
        return Register(self.driver)
