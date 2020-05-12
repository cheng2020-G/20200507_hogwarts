import pytest
import selenium
from selenium import webdriver
from time import sleep


class TestElement():

    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.baidu.com/")
        self.driver.maximize_window()
        self.driver.implicitly_wait(3)

    def teardown(self):
        self.driver.quit()

    @pytest.mark.skip
    def test_element_by_id(self):
        # 定位元素用id方式
        self.driver.find_element_by_id("kw").send_keys("selenium")
        self.driver.find_element_by_id("su").click()

    @pytest.mark.skip
    def test_element_by_name(self):
        # 定位元素用name方式
        self.driver.find_element_by_name("wd").send_keys("name")

    @pytest.mark.skip
    def test_element_by_xpath(self):
        # 定位元素用xpath方式
        self.driver.find_element_by_xpath("//*[@id='kw']").send_keys("xpath")
        self.driver.find_element_by_xpath("//*[@id='su']").click()

    # @pytest.mark.skip
    def test_element_by_css_selector(self):
        # 定位元素用css_selector
        self.driver.find_element_by_css_selector("#kw").send_keys("css_selector")
        self.driver.find_element_by_css_selector("#su").click()
