from test_requests_wechat_po.api.baseapi import BaseApi
from test_requests_wechat_po.api.get_token import GetToken


class Dept(BaseApi):
    token = GetToken().get_token()

    def get_dept(self, token):
        data = {
            "method": "get",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/department/list?",
            "params": {
                "access_token": token,
                "id": "1"
            }
        }
        return self.send(data)

    def add_dept(self, token):
        data = {
            "method": "post",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/department/create?",
            "params": {
                "access_token": token,
                "name": "apiobject",
                "parentid": 1,
                "id": id
            }
        }
        return self.send(data)

    def update_dept(self, token):
        data = {
            "method": "post",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/department/update?",
            "params": {
                "access_token": token,
                "id": id,
                "name": "apiobject_change",
                "parentid": 1,
                "order": 1
            }
        }
        return self.send(data)

    def delete_dept(self, token):
        data = {
            "method": "post",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/department/delete?",
            "params": {
                "access_token": token,
                "id": id
            }
        }
        return self.send(data)
