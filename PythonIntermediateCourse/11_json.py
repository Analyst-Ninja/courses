import json

# person = {
#     'name' : 'Rohit',
#     'age' : 27,
#     'hasChildern' : False,
#     'interested roles' : ['Data Engineer', 'Data Scientist', 'Programmer']
# }

# personJSON = json.dumps(person, indent=4, sort_keys=True)
# # print(personJSON)

# with open('person.json', mode='+w') as file:
#     json.dump(person, file, indent=4)

# # Convert JSON String to Python Dict

# personDict = json.loads(personJSON)
# from pprint import pprint

# # From file'
# with open('person.json', '+r') as file:
#     personDict = json.load(file)
#     print(personDict)


class User:

    def __init__(self, name, age):
        self.name = name
        self.age = age


user = User("Rohit", 27)


def encode_user(obj):
    if isinstance(obj, User):
        return {"name": obj.name, "age": obj.age, obj.__class__.__name__: True}
    else:
        raise TypeError("Object of type User is not JSON serializable")


userJSON = json.dumps(user, indent=4, default=encode_user)

print(userJSON)
