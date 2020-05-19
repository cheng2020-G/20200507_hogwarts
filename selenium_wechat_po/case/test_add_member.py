from selenium.webdriver.remote.webdriver import WebDriver

from selenium_wechat_po.page.main import Main


class TestAddMember():
    def setup(self):
        self.main = Main()

    def test_addmember(self):
        add_member = self.main.goto_add_member()
        add_member.add_member()
        # 添加断言，验证是否新增的成员成功
        assert "hogwarts" in add_member.get_element()
