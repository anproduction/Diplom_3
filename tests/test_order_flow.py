import pytest
import allure
from pages.main_page import MainPage
from pages.feed_page import FeedPage
from pages.auth_page import AuthPage
from data import EXISTING_USER
from locators import MainPageLocators

@allure.feature("Проверка функционала заказа в Stellar Burgers")
class TestOrderFlow:

    @pytest.fixture(autouse=True)
    def setup(self, browser):
        self.main_page = MainPage(browser)
        self.feed_page = FeedPage(browser)
        self.auth_page = AuthPage(browser)

        self.auth_page.open("/login")

        with allure.step("Авторизация существующим пользователем"):
            self.auth_page.login(EXISTING_USER['email'], EXISTING_USER['password'])

        self.main_page.open_main_page()

    @allure.story("Проверка открытия модального окна ингредиента и его закрытия")
    @allure.title("Открываем и закрываем окно деталей ингредиента")
    def test_ingredient_modal_open_and_close(self):
        with allure.step("Кликаем по первому ингредиенту (булке)"):
            self.main_page.click_first_ingredient()
        with allure.step("Проверяем, что модальное окно открылось"):
            assert self.main_page.is_ingredient_details_open(), "Модальное окно не открылось"
        with allure.step("Закрываем модальное окно"):
            self.main_page.close_ingredient_details()
        with allure.step("Проверяем, что модальное окно закрылось"):
            assert self.main_page.is_ingredient_details_closed(), "Модальное окно не закрылось"

    @allure.story("Проверка увеличения счётчика ингредиента")
    @allure.title("Добавляем ингредиент и проверяем счётчик")
    def test_ingredient_counter_increases(self):
        initial_counter = self.main_page.get_bun_ingredient_counter()
        with allure.step("Добавляем булку в заказ"):
            self.main_page.add_bun_ingredient_to_order()
        with allure.step("Проверяем, что счётчик увеличился"):
            new_counter = self.main_page.get_bun_ingredient_counter()
            assert new_counter > initial_counter, "Счётчик ингредиента не увеличился"

    @allure.story("Проверка увеличения счётчиков заказов после создания нового заказа")
    @allure.title("Создаём заказ и проверяем счётчики 'Выполнено за всё время' и 'Выполнено за сегодня'")
    def test_order_counters_increment_after_order(self):
        self.feed_page.open_feed_page()
        total_before = self.feed_page.get_total_orders_count()
        today_before = self.feed_page.get_today_orders_count()

        self.main_page.open_main_page()
        with allure.step("Добавляем булку в заказ и оформляем заказ"):
            self.main_page.add_bun_ingredient_to_order()
            self.main_page.click(MainPageLocators.ORDER_BUTTON)

        with allure.step("Получаем номер созданного заказа"):
            order_id = self.main_page.get_order_id()

        self.feed_page.open_feed_page()
        total_after = self.feed_page.get_total_orders_count()
        today_after = self.feed_page.get_today_orders_count()

        with allure.step("Проверяем, что общее количество заказов увеличилось"):
            assert total_after > total_before, "Общее количество заказов не увеличилось"
        with allure.step("Проверяем, что количество заказов за сегодня увеличилось"):
            assert today_after > today_before, "Количество заказов за сегодня не увеличилось"
        with allure.step(f"Проверяем, что заказ с номером {order_id} отображается в разделе 'В работе'"):
            assert self.feed_page.is_order_in_progress(order_id), "Номер заказа не появился в разделе 'В работе'"
