"""
The module that represents each possible Monzo API error; documented at:
https://monzo.co.uk/docs/#errors as individual Python errors.
"""


class MonzoException(Exception):
    """A generic Monzo exception."""


class BadRequestError(MonzoException):
    """An error to be raised when a request has missing arguments or is malformed."""


class UnauthorizedError(MonzoException):
    """An error to be raised when a request is not authenticated."""


class ForbiddenError(MonzoException):
    """An error to be raised when a request has insufficient permissions."""


class MethodNotAllowedError(MonzoException):
    """An error to be raised when a request is using an incorrect HTTP verb."""


class PageNotFoundError(MonzoException):
    """An error to be raised when a request requests an endpoint that doesn't exist."""


class NotAcceptableError(MonzoException):
    """An error to be raised when an application does not accept the content
    format returned according to the Accept headers sent in the request."""


class TooManyRequestsError(MonzoException):
    """An error to be raised when an application is exceeding its rate limit."""


class InternalServerError(MonzoException):
    """An error with Monzo's servers."""


class GatewayTimeoutError(MonzoException):
    """A timeout has occured on Monzo's servers."""
