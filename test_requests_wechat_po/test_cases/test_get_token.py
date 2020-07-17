from test_requests_wechat_po.test_base.testbase import TestBase


class TestGetToken(TestBase):

    def test_get_token(self):
        r = self.gettoken.get_token()
        print(r)
