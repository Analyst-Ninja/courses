"""
Understanding Dictionaries in Python: Unordered
It hashed the key to the address in memory, hence the finding the key in dictionary is very fast
Time Complexity - O(1) / Constant
"""


def main():
    """
    Main function to demonstrate dictionary operations.
    """
    # Create and manuplulating a dictionary
    person: dict[int | str, int | str] = {
        "name": "Rohit",
        "profession": "Data Engineer",
        "age": 29,
        "city": "Bangalore",
    }
    print("Original Dictionary\n", person)

    # Dictionaries are mutatble: values can be changes based on their keys
    person["name"] = "Ajay"
    print("Dictionary after changing the value for key -> name to `Ajay`:\n", person)

    # Access the elements using thier keys
    profession = person["profession"]
    print(f"Profession: \n {profession}")

    # Adding a new key value pair in current dictionary
    person["company"] = "Moodys Ratings"
    print("After adding a new key-value pair:\n", person)

    # Removing a key value pair
    del person["city"]
    print("After removing a key-value pair:\n", person)

    # Key and value can be of different data types
    person[1] = "One"
    print(
        "Mixed typed dictionary:\n",
        person,
    )

    # Getting the list of all the keys and values
    print("Keys:", person.keys())
    print("Values:", person.values())

    # Getting a tuple of key and values pairs
    print("Key-value pair tuple:\n", person.items())

    # In newer version of Python - Dictionary maintains the order of the insertion
    data: dict[int, str] = {1: "One", 2: "Two", 3: "Three"}

    # Adding new key value to dict
    data[4] = "Four"

    for k, v in data.items():
        print(f"{k} -> {v}")


if __name__ == "__main__":
    main()
