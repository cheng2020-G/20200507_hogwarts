from time import sleep

from selenium.webdriver import TouchActions

from test_selenium.test_Action.test_action_base import TestAction


class TestTouchAction(TestAction):
    def test_touchaction_scrollbottom(self):
        self.driver.get("http://www.baidu.com/")
        ele_input = self.driver.find_element_by_xpath("//*[@id='kw']")
        ele_search = self.driver.find_element_by_xpath("//*[@id='su']")
        ele_input.send_keys("selenium")
        action = TouchActions(self.driver)
        action.tap(ele_search)
        # action.scroll(10000)
        # 滑动到页面底部，从哪个元素开始
        action.scroll_from_element(ele_search, 0, 10000)
        action.perform()
        sleep(2)