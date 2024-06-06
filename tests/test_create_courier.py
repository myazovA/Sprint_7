import allure
import requests
from data import URL, ResponseMessages
from helpers import Helpers

@allure.story("Создание курьера")
class TestCreateCourier:

    @allure.title("Курьер успешно создан")
    def test_create_courier_successful_registrarion(self, generete_courier_data):
        payload = generete_courier_data
        response = requests.post(URL.url_create_courier, data=payload)
        assert response.status_code == 201 and response.text == ResponseMessages.successful_registration
        Helpers.delete_courier(payload['login'], payload['password'])

    @allure.title("Ошибка, при создании курьера с занятым логином")
    def test_create_courier_with_existing_login_error_409(self, generete_courier_data):
        payload = generete_courier_data
        requests.post(URL.url_create_courier, data=payload)
        response = requests.post(URL.url_create_courier, data=payload)
        assert response.status_code == 409 and response.json()["message"] == ResponseMessages.login_has_been_used

    @allure.title("Ошибка, при создании курьера с пустым логином")
    def test_create_courier_with_null_login_error_400(self, generete_courier_data):
        payload = generete_courier_data
        payload['login'] = ''
        response = requests.post(URL.url_create_courier, data=payload)
        assert response.status_code == 400 and response.json()[
            'message'] == ResponseMessages.not_enough_data_to_create_account

    @allure.title("Ошибка, при создании курьера с пустым паролем")
    def test_create_courier_with_null_login_error_400(self, generete_courier_data):
        payload = generete_courier_data
        payload['password'] = ''
        response = requests.post(URL.url_create_courier, data=payload)
        assert response.status_code == 400 and response.json()[
            'message'] == ResponseMessages.not_enough_data_to_create_account
