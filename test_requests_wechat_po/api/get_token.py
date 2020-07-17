import pytest
import yaml

from test_requests_wechat_po.api.baseapi import BaseApi


class GetToken(BaseApi):
    def get_token(self):
        # 请求参数从yaml文件读取
        data = yaml.safe_load(
            open("../data/get_token.yaml"))
        print(data)
        return self.send(data)['access_token']

# 调试时使用，以便验证return回的结果
# if __name__ == '__main__':
#     gettoken = GetToken().get_token()
