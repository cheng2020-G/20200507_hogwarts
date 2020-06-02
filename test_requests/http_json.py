import json

import requests


class TestHttpJson():
    def test_http_json(self):
        url = 'http://httpbin.org/post'
        datas = {'hogwarts': ["a", "b", "c"]}
        # 使用data关键字发送json请求，需要使用json.dumps对传入的变量进行转码
        r = requests.post(url, data=json.dumps(datas))
        # 响应断言
        assert r.json()['headers']["Host"] == "httpbin.org"
        print(r.json())
        print(r.headers)

    def test_http_json_data(self):
        url = 'http://httpbin.org/post'
        datas = {'hogwarts': ["a", "b", "c"]}
        # 使用json关键字参数发送请求
        r = requests.post(url, json=datas)
        assert r.json()['json']['hogwarts'][2] == "c"
        print(r)
        print(r.headers)
        print(r.json())
