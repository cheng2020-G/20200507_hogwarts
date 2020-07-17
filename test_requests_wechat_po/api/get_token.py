import pytest

from test_requests_wechat_po.api.baseapi import BaseApi


class GetToken(BaseApi):
    # @pytest.fixture(autouse=True)
    def get_token(self):
        data = {
            "method": "get",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/gettoken?",
            "params": {
                "corpid": "ww197063f50a78f00e",
                "corpsecret": "KjeanuIGls0J7_mwx0KNHc7W2hvYiqRnCFxEwtdKrHU"
            }
        }
        return self.send(data)['access_token']

# 调试时使用，以便验证return回的结果
# if __name__ == '__main__':
#     gettoken = GetToken().get_token()
