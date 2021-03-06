from rest_framework import status
from rest_framework.exceptions import APIException


class RequiredParameterMissingException(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    pass


class DateParseException(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    pass


class DateTimeParseException(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    pass


class ValidationFailedException(APIException):
    status_code = status.HTTP_403_FORBIDDEN
    pass