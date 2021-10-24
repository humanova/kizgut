import requests

API_URL = ''

reason_data = {"description": "test description",
               "evidence": "test evidence",
               "user_id": "test user_id"}

if __name__ == '__main__':
    r = requests.post(f'{API_URL}/reason', data=reason_data)