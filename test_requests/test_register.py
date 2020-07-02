import json

import pytest
import requests
from jsonpath import jsonpath


class TestRegister():
    url = 'http://161.117.184.189:8888/user/api/register'
    register_data = json.load(open('data/register_data.json', 'r'))

    def test_redister_success(self):
        # data关键字使用json请求,先对post_data进行转码
        # r = requests.post(self.url, data=json.dumps(self.post_data))
        # json关键字
        # r = requests.post(url, json=post_data)
        r = requests.post(self.url, data=self.register_data)
        print(r.text)
        assert r.json()['msg'] == 'success'

    def test_register_fail(self):
        r = requests.post(self.url, data=self.register_data)
        print(r.text)
        assert jsonpath(r.json(), '$.msg')[0] == '用户已存在'

if __name__ == '__main__':
    pytest.main()