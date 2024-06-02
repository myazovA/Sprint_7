import allure
import requests
from data import URL, ResponseMessages

@allure.story("Создание курьера")
class TestCreateCourier:

    @allure.title("Курьер успешно создан")
    def test_create_courier_successful_registrarion(self, register_new_courier, login_and_delete_courier):
        response = register_new_courier
        assert response.status_code == 201 and response.text == ResponseMessages.successful_registration


    @allure.title("Ошибка, при создании курьера с занятым логином")
    def test_create_courier_with_existing_login_error_409(self, create_new_courier, login_and_delete_courier):
        payload = create_new_courier
        response = requests.post(URL.url_create_courier, data=payload)
        assert response.status_code == 409 and response.json()["message"] == ResponseMessages.login_has_been_used

    @allure.title("Ошибка, при создании курьера с пустым обязательным полем")
    def test_create_courier_with_null_login_error_400(self, create_new_courier):
        payload = create_new_courier
        payload['login'] = ''
        response = requests.post(URL.url_create_courier, data=payload)
        assert response.status_code == 400 and response.json()['message'] == ResponseMessages.not_enough_data_to_create_account
