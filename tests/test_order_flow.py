import allure
from locators import MainPageLocators

@allure.feature("Проверка функционала заказа в Stellar Burgers")
class TestOrderFlow:

    @allure.story("Проверка открытия модального окна ингредиента и его закрытия")
    @allure.title("Открываем и закрываем окно деталей ингредиента")
    def test_ingredient_modal_open_and_close(self, authorized_main_page):
        main_page, _ = authorized_main_page

        with allure.step("Кликаем по первому ингредиенту (булке)"):
            main_page.click_first_ingredient()
        with allure.step("Проверяем, что модальное окно открылось"):
            assert main_page.is_ingredient_details_open(), "Модальное окно не открылось"
        with allure.step("Закрываем модальное окно"):
            main_page.close_ingredient_details()
        with allure.step("Проверяем, что модальное окно закрылось"):
            assert main_page.is_ingredient_details_closed(), "Модальное окно не закрылось"

    @allure.story("Проверка увеличения счётчика ингредиента")
    @allure.title("Добавляем ингредиент и проверяем счётчик")
    def test_ingredient_counter_increases(self, authorized_main_page):
        main_page, _ = authorized_main_page

        initial_counter = main_page.get_bun_ingredient_counter()
        with allure.step("Добавляем булку в заказ"):
            main_page.add_bun_ingredient_to_order()
        with allure.step("Проверяем, что счётчик увеличился"):
            new_counter = main_page.get_bun_ingredient_counter()
            assert new_counter > initial_counter, "Счётчик ингредиента не увеличился"

    @allure.story("Проверка увеличения счётчиков заказов после создания нового заказа")
    @allure.title("Создаём заказ и проверяем счётчики 'Выполнено за всё время' и 'Выполнено за сегодня'")
    def test_order_counters_increment_after_order(self, authorized_main_page):
        main_page, feed_page = authorized_main_page

        feed_page.open_feed_page()
        total_before = feed_page.get_total_orders_count()
        today_before = feed_page.get_today_orders_count()

        main_page.open_main_page()
        with allure.step("Добавляем булку в заказ и оформляем заказ"):
            main_page.add_bun_ingredient_to_order()
            main_page.click(MainPageLocators.ORDER_BUTTON)

        with allure.step("Получаем номер созданного заказа"):
            order_id = main_page.get_order_id()

        feed_page.open_feed_page()
        total_after = feed_page.get_total_orders_count()
        today_after = feed_page.get_today_orders_count()

        with allure.step("Проверяем, что общее количество заказов увеличилось"):
            assert total_after > total_before, "Общее количество заказов не увеличилось"
        with allure.step("Проверяем, что количество заказов за сегодня увеличилось"):
            assert today_after > today_before, "Количество заказов за сегодня не увеличилось"
        with allure.step(f"Проверяем, что заказ с номером {order_id} отображается в разделе 'В работе'"):
            assert feed_page.is_order_in_progress(order_id), "Номер заказа не появился в разделе 'В работе'"
