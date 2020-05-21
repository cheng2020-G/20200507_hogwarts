from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

from selenium_wechat_po.base.base_page import BasePage
from selenium_wechat_po.page.add_member import AddMember
from selenium_wechat_po.page.contact import Contact


class Main(BasePage):
    base_url = "https://work.weixin.qq.com/wework_admin/frame"

    def goto_add_member(self):
        self.find(By.XPATH, "//*[@id='_hmt_click']/div[1]/div[4]/div[2]/a[1]/div/span[2]").click()
        return AddMember(self.driver)

    def goto_contact(self):
        self.find(By.XPATH, "//*[@id='menu_contacts']/span").click()
        return Contact(self.driver)
