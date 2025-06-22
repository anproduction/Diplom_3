import pytest
import allure
from pages.main_page import MainPage
from pages.feed_page import FeedPage
from locators import MainPageLocators, OrderPageLocators

@allure.feature("Навигация по сайту")
class TestNavigation:

    @pytest.fixture(autouse=True)
    def setup(self, browser):
        self.main_page = MainPage(browser)
        self.feed_page = FeedPage(browser)
        self.main_page.open_main_page()

    @allure.story("Переход по кнопке Конструктор")
    @allure.title("Проверяем, что при клике на 'Конструктор' открывается главная страница конструктора")
    def test_click_constructor(self):
        with allure.step("Кликаем на кнопку 'Конструктор'"):
            self.main_page.click_constructor()

        with allure.step("Проверяем, что отображается текст 'Соберите бургер'"):
            assert self.main_page.is_displayed(MainPageLocators.CREATE_BURGER_TEXT), "Страница конструктора не открылась"

    @allure.story("Переход по кнопке Лента заказов")
    @allure.title("Проверяем, что при клике на 'Лента заказов' открывается страница с лентой заказов")
    def test_click_orders_feed(self):
        with allure.step("Кликаем на кнопку 'Лента заказов'"):
            self.main_page.click_orders_feed()

        with allure.step("Проверяем, что произошёл переход на /feed"):
            assert "/feed" in self.feed_page.driver.current_url, "URL не содержит /feed"

        with allure.step("Проверяем, что отображается счётчик заказов"):
            assert self.feed_page.is_displayed(OrderPageLocators.ALL_ORDERS_COUNTER), \
                "Счётчик заказов не отображается — страница ленты заказов не загрузилась"
