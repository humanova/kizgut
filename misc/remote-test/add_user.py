import requests

API_URL = ''

user_data = {"username": "test",
             "category": "test category",
             "notes": "test notes"}

if __name__ == '__main__':
    r = requests.post(f'{API_URL}/user', data=user_data)