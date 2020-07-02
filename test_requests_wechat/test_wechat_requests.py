import pytest
import requests


class TestWechat():

    def test_access_token(self):
        corpid = 'ww197063f50a78f00e'
        corpsecret = "KjeanuIGls0J7_mwx0KNHaw2Jp_yDO7NZ9fBZWkJBcM"
        r = requests.get(f'https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={corpid}&corpsecret={corpsecret}')
        assert r.status_code == 200
        access_token = r.json()['access_token']
        print(access_token)
        return r.json()['access_token']

    def test_get_contact(self):
        r = requests.get(
            f'https://qyapi.weixin.qq.com/cgi-bin/user/get?access_token={self.test_access_token()}&userid=20200521')
        assert r.json()['userid'] == "20200521"
        print(r.json())

    def test_create_member(self):
        data = {"userid": "jhon", "name": "拔刀斋", "mobile": "15700000000", "department": [1]}
        r = requests.post(f'https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={self.test_access_token()}]',
                          json=data)
        assert r.json()['errmsg'] == "created"
        print(r.json())

    def test_update_member(self):
        data = {"userid": "jhon", "name": "浪心", "mobile": "18511111111"}
        r = requests.post(f'https://qyapi.weixin.qq.com/cgi-bin/user/update?access_token={self.test_access_token()}',
                          json=data)
        assert r.json()['errmsg'] == "updated"

        print(r.json())

    def test_delete_member(self):
        r = requests.get(
            f'https://qyapi.weixin.qq.com/cgi-bin/user/delete?access_token={self.test_access_token()}&userid=jhon')
        assert r.json()['errmsg'] == "deleted"
        print(r.json())


if __name__ == '__main__':
    pytest.main()
