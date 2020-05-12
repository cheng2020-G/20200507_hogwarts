from time import sleep

from test_Selenium.test_Action.test_action_base import TestAction


class TestWindow(TestAction):
    def test_window(self):
        self.driver.get("https://www.baidu.com/")
        self.driver.find_element_by_xpath("//*[@id='u1']//a[2]").click()
        # 获取当前窗口的句柄
        print(self.driver.current_window_handle)
        self.driver.find_element_by_xpath("//*[@id='passport-login-pop-dialog']/div/div/div/div[3]/a").click()
        # 获取当前窗口的句柄
        print(self.driver.current_window_handle)
        # 获取所有的窗口句柄
        print(self.driver.window_handles)
        # 变量存储所有窗口句柄
        windows = self.driver.window_handles
        # 切换到新窗口，-1表示最后一个窗口，当前只有2个
        self.driver.switch_to_window(windows[-1])
        self.driver.find_element_by_xpath("//*[@id='TANGRAM__PSP_4__userNameWrapper']/input[2]").send_keys("hogwarts")
        # 切换到原来的窗口
        self.driver.switch_to_window(windows[0])
        self.driver.find_element_by_xpath("//*[@id='TANGRAM__PSP_10__footerULoginBtn']").click()
        self.driver.find_element_by_xpath("//*[@id='TANGRAM__PSP_10__userName']").send_keys("hogwarts")
        self.driver.find_element_by_xpath("//*[@id='TANGRAM__PSP_10__password']").send_keys("hogwarts")
        self.driver.find_element_by_xpath("//*[@id='TANGRAM__PSP_10__submit']").click()
        sleep(3)