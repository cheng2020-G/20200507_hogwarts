from test_requests_wechat_po.test_base.testbase import TestBase


class TestDept(TestBase):

    def test_add_dept(self):
        assert self.dept.add_dept()['errmsg'] == 'created'

    def test_get_dept(self):
        # assert self.dept.get_dept()['department'][0]['name'] == 'apiobject'
        r = self.dept.get_dept()
        print(r)

    def test_update_dept(self):
        assert self.dept.update_dept()['errmsg'] == 'updated'

    def test_delete_dept(self):
        assert self.dept.delete_dept()['errmsg'] == 'deleted'
