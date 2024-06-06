class URL:
    url_main = 'https://qa-scooter.praktikum-services.ru/api/v1/'
    url_login_courier = f'{url_main}courier/login'
    url_create_courier = f'{url_main}courier'
    url_delete_courier = f'{url_main}courier/'
    url_create_order = f'{url_main}orders'
    url_get_order_list = f'{url_main}orders?courierId='
    url_accept_order = f'{url_main}orders/accept'
    url_get_order = f'{url_main}orders/track'

class ResponseMessages:
    account_not_found = 'Учетная запись не найдена'
    not_enough_data_to_login = "Недостаточно данных для входа"
    not_enough_data_to_create_account = 'Недостаточно данных для создания учетной записи'
    login_has_been_used = 'Этот логин уже используется. Попробуйте другой.'
    successful_registration = '{"ok":true}'

class OrderData:
    order_data = {
        "firstName": "Денис",
        "lastName": "Петров",
        "address": "Питер, д. 1",
        "metroStation": 1,
        "phone": "+7 777 777 77 77",
        "rentTime": 1,
        "deliveryDate": "2024-06-02",
        "comment": "zxc",
        "color": [
            "BLACK"
        ]
    }

    color_list = ['BLACK', 'GREY', 'BLACK, GREY', '']