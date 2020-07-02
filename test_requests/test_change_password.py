import requests


class TestChangePassword():
    url = 'http://161.117.184.189:8888/user/api/changePassword'
    change_password_data = {"userId": "876", "oldPassword": "111111", "newPassword": "111111",
                            "confirmPassword": "111111"}

    def test_change_pasword(self):
        r = requests.post(self.url, data=self.change_password_data)
        print(r.text)
