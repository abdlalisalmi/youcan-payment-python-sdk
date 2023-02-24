import os
from .client import APIService
from .client import Keys, Token


class YouCanPay:

    """ This is the main class for the YouCanPay SDK """

    keys = None
    token = None
    api_service = None

    def __init__(self, public_key: str, private_key: str, sandbox_mode=False) -> None:
        # Initialize the api service
        self.api_service = APIService(public_key, private_key, sandbox_mode)
        # Initialize the keys object
        self.keys = Keys(self.api_service)
        # Initialize the token object
        self.token = Token(self.api_service)
