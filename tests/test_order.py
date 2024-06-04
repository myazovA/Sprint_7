import pytest
import allure
import requests
import json
from data import URL, OrderData
from helpers import Helpers

@allure.story("Список заказов")
class TestOrder:

    @allure.title("Успешный заказ самоката с цветом {color}")
    @pytest.mark.parametrize('color', OrderData.color_list)
    def test_order_with_different_color_successful_added(self, color):
        payload = OrderData.order_data
        payload['color'] = color
        payload = json.dumps(OrderData.order_data)
        response = requests.post(URL.url_create_order, data=payload)
        assert response.status_code == 201 and 'track' in response.json().keys()

    @allure.title("Получение списка заказов")
    def test_get_order_list_successful_got(self, generete_courier_data):
        payload = generete_courier_data
        requests.post(URL.url_create_courier, data=payload)
        login = requests.post(URL.url_login_courier, data=payload).json()
        create_order = requests.post(URL.url_create_order, data=json.dumps(OrderData.order_data)).json()
        get_order = requests.get(f"{URL.url_get_order}?t={create_order['track']}").json()

        requests.put(f"{URL.url_accept_order}/{get_order['order']['id']}?courierId={login['id']}")
        get_order_list = requests.get(f"{URL.url_get_order_list}{login['id']}").json()
        assert get_order_list['orders'][0]['id'] == get_order['order']['id']
        Helpers.delete_courier(payload['login'], payload['password'])