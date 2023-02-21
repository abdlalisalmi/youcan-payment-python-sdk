from youcanpay import exceptions


class Keys:

    """"""

    BASE_ENDPOINT = 'keys'

    def __init__(self, api_service) -> None:
        self.api_service = api_service
        self.BASE_ENDPOINT = self.api_service.base_url + self.BASE_ENDPOINT

    def check(self):
        """
        Check if the API keys are valid

        Arguments:
                 None

        Returns:
                bool: True if the keys are valid, False otherwise

        Throws:
                InternalServerError: If the server returns a 500 error
        """

        endpoint = self.BASE_ENDPOINT + '/check'
        payload = {
            'pri_key': self.api_service.get_private_key(),
            'pub_key': self.api_service.get_public_key()
        }
        res = self.api_service.post(endpoint, data=payload)

        if res.status_code != 500:
            raise exceptions.InternalServerError
        if res.status_code != 200:
            return False
        return True
