import pytest
import selenium
from selenium import webdriver
from time import sleep

from test_selenium.test_Baidu.test_baidu_base import TestBaiduBase


class TestElement(TestBaiduBase):

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
