"""
Understanding NumPy Arrays
"""

import numpy as np


def main() -> None:
    """
    Main function to demonstrate NumPy array operations.
    """
    a = np.array([1, 2, 3])
    b = np.array([4, 5, 6])

    c = np.append(a, 4)

    print(f"a: {a}, c: {c}")
    print(f"id: a -> {id(a)}, id: c -> {id(c)}")

    print(f"a + b = {a + b}")
    print(f"a * b = {a * b}")

    data = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

    print(f"Mean: {np.mean(data)}")
    print(f"median: {np.median(data)}")
    print(f"std: {np.std(data) }")


if __name__ == "__main__":
    main()
