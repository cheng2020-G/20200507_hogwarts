import pytest
import requests


class TestHttp():
    @pytest.mark.skip
    def test_http_get(self):
        r = requests.get('http://api.github.com/events')
        assert r.status_code == 200
        print(r)
        print(r.status_code)
        print(r.headers)

    # @pytest.mark.skip
    def test_http_post(self):
        r = requests.post('http://httpbin.org/post', data={"key": "value"})
        assert r.status_code == 200
        print(r)
        print(r.status_code)
        print(r.text)
        print(r.headers)

    @pytest.mark.skip
    def test_http_put(self):
        r = requests.put('http://httpbin.org/post', data={"key": "value"})
        # assert r.status_code == 200
        print(r)
        print(r.text)
        print(r.status_code)
        print(r.headers)

    @pytest.mark.skip
    def test_http_delete(self):
        r = requests.delete('http://httpbin.org/delete')
        assert r.status_code == 200
        print(r)
        print(r.status_code)
        print(r.text)
        print(r.headers)

    @pytest.mark.skip
    def test_http_head(self):
        r = requests.head('http://httpbin.org/get')
        assert r.status_code == 200
        print(r)
        print(r.status_code)
        print(r.text)
        print(r.headers)

    @pytest.mark.skip
    def test_http_options(self):
        r = requests.options('http://httpbin.org/get')
        assert r.status_code == 200
        print(r)
        print(r.status_code)
        print(r.text)
        print(r.headers)

    @pytest.mark.skip
    def test_http_requests(self):
        r = requests.request('get', 'https://www.baidu.com')
        assert r.status_code == 200
        print(r)
        print(r.status_code)
        print(r.text)
        print(r.headers)

    @pytest.mark.skip
    def test_http_dict(self):
        url = 'http://api.github.com/some/endpoint'
        header = {'user-agent': 'my-app/0.01'}
        r = requests.get(url, headers=header)
        print(r)
        print(r.status_code)
        print(r.headers)
        print(r.text)

    @pytest.mark.skip
    def test_http_data(self):
        url = 'http://httpbin.org/get'
        payload = {'key1': 'value1', 'key2': 'value2'}
        r = requests.post(url, data=payload)
        print(r.text)
        print(r.status_code)
        print(r.headers)
