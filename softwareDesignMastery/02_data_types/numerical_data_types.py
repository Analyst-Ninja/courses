"""
We should use Decimal type to store the currency values instead of float,
because it will give you more precision than the float

Decimal Type: more precision than float
But it is slower than float, so use it only when you need more precision
"""

from decimal import Decimal


def main():
    # nums_sum = 0.1 + 0.1 + 0.1
    # expected_sum = 0.3

    # print("Expected Sum: ", expected_sum)
    # print("Sum: ", nums_sum)

    # assert nums_sum == expected_sum  # Give error due to the precision issue

    # To fix this use Decimal type
    nums_sum = Decimal("0.1") + Decimal("0.1") + Decimal("0.1")
    expected_sum = Decimal("0.3")

    print("Expected Sum: ", expected_sum)
    print("Sum: ", nums_sum)

    assert nums_sum == expected_sum  # Give error due to the precision issue


if __name__ == "__main__":
    main()
