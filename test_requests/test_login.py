import json
import pytest
import requests
from jsonpath import jsonpath


class TestLogin():
    url = 'http://161.117.184.189:8888/user/api/login'
    login_data = json.load(open('data/login_data.json', 'r'))
    __login_token = []

    def test_login_success(self):
        r = requests.post(self.url, json=self.login_data)
        print(r.text)
        # 响应断言
        assert r.json()['msg'] == 'success'
        # 提取出token和user_id
        login_token = r.json()['data']['token']
        user_id = r.json()['data']['userId']
        # 将提取出的token传递给类变量
        self.__login_token.append(login_token)
        print(user_id)
        print(self.__login_token)


if __name__ == '__main__':
    pytest.main()
