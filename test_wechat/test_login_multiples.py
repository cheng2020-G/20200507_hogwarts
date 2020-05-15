from time import sleep

import pytest

from test_wechat.test_wechat_base import TestBase


class TestLogin(TestBase):
    # @pytest.mark.skip
    def test_login(self):
        print(self.driver.current_window_handle)
        self.driver.find_element_by_xpath("//*[@id='indexTop']//div[2]//aside//a[1]").click()
        print(self.driver.current_window_handle)
        window = self.driver.window_handles
        self.driver.switch_to_window(window[-1])
        sleep(3)
        self.driver.find_element_by_xpath("//*[@id='wework_admin.loginpage_wx_$']/header/div/a").click()

    @pytest.mark.skip
    def test_multiplex(self):
        self.driver.find_element_by_xpath("//*[@id='menu_contacts']/span").click()
