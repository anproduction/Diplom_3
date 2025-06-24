import allure
from locators import MainPageLocators, OrderPageLocators

@allure.feature("Навигация по сайту")
class TestNavigation:

    @allure.story("Переход по кнопке Конструктор")
    @allure.title("Проверяем, что при клике на 'Конструктор' открывается главная страница конструктора")
    def test_click_constructor(self, main_page):
        with allure.step("Кликаем на кнопку 'Конструктор'"):
            main_page.click_constructor()

        with allure.step("Проверяем, что отображается текст 'Соберите бургер'"):
            assert main_page.is_displayed(MainPageLocators.CREATE_BURGER_TEXT), "Страница конструктора не открылась"

    @allure.story("Переход по кнопке Лента заказов")
    @allure.title("Проверяем, что при клике на 'Лента заказов' открывается страница с лентой заказов")
    def test_click_orders_feed(self, main_page, feed_page):
        with allure.step("Кликаем на кнопку 'Лента заказов'"):
            main_page.click_orders_feed()

        with allure.step("Проверяем, что произошёл переход на /feed"):
            assert feed_page.current_url_contains("/feed"), "URL не содержит /feed"

        with allure.step("Проверяем, что отображается счётчик заказов"):
            assert feed_page.is_displayed(OrderPageLocators.ALL_ORDERS_COUNTER), \
                "Счётчик заказов не отображается — страница ленты заказов не загрузилась"
