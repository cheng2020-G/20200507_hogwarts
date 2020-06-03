import json

import requests


class TestNetLoan():
    def test_register(self):
        url = 'http://161.117.184.189:8888/user/api/register'
        # headers = {"Content-Type": "application/json", "User-Agent": "Chrome", "appversion": "1.1.6",
        # "carrier": "carrier", "manufacturer": "manufacturer"}
        post_data = {"inviteCode": "", "phone": "18282821111", "verifyCode": "1111", "sourceType": 1,
                     "password": "123123", "appVersion": "2.0.5", "token": "", "baiqishiToken": "string",
                     "deviceToken": "", "deviceType": 1, "serialNumber": "string", "idcard": "", "referrer": "string",
                     "deviceModel": "OPPO R11", "deviceAppVersion": "7.1.1", "carrier": "string",
                     "manufacturer": "OPPO"}
        # r = requests.post(url, data=post_data)
        # data关键字使用json请求
        r = requests.post(url, data=json.dumps(post_data))
        # json关键字
        # r = requests.post(url, json=post_data)
        assert r.json()["msg"] == "手机号格式无效"

        print(r.url)
        print(r.text)
        print(r.status_code)
        print(r.headers)
        print(r.json())
        print(r.cookies)
        print(r.request)
        print(r.raw)
