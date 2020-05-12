from time import sleep

from selenium.webdriver import ActionChains

from test_Selenium.test_Action.test_action_base import TestAction


class TestFrame(TestAction):
    def test_frame(self):
        self.driver.get("https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable")
        # 第一种常用的切换frame方式
        self.driver.switch_to.frame("iframeResult")
        # 第二种，也可以切换frame
        # self.driver.switch_to_frame("iframeResult")
        ele_draggable = self.driver.find_element_by_id("draggable")
        ele_droppable = self.driver.find_element_by_id("droppable")
        action = ActionChains(self.driver)
        # 移动一个元素到另一个元素
        action.drag_and_drop(ele_draggable,ele_droppable)
        action.perform()
        sleep(3)
        # alert弹框处理，模拟确定操作
        self.driver.switch_to.alert.accept()
        # 切回到默认的frame，也就是父frame
        self.driver.switch_to.default_content()
        self.driver.find_element_by_id("submitBTN").click()
        sleep(3)

