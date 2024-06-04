import allure
import requests
from data import URL, ResponseMessages
from helpers import Helpers

@allure.story("Логин курьера")
class TestLoginCourier:

    @allure.title("Успешный логин")
    def test_login_courier_successful(self, generete_courier_data):
        payload = generete_courier_data
        requests.post(URL.url_create_courier, data=payload)
        response = requests.post(URL.url_login_courier, data=payload)
        response_body = response.json()
        assert response.status_code == 200 and 'id' in response_body.keys()
        Helpers.delete_courier(payload['login'], payload['password'])

    @allure.title("Ошибка, при вводе несуществующего логина")
    def test_login_courier_with_wrong_login_error_404(self, generete_courier_data):
        payload = generete_courier_data
        response = requests.post(URL.url_login_courier, data=payload)
        assert response.status_code == 404 and response.json()['message'] == ResponseMessages.account_not_found

    @allure.title("Ошибка, при вводе пароля без логина")
    def test_login_courier_without_login_error_400(self, generete_courier_data):
        payload = generete_courier_data
        payload['login'] = ''
        response = requests.post(URL.url_login_courier, data=payload)
        assert response.status_code == 400 and response.json()['message'] == ResponseMessages.not_enough_data_to_login

    @allure.title("Ошибка, при вводе пароля без пароля")
    def test_login_courier_without_login_error_400(self, generete_courier_data):
        payload = generete_courier_data
        payload['password'] = ''
        response = requests.post(URL.url_login_courier, data=payload)
        assert response.status_code == 400 and response.json()['message'] == ResponseMessages.not_enough_data_to_login
