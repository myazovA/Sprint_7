import requests
import pytest

from data import URL
from helpers import Helpers

@pytest.fixture
def generete_courier_data():
    login = Helpers.generate_random_string(10)
    password = Helpers.generate_random_string(10)
    first_name = Helpers.generate_random_string(10)

    payload = {
        "login": login,
        "password": password,
        "firstName": first_name
    }
    return payload

@pytest.fixture
def register_new_courier(generete_courier_data):
    payload = generete_courier_data
    response = requests.post(URL.url_create_courier, data=payload)
    return response

@pytest.fixture
def courier_login():
    login_data = register_new_courier
    response = requests.post(URL.url_login_courier, data=login_data)
    return response

