import shelve
from time import sleep

from test_wechat.test_wechat_base import TestBase


class TestCookies(TestBase):
    def test_wechatlogin_cookies(self):
        # print(self.driver.get_cookies())
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        # 创建用于存储cookies的文件，使用shelve库
        db = shelve.open("cookies")
        # 保存cookies
        # db['cookie'] = self.driver.get_cookies()
        # 使用cookies
        cookies = db['cookie']
        # 获取cookies
        for cookie in cookies:
            # 删除不符合要求的值：”expiry“
            if "expiry" in cookie.keys():
                cookie.pop("expiry")
            # 将获取到的符合的cookie加入到driver
            self.driver.add_cookie(cookie)
         # 最后去访问页面
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        sleep(3)
        db.close()
        self.driver.find_element_by_xpath("//*[@id='menu_contacts']/span").click()
        sleep(3)
