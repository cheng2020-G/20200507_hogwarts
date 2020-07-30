import requests


class BaseApi:
    # 构建send方法，data传参，**data解参
    def send(self, data):
        return requests.request(**data).json()
