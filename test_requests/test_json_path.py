import requests
from jsonpath import jsonpath


class TestJsonpath():

    def test_jsonpath1(self):
        data = {'hogwarts': ["a", "b", "c"]}
        r = requests.post('http://httpbin.org/post', data=data)
        url = jsonpath(r.json(), '$["url"]')
        print(r.text)
        print('url is:' + str(url))

    def test_jsonpath2(self):
        r = requests.get('https://testerhome.com/api/v3/topics.json?limit=2')
        user_id = jsonpath(r.json(), '$..topics.user[?(@.user.login)]')
        print(r.text)
        print('url is:' + str(user_id))