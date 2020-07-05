import pytest
import requests
from jsonpath import jsonpath


@pytest.fixture(scope="session")
def test_access_token():
    corpid = 'ww197063f50a78f00e'
    corpsecert = 'KjeanuIGls0J7_mwx0KNHaw2Jp_yDO7NZ9fBZWkJBcM'
    url = f'https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={corpid}&corpsecret={corpsecert}'
    r = requests.get(url)
    return r.json()['access_token']


def test_get_dept(id, test_access_token):
    url = f'https://qyapi.weixin.qq.com/cgi-bin/department/list?access_token={test_access_token}&id={id}'
    r = requests.get(url)
    return r.json()


def test_add_dept(name, id, test_access_token):
    data = {
        "name": name,
        "parentid": 1,
        "id": id
    }
    url = f'https://qyapi.weixin.qq.com/cgi-bin/department/create?access_token={test_access_token}'
    r = requests.post(url, json=data)
    return r.json()


# @pytest.mark.skip
def test_update_dept(name_new, id, test_access_token):
    data = {
        "id": id,
        "name": name_new,
        "parentid": 1,
        "order": 1
    }
    url = f'https://qyapi.weixin.qq.com/cgi-bin/department/update?access_token={test_access_token}'
    r = requests.post(url, json=data)
    return r.json()


# @pytest.mark.skip
def test_delete_dept(id, test_access_token):
    url = f'https://qyapi.weixin.qq.com/cgi-bin/department/delete?access_token={test_access_token}&id={id}'
    r = requests.get(url)
    return r.json()


@pytest.mark.parametrize("name, id, name_new", [("tester1", "6", 'ceshi1'), ("tester2", "7", 'ceshi2')])
def test_all(name, id, name_new, test_access_token):
    try:
        assert 'created' == test_add_dept(name, id, test_access_token)['errmsg']
    except AssertionError as e:
        if 'department existed' in e.__str__():
            assert 'deleted' == test_delete_dept(id, test_access_token)['errmsg']
            assert 'created' == test_add_dept(name, id, test_access_token)['errmsg']
    assert 'updated' == test_update_dept(name_new, id, test_access_token)['errmsg']
    assert name_new == test_get_dept(id, test_access_token)['department'][0]['name']
    assert 'deleted' == test_delete_dept(id, test_access_token)['errmsg']
