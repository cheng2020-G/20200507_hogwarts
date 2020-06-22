import requests
from requests.auth import HTTPBasicAuth


class TestAuth:
    def test_auth_http(self):
        url = "http://httpbin.testing-studio.com/basic-auth/user/passwd"
        r = requests.get(url, auth=HTTPBasicAuth("user", "passwd"))
        print(r.status_code)
        print(r.json())
