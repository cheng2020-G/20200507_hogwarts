from test_Selenium.test_Action.test_action_base import TestAction


class TestForm(TestAction):
    def test_form(self):
        self.driver.get("https://testerhome.com/account/sign_in")
        self.driver.find_element_by_xpath("//*[@id='new_user']//div[1]/input").send_keys("hogwarts")
        self.driver.find_element_by_xpath("//*[@id='new_user']//div[2]/input").send_keys("hogwarts")
        self.driver.find_element_by_xpath("//*[@id='new_user']//div[last()]/input").click()
