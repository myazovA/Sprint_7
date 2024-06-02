1. test_create_courier - Создание курьера
   1. test_create_courier_successful_registrarion - Курьер успешно создан
   2. test_create_courier_with_existing_login_error_409 - Ошибка, при создании курьера с занятым логином
   3. test_create_courier_with_null_login_error_400 - Ошибка, при создании курьера с пустым обязательным полем
2. test_login_courier - Логин курьера
   1. test_login_courier_successful - Успешный логин
   2. test_login_courier_with_wrong_login_error_404 - Ошибка, при вводе несуществующего логина
   3. test_login_courier_without_login_error_400 - Ошибка, при вводе пароля без логина
3. test_order - Список заказов
   1. test_order_with_different_color_successful_added - Успешный заказ самоката с цветом {color}
   2. test_get_order_list_successful_got - Получение списка заказов