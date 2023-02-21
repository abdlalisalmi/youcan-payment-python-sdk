import os
from .client import APIService
from .client import Keys


class YouCanPay:

    """ This is the main class for the YouCanPay SDK """

    keys = None
    token = None
    api_service = None

    def __init__(self, public_key: str, private_key: str, sandbox_mode=False) -> None:
        self.api_service = APIService(public_key, private_key, sandbox_mode)

        self.keys = Keys(self.api_service)
