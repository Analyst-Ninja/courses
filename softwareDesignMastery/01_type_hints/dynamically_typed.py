"""
Dynamically typed code with type hints.
"""

LIMIT: int = 100
NAME: str = "Jhon"
AGE: int = 20

nums: list[int | float | bool | str] = [1, 2, 3, 4, 5.6, False, "Jhon"]


def verify_password(submitted_password: str, stored_hash: str = "1234") -> bool:
    """
    Verify password method
    """
    if submitted_password == stored_hash:
        return True
    return False


print(verify_password("hello"))


class Car:
    """
    Car Class
    """

    def __init__(self, name: str, brand: str, price: int) -> None:
        self.name = name
        self.brand = brand
        self.price = price


car = Car(name="M5 Competition", brand="BMW", price=30_000_000)
