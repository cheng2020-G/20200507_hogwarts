import requests
from jsonpath import jsonpath


class TestJsonpath():

    def test_jsonpath1(self):
        data = {'hogwarts': ["a", "b", "c"]}
        r = requests.post('http://httpbin.org/post', data=data)
        url = jsonpath(r.json(), '$..url')[0]
        print(r.text)
        print('url is:' + url)

    def test_jsonpath2(self):
        r = requests.get('https://testerhome.com/api/v3/topics.json?limit=2')
        # user_id = jsonpath(r.json(), '$..topics.user[?(@.user.login)]')
        print(r.text)
        print(jsonpath(r.json(), '$..user'))
        user_id = jsonpath(r.json(), '$..user.login')
        print(user_id)

    def test_hogwarts_jsonpath(self):
        url = "https://ceshiren.com/categories.json"
        r = requests.get(url)
        print(r.json())
        assert r.json()['category_list']['categories'][0]['name'] == '霍格沃兹测试学院公众号'
        # 使用jsonpath提取出的内容为一个列表，需要再次提取[0]
        assert jsonpath(r.json(), '$.category_list.categories[0].name')[0] == '霍格沃兹测试学院公众号'
        assert jsonpath(r.json(), '$..name')[0] == '霍格沃兹测试学院公众号'
