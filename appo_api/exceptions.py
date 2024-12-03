class AppoException(Exception):
    """Base exception for the Appo API."""


class SettingException(AppoException):
    """Exception for server setting errors (5xx)."""

    status_code: int = 500
    message: str = 'Server Setting Error'


class DetailedHTTPException(AppoException):
    """Exception that includes a status code and a message."""

    def __init__(
        self,
        *,
        status_code: int,
        message: str,
        detail: dict | str | None = None,
        headers: dict | None = None,
    ):
        self.status_code = status_code
        self.message = message
        self.detail = detail
        self.headers = headers


class ClientException(DetailedHTTPException):
    """Exception for client errors (4xx)."""

    status_code: int = 400
    message: str = 'Bad Request'

    def __init__(
        self,
        *,
        message: str | None = None,
        detail: dict | str | None = None,
        headers: dict | None = None,
    ):
        if message is not None:
            self.message = message
        self.detail = detail
        self.headers = headers


class UnAuthorizedException(ClientException):
    """Exception for 401 Unauthorized errors."""

    status_code: int = 401
    message: str = '인증에 실패했습니다.'
    headers: dict = {'WWW-Authenticate': 'Bearer'}

    def __init__(self, *, detail: dict | str | None = None):
        self.detail = detail


class NotFoundException(ClientException):
    """Exception for 404 Not Found errors."""

    status_code: int = 404
    message: str = 'Not Found'


class UserNotFound(NotFoundException):
    message = '유저 정보를 찾을 수 없습니다.'
