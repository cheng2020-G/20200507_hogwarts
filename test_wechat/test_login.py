from time import sleep

from test_wechat.test_wechat_base import TestBase


class TestLogin(TestBase):
    def test_login(self):
        self.driver.get("https://work.weixin.qq.com/")
        print(self.driver.current_window_handle)
        self.driver.find_element_by_xpath("//*[@id='indexTop']//div[2]//aside//a[1]").click()
        print(self.driver.current_window_handle)
        window = self.driver.window_handles
        self.driver.switch_to_window(window[-1])
        sleep(3)
        self.driver.find_element_by_xpath("//*[@id='wework_admin.loginpage_wx_$']/header/div/a").click()
        self.driver.switch_to.frame(0)
        ele_login = self.driver.find_element_by_xpath("/html//div/div/div[2]/div/img")
        ele_login.screenshot_as_png("D:\PycharmProject\20200507_pytest_calc\image")