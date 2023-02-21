import os
import requests
import json


class APIService(object):

    """  """

    BASE_API_URL = 'https://youcanpay.com/'

    def __init__(self, public_key: str, private_key: str, sandbox_mode=False) -> None:
        self.public_key = public_key
        self.private_key = private_key
        self.sandbox_mode = sandbox_mode

    @property
    def base_url(self) -> str:
        # Get base url from environment variable
        base_url = os.environ.get('YOUCAN_PAY_API_URL', self.BASE_API_URL)
        #  Check sandbox mode
        base_url = base_url + 'sandbox/api/' if self.sandbox_mode else base_url + 'api/'
        return base_url

    @property
    def is_sandbox_mode(self) -> bool:
        return self.sandbox_mode

    def get_private_key(self) -> str:
        return self.private_key

    def get_public_key(self) -> str:
        return self.public_key

    @staticmethod
    def request(method: str, endpoint: str, data: dict, headers: dict):
        headers['Content-Type'] = 'application/json'
        return requests.request(
            method, endpoint, headers=headers, data=json.dumps(data))

    def post(self, endpoint: str, data: dict = {}, headers: dict = {}):
        return self.request('POST', endpoint, data, headers)

    def get(self, endpoint: str, data: dict = {}, headers: dict = {}):
        return self.request('GET', endpoint, data, headers)
