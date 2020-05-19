import pytest

from test_po_wechat.page.index import Index


class TestRegister():
    def setup(self):
        self.index = Index()

    @pytest.mark.skip
    def test_register_goto_login(self):
        self.index.goto_login().goto_register().register()

    # @pytest.mark.skip
    def test_register_goto_register(self):
        self.index.goto_register().register()
