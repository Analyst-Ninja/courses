"""
Understanding Lists in Python: Ordered
"""

from pprint import pprint


def main():
    """
    Main function to demonstrate list operations.
    """
    # Create a list of numbers
    numbers = [1, 2, 3, 4, 5]

    # Print the original list
    print("Original list:", numbers)

    # Append a new number to the list
    numbers.append(6)
    print("After appending 6:", numbers)

    # Remove a number from the list
    numbers.remove(3)
    print("After removing 3:", numbers)

    # Access an element by index
    print("Element at index 2:", numbers[2])

    # Iterate through the list
    print("Iterating through the list:")
    for num in numbers:
        print(num)

    # Pretty print the list of methods and attributes of the list object
    print("\nList of methods and attributes of the list object:")
    pprint(dir(numbers))

    # Mixed list with different data types
    mixed_list = [1, "two", 3.0, True, None, [1, "Hello"], {"key": "value"}]
    print("\nMixed list:", mixed_list)


if __name__ == "__main__":
    main()
