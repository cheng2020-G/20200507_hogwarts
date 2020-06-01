import pytest
import yaml
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from po_change.page.base_page import BasePage


class Main(BasePage):

    def goto_search(self):
        ele_search = self.find(MobileBy.ID, "tv_search")
        WebDriverWait(self._driver, 10).until(expected_conditions.element_to_be_clickable, ele_search)
        # self.find(MobileBy.ID, "tv_search").click()
        ele_search.click()
        # self.steps("D:\PycharmProject/20200507_pytest_calc\po_change\page\main.yaml")

    def goto_windows(self):
        self.find(By.ID, "post_status").click()
        self.find(By.ID, "tv_search").click()