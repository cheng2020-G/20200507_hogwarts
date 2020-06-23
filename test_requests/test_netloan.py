import json
import pytest
import requests
from jsonpath import jsonpath


class TestNetLoan():
    url = 'http://161.117.184.189:8888/user/api/register'
    register_data = json.load(open('data/register_data.json', 'r'))

    # @pytest.fixture()
    @pytest.mark.skip
    def test_register_num_error(self):
        r = requests.post(self.url, data=self.register_data)
        # data关键字使用json请求,先对post_data进行转码
        # r = requests.post(self.url, data=json.dumps(self.post_data))
        # json关键字
        # r = requests.post(url, json=post_data)
        assert r.json()["msg"][0] == "手机号格式无效"
        print(r.text)
        print(r.status_code)
        print(r.json())

    def test_register_yicunzai(self):
        r = requests.post(self.url, data=self.register_data)
        assert jsonpath(r.json(), '$.msg')[0]== '用户已存在'
        print(r.json())
        assert r.json()['msg'] == '用户已存在'
        print(self.register_data)

    def test_login_success(self):
        url = 'http://161.117.184.189:8888/user/api/login'
        login_data = json.load(open('data/login_data.json', 'r'))
        r = requests.post(url, json=login_data)
        print(r.text)

