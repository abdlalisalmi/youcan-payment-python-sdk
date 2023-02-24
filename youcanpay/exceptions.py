

class BaseException(Exception):

    """Base exception for all exceptions in this package."""

    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message


class BadRequestError(BaseException):

    """Exception raised for bad requests."""

    msg = 'Bad request. Please check the request and try again!'

    def __init__(self, message=None):
        super().__init__(message if message else self.msg)


class UnauthorizedError(BaseException):

    """Exception raised for unauthorized requests."""

    msg = 'Unauthorized request. Please check the API keys and try again!'

    def __init__(self, message=None):
        super().__init__(message if message else self.msg)


class UnprocessableEntityError(BaseException):

    """Exception raised for unprocessable requests."""

    msg = 'Unprocessable request. Please check the request and try again!'

    def __init__(self, message=None):
        super().__init__(message if message else self.msg)


class NotFoundError(BaseException):

    """Exception raised for not found requests."""

    msg = 'Not found. Please check the request and try again!'

    def __init__(self, message=None):
        super().__init__(message if message else self.msg)


class InternalServerError(BaseException):

    """Exception raised for internal server errors."""

    msg = 'Internal error from server. Support has been notified. Please try again!'

    def __init__(self, message=None):
        super().__init__(message if message else self.msg)


class UnknownError(BaseException):

    """Exception raised for unknown errors."""

    msg = 'Unknown error. Please try again!'

    def __init__(self, message=None):
        super().__init__(message if message else self.msg)
