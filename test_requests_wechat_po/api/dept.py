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
                "name": "api",
                "parentid": 1,
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
                "id": 10,
                "name": "apio",
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
                "id": id
            }
        }
        return self.send(data)
