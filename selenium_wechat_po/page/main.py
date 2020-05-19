from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from selenium_wechat_po.page.add_member import AddMember


class Main():
    def __init__(self):
        chrome_option = Options()
        chrome_option.debugger_address="127.0.0.1:9666"
        self.driver = webdriver.Chrome(options=chrome_option)
        self.driver.maximize_window()
        self.driver.implicitly_wait(3)
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")

    def goto_add_member(self):
        self.driver.find_element_by_xpath("//*[@id='_hmt_click']/div[1]/div[4]/div[2]/a[1]/div/span[2]").click()
        return AddMember(self.driver)