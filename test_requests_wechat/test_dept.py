import pytest
import requests
from jsonpath import jsonpath


def test_access_token():
    corpid = 'ww197063f50a78f00e'
    corpsecert = 'KjeanuIGls0J7_mwx0KNHaw2Jp_yDO7NZ9fBZWkJBcM'
    url = f'https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={corpid}&corpsecret={corpsecert}'
    r = requests.get(url)
    print(r.json())
    return r.json()['access_token']


def test_get_dept():
    id = 1
    url = f'https://qyapi.weixin.qq.com/cgi-bin/department/list?access_token={test_access_token()}&id={id}'
    r = requests.get(url)
    print(r.json())
    assert r.json()['department'][0]['name'] == 'cheng'
    print(jsonpath(r.json(), '$..department'))

def test_add_dept():
    data = {
        "name": "hogwarts测试平台",
        "name_en": "hogwarts",
        "parentid": 1,
        "order": 1,
        "id": 2
    }
    url = f'https://qyapi.weixin.qq.com/cgi-bin/department/create?access_token={test_access_token()}'
    r = requests.post(url, json=data)
    print(r.json())
    assert r.json()['errmsg'] == 'created'
    assert r.json()['id'] == 2


def test_update_dept():
    data = {
        "id": 2,
        "name": "爱测测试平台",
        "name_en": "ceshier",
        "parentid": 1,
        "order": 1
    }
    url = f'https://qyapi.weixin.qq.com/cgi-bin/department/update?access_token={test_access_token()}'
    r = requests.post(url, json=data)
    print(r.json())
    assert r.json()['errmsg'] == 'updated'


@pytest.mark.skip
def test_delete_dept():
    id = 2
    url = f'https://qyapi.weixin.qq.com/cgi-bin/department/delete?access_token={test_access_token()}&id={id}'
    r = requests.get(url)
    print(r.json())
    assert r.json()['errmsg'] == 'deleted'


if __name__ == '__main__':
    pytest.main()
