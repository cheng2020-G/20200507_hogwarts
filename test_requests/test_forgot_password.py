import json

import pytest
import requests
from jsonpath import jsonpath


class TestForgotPassword():
    url = 'http://161.117.184.189:8888/user/api/resetPassword'
    forgot_data = {"phone": "09956236061", "verifyCode": "1111", "newPassword": "111111"}

    def test_forgot_password(self):
        r = requests.post(self.url, json=self.forgot_data)
        print(r.text)
        assert jsonpath(r.json(), '$.msg')[0] == '验证码错误'

if __name__ == '__main__':
    pytest.main()
