from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from test_po_wechat.page.address_list_page import AddressList


class Main():
    def __init__(self):
        chrome_option = Options
        chrome_option.debugger_address = "127.0.0.1:9666"
        self.driver = webdriver.Chrome(options=chrome_option)

    def test_adddress_list(self):
        self.driver.find_element_by_xpath("//*[@id='menu_contacts']/span").click()
        return AddressList(self.driver)
