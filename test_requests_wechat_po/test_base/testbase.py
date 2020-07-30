from test_requests_wechat_po.api.dept import Dept
from test_requests_wechat_po.api.get_token import GetToken


class TestBase:

    def setup(self):
        self.gettoken = GetToken()
        self.dept = Dept()
