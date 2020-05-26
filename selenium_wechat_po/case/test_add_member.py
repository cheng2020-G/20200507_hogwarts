import pytest

from selenium_wechat_po.page.main import Main


class TestAddMember():
    def setup(self):
        self.main = Main()

    @pytest.mark.skip
    def test_add_member(self):
        add_member = self.main.goto_add_member()
        add_member.add_member()
        # 添加断言，验证是否新增的成员成功
        assert "hogwarts" in add_member.get_element()

    # @pytest.mark.skip
    def test_add_member_contact(self):
        add_member_contact = self.main.goto_contact().add_member_contacts()
        add_member_contact.add_member()
        assert "hogwarts" in add_member_contact.get_element()

    # def test_del_member(self):
    #     del_member = "hogwarts"
    #     del_member_action = self.main.goto_contact()
