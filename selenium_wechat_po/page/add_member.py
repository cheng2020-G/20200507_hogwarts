from selenium.webdriver.remote.webdriver import WebDriver


class AddMember():
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def add_member(self):
        self.driver.find_element_by_id("username").send_keys("hogwarts")
        self.driver.find_element_by_id("memberAdd_acctid").send_keys("20200521")
        self.driver.find_element_by_id("memberAdd_phone").send_keys("15800000000")
        self.driver.find_element_by_xpath("//*[@id='js_contacts39']/div/div[2]/div/div[4]/div/form/div[3]/a[2]").click()
        self.driver.quit()
        return  True