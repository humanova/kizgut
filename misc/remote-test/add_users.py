import requests
import json

API_URL = ''

def add_users(users):
    for u in users:
        add_user(u)

def add_user(user):
    print(f'adding {user["username"]}...')
    r = requests.post(f'{API_URL}/user', json=user)
    print(f'status : {r.text}')

if __name__ == '__main__':
    user_data_path = 'test.json'
    with open(user_data_path, encoding='utf-8', mode='r+') as f:
        data = json.load(f)

    add_users(data)
