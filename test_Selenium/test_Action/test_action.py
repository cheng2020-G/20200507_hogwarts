from time import sleep
import pytest
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

from test_Selenium.test_Action.test_action_base import TestAction


class TestActions(TestAction):
    # 点击、右击、双击
    @pytest.mark.skip
    def test_action_click(self):
        self.driver.get("http://sahitest.com/demo/clicks.htm")

        # 定位要点击的元素，赋值给变量click
        click = self.driver.find_element_by_xpath("")
        # 定位要右击的元素。赋值给rightclick
        rightclick = self.driver.find_element_by_xpath("")
        # 定位要双击的元素，赋值给doubleclick
        doubleclick = self.driver.find_element_by_xpath("")
        # 定义action，使用ActionChains（需要从seelnium导入），并继承driver

        action = ActionChains(self.driver)
        # 创建点击事件，排队等待
        action.click(click)
        # 创建右击事件，排队等待
        action.context_click(rightclick)
        # 创建双击事件，排队等地啊
        action.double_click(doubleclick)

        # perform执行上述等待的action事件
        action.perform()

    # actionchains用法：鼠标移动到某个元素上
    # @pytest.mark.skip
    def test_action_move(self):
        self.driver.get("https://www.baidu.com/")
        ele_move = self.driver.find_element_by_xpath("//*[@id='u']//a[2]")
        action = ActionChains(self.driver)
        action.move_to_element(ele_move)
        action.perform()
        sleep(3)

    # 鼠标拖拽一个元素到另外一个元素
    @pytest.mark.skip
    def test_action_dragdrop(self):
        self.driver.get("http://sahitest.com/demo/dragDropMooTools.htm")
        ele_drag = self.driver.find_element_by_xpath()
        ele_drop = self.driver.find_element_by_xpath()
        action = ActionChains(self.driver)
        action.drag_and_drop(ele_drag, ele_drop).perform()
        # 或者
        action.click_and_hold(ele_drag).release(ele_drop).perform()
        # 再或者
        action.click_and_hold(ele_drag).move_to_element(ele_drop).release().perform()

    @pytest.mark.skip
    def test_action_keys(self):
        self.driver.get("http://sahitest.com/demo/label.htm")
        ele_keys = self.driver.find_element_by_xpath()
        ele_keys.click()
        action = ActionChains(self.driver)
        # pause等待
        action.send_keys("username").pause(1)
        action.send_keys(Keys.SPACE).pause(1)
        action.send_keys("tom").pause(1)
        action.send_keys(Keys.BACK_SPACE).pause(1)
        action.perform()
