from typing import TypedDict


class Person(TypedDict):
    name: str
    age: str


new_person: Person = {"name": "Rohit", "age": 28}

# new_person: Person = {
#     'name': 'Rohit',
#     'age': '28'
# }

print(new_person)
