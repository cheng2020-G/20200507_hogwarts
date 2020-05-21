from time import sleep

import pytest

from test_selenium.test_Action.test_action_base import TestAction


class TestJs(TestAction):
    @pytest.mark.skip
    def test_js_scroll(self):
        self.driver.get("http://www.baidu.com")
        self.driver.find_element_by_id("kw").send_keys("selenium")
        # 获取js中的元素，并返回，赋值给变量
        ele_su = self.driver.execute_script("return document.getElementById('su')")
        ele_su.click()
        sleep(3)
        # 执行javascript页面滑动
        self.driver.execute_script("document.documentElement.scrollTop=10000")
        self.driver.find_element_by_xpath("//*[@id='page']//a[last()]").click()
        sleep(3)
        # 获取当前页面title，及性能数据，返回赋值给code，打印code
        # for code in [
        #     'return document.title', 'return Json.stringify(performance.timing)'
        # ]:
        #     print(self.driver.execute_script(code))
        # 也可以这样写
        print(self.driver.execute_script("return document.title;return Json.stringify(performance.timing"))

    def test_datatime(self):
        self.driver.get("https://www.12306.cn/index/")
        self.driver.find_element_by_id("fromStationText").click()
        self.driver.find_element_by_xpath("//*[@id='ul_list1']/li[1]").click()
        self.driver.find_element_by_id("toStationText").click()
        self.driver.find_element_by_xpath("//*[@id='ul_list1']//li[2]").click()
        # 获取出发时间元素，并移除只读属性
        self.driver.execute_script("a = document.getElementById('train_date');a.removeAttribute('readonly')")
        # 给元素重新赋值
        self.driver.execute_script("document.getElementById('train_date').value='2020-01-01'")
        sleep(5)
        # 打印return回来的value
        print(self.driver.execute_script("return document.getElementById('train_date').value"))
        self.driver.find_element_by_id("search_one").click()
        # 获取所有的窗口
        window = self.driver.window_handles
        # 切换到新页面
        self.driver.switch_to_window(window[-1])
        sleep(10)