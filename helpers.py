import random
import string
import requests
from data import URL

class Helpers:
    @staticmethod
    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string

    @staticmethod
    def delete_courier(login, password):
        response_post = requests.post(URL.url_login_courier, data={
            "login": login,
            "password": password,
        })
        courier_id = response_post.json()['id']
        requests.delete(f'{URL.url_delete_courier}{courier_id}')
