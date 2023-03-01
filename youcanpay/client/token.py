from youcanpay import exceptions


class Token:

    """Token class to handle token related operations"""

    BASE_ENDPOINT = "tokenize"

    def __init__(self, api_service) -> None:
        self.api_service = api_service
        self.BASE_ENDPOINT = self.api_service.base_url + self.BASE_ENDPOINT

        self.id = None

    def create(
        self,
        orderId: str,
        amount: str,
        currency: str,
        customer_ip: str,
        success_url: str = None,
        error_url: str = None,
        customer_info: list = [],
        metadata: list = [],
    ):
        data = {
            "pri_key": self.api_service.get_private_key(),
            "order_id": orderId,
            "amount": amount,
            "currency": currency,
            "customer_ip": customer_ip,
            "success_url": success_url,
            "error_url": error_url,
            "customer": customer_info,
            "metadata": metadata,
        }
        res = self.api_service.post(self.BASE_ENDPOINT, data=data)
        res = self.api_service.assert_response(res)
        self.id = res.get("token", {}).get("id", None)
        if not self.id:
            raise exceptions.UnknownError
        return self

    def get_payment_url(self, lang="en"):
        sandbox = "sandbox/" if self.api_service.is_sandbox_mode else ""
        return f"{self.api_service.base_api_url}{sandbox}payment-form/{self.id}?lang={lang}"
