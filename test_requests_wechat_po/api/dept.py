from test_requests_wechat_po.api.baseapi import BaseApi
from test_requests_wechat_po.api.get_token import GetToken


class Dept(BaseApi):
    token = GetToken().get_token()

    def get_dept(self):
        data = {
            "method": "get",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/department/list?",
            "params": {
                "access_token": self.token,
                "id": "1"
            }
        }
        return self.send(data)

    def add_dept(self):
        data = {
            "method": "post",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/department/create?",
            "params": {
                "access_token": self.token,
                "name": "北京部门",
                "name_en": "dept-bj",
                "parentid": 1,
                "order": 1,
                "id": 10
            }
        }
        return self.send(data)

    def update_dept(self):
        data = {
            "method": "post",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/department/update?",
            "params": {
                "access_token": self.token,
                "id": 5,
                "name": "爱测测试平台",
                "name_en": "ceshier",
                "parentid": 1,
                "order": 1
            }
        }
        return self.send(data)

    def delete_dept(self):
        data = {
            "method": "post",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/department/delete?",
            "params": {
                "access_token": self.token,
                "id": 4
            }
        }
        return self.send(data)
