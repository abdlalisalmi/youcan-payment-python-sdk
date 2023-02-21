

class BaseException(Exception):

    """Base exception for all exceptions in this package."""

    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message


class InternalServerError(BaseException):

    """Exception raised for internal server errors."""

    msg = 'Internal error from server. Support has been notified. Please try again!'

    def __init__(self, message=msg):
        super().__init__(message)


class InvalidRequestError(BaseException):

    """Exception raised for invalid requests."""
    pass
