import allure
import requests
from data import URL, ResponseMessages

@allure.story("Логин курьера")
class TestLoginCourier:

    @allure.title("Успешный логин")
    def test_login_courier_successful(self, login_and_delete_courier):
        response = login_and_delete_courier
        response_body = response.json()
        assert response.status_code == 200 and 'id' in response_body.keys()

    @allure.title("Ошибка, при вводе несуществующего логина")
    def test_login_courier_with_wrong_login_error_404(self, create_new_courier):
        payload = create_new_courier
        response = requests.post(URL.url_login_courier, data=payload)
        assert response.status_code == 404 and response.json()['message'] == ResponseMessages.account_not_found

    @allure.title("Ошибка, при вводе пароля без логина")
    def test_login_courier_without_login_error_400(self, login_and_delete_courier, create_new_courier):
        payload = create_new_courier
        payload.pop('login')
        response = requests.post(URL.url_login_courier, data=payload)
        assert response.status_code == 400 and response.json()['message'] == ResponseMessages.not_enough_data_to_login
