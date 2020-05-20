from selenium.webdriver.remote.webdriver import WebDriver

from selenium_wechat_po.page.add_member import AddMember


class Contact():
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def add_member_contacts(self):
        self.driver.find_element_by_xpath("//*[@id='js_contacts63']//div//div[2]/div//div[3]/div[1]/a[1]").click()
        return AddMember(self.driver)