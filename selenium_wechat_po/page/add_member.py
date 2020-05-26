from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from selenium_wechat_po.base.base_page import BasePage


class AddMember(BasePage):

    def add_member(self):
        self.find(By.ID, "username").send_keys("hogwarts")
        self.find(By.ID, "memberAdd_acctid").send_keys("20200521")
        self.find(By.ID, "memberAdd_phone").send_keys("15800000000")
        self.find(By.CSS_SELECTOR, ".js_btn_save").click()
        self.wait_for_click((By.CSS_SELECTOR, ".js_has_member>div:nth-child(1) .js_add_member"))

    def get_element(self):
        elements = self.finds(By.CSS_SELECTOR, ".member_colRight_memberTable_td:nth-child(2)")
        # 获取元素属性值到list，第一种方法
        # list = []
        # for element in elements:
        #     # 获取所有的title值
        #     list.append(element.get_attribute("title"))
        # return list

        # 获取元素属性值，第二种方法，列表推导式
        return [element.get_attribute("title") for element in elements]
