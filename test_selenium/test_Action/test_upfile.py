from time import sleep
from test_selenium.test_Action.test_action_base import TestAction


class TestUpFile(TestAction):

    def test_up_file(self):
        self.driver.get("https://image.baidu.com")
        self.driver.find_element_by_xpath("//*[@id='sttb']//img[1]").click()
        self.driver.find_element_by_id("stfile").send_keys("D:\PycharmProject\20200507_pytest_calc\image\1.jpg")
        sleep(3)
