from selenium import webdriver

from test_Selenium.test_Hogworts.test_base import TestBase

# 测试类继承基础类
class TestHogwarts(TestBase):

    # 定义测试case，里面包含测试步骤，定位元素的方式（八种），要执行什么操作，比如click,send等
    def test_hogwarts(self):
        self.driver.get("https://testerhome.com/")
        self.driver.find_element_by_xpath("/html/body/div[2]/div[1]/nav/div/div[2]/div/ul/li[4]/a").click()
        self.driver.find_element_by_xpath(
            "/html/body/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[2]/div[1]/a").click()
        self.driver.find_element_by_css_selector(
            "div.topic:nth-child(1) > div:nth-child(2) > div:nth-child(1) > a:nth-child(1)").click()
