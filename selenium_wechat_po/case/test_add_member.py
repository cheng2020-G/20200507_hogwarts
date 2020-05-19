from selenium.webdriver.remote.webdriver import WebDriver

from selenium_wechat_po.page.main import Main


class TestAddMember():
    def setup(self):
        self.main = Main()

    def test_addmember(self):
        self.main.goto_add_member().add_member()
