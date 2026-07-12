import requests

dummy_db = {
    1: "Alice",
    2: "Bob",
    3: "Charlie",
}


def get_user_from_db(user_id):
    return dummy_db[user_id]


def get_users():
    response = requests.get("https://jsonplaceholder.typicode.com/users")
    if response.status_code == 200:
        return response.json()

    raise requests.HTTPError
