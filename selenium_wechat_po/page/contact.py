from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from selenium_wechat_po.base.base_page import BasePage
from selenium_wechat_po.page.add_member import AddMember


class Contact(BasePage):

    def add_member_contacts(self):
        self.wait_for_click((By.CSS_SELECTOR, ".js_has_member>div:nth-child(1) .js_add_member"))
        self.find(By.CSS_SELECTOR, ".js_has_member>div:nth-child(1) .js_add_member").click()
        return AddMember(self.driver)
