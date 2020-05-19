from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class AddMember():
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def add_member(self):
        self.driver.find_element_by_id("username").send_keys("hogwarts")
        self.driver.find_element_by_id("memberAdd_acctid").send_keys("20200521")
        self.driver.find_element_by_id("memberAdd_phone").send_keys("15800000000")
        self.driver.find_element_by_xpath("//*[@id='js_contacts51']/div/div[2]/div/div[4]/div/form/div[3]/a[2]").click()
        # self.driver.quit()

    def get_element(self):
        elements = self.driver.find_elements(By.CSS_SELECTOR, ".member_colRight_memberTable_td:nth-child(2)")
        # 获取元素属性值到list，第一种方法
        # list = []
        # for element in elements:
        #     # h获取所有的title值
        #     list.append(element.get_attribute("title"))

        # 获取元素属性值到list，第二种方法，列表推导式
        list = [element.get_attribute("title") for element in elements]
        return list