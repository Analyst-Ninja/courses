"""
Enum Data Type
"""

from enum import Enum, StrEnum


class EmployeeType(Enum):
    """
    Enum for Employee Types"""

    FULL_TIME = 1
    PART_TIME = 2
    CONTRACTOR = 3


class EmployeeTypeStr(StrEnum):
    """
    String Enum for Employee Types
    """

    FULL_TIME = "Potato"
    PART_TIME = "Part Time"
    CONTRACTOR = "Contractor"


class HTTPStatus(Enum):
    """
    Enum for HTTP Status Codes
    """

    OK = 200
    NOT_FOUND = 404
    INTERNAL_SERVER_ERROR = 500
    UNAUTHORIZED = 401
    FORBIDDEN = 403


class RESTMethod(StrEnum):
    """
    String Enum for REST Methods
    """

    GET = "GET"
    POST = "POST"
    PUT = "PUT"
    DELETE = "DELETE"
    PATCH = "PATCH"


class Color(Enum):
    """
    Enum for Colors
    """

    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)

    def __init__(self, red: int, green: int, blue: int):
        self.r = red
        self.g = green
        self.b = blue

    def luminance(self) -> float:
        """
        Calculate the luminance of the color.
        """
        return 0.2126 * self.r + 0.7152 * self.g + 0.0722 * self.b


def get_http_status_message(status_code: HTTPStatus) -> str:
    """
    Returns the message for a given HTTP status code.
    """
    messages = {
        HTTPStatus.OK: "OK",
        HTTPStatus.NOT_FOUND: "Not Found",
        HTTPStatus.INTERNAL_SERVER_ERROR: "Internal Server Error",
        HTTPStatus.UNAUTHORIZED: "Unauthorized",
        HTTPStatus.FORBIDDEN: "Forbidden",
    }
    return messages.get(status_code, "Unknown Status")


def get_http_status_code(status_code: HTTPStatus) -> int:
    """
    Returns the code for a given HTTP status.
    """
    return status_code.value


def get_rest_method(method: RESTMethod) -> str:
    """
    Returns the string representation of a given REST method.
    """
    return method.value


def main():
    """
    Main function to demonstrate enum operations.
    """
    e_type = EmployeeType.FULL_TIME

    print(e_type)
    print(e_type.name)
    print(e_type.value)

    print(get_http_status_message(HTTPStatus.INTERNAL_SERVER_ERROR))
    print(get_http_status_code(HTTPStatus.INTERNAL_SERVER_ERROR))
    print(get_rest_method(RESTMethod.GET))

    color = Color(Color.GREEN)
    print(color.luminance())


if __name__ == "__main__":
    main()
