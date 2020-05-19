from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from test_po_wechat.page.login import Login
from test_po_wechat.page.register import Register


class Index():
    # driver初始化
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://work.weixin.qq.com/")
        self.driver.maximize_window()
        self.driver.implicitly_wait(3)

    def goto_login(self):
        self.driver.find_element_by_xpath("//*[@id='indexTop']/div[2]/aside/a[1]").click()
        # self.driver:传入driver，避免再次初始化driver
        return Login(self.driver)

    def goto_register(self):
        self.driver.find_element_by_xpath("//*[@id='tmp']/div[1]/a[2]").click()
        return Register(self.driver)
