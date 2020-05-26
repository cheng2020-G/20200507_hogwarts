from selenium.webdriver.common.by import By

from selenium_wechat_po.base.base_page import BasePage


class DelMember(BasePage):
    def del_member(self):
        del_member = "hogwarts"
        ele_members = self.find(By.CSS_SELECTOR, ".member_colRight_memberTable_td:nth-child(2)")
        list = [ele_members.get_attribute("title") for del_members in ele_members]
        if del_member in list:
            ele_members.get_attribute("title")

