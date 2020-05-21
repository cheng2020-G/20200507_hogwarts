from test_selenium.test_Hogworts.test_base import TestBase


class TestHogwarts(TestBase):
    # 定义测试case，里面包含测试步骤，定位元素的方式（八种），要执行什么操作，比如click,send等
    def test_hogwarts(self):
        self.driver.get("http://www.baidu.com")
        self.driver.find_element_by_id("kw").send_keys("selenium")
        self.driver.find_element_by_id("su").click()

