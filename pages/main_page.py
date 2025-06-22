import allure
from pages.base_page import BasePage
from locators import MainPageLocators

class MainPage(BasePage):

    @allure.step("Открываем главную страницу")
    def open_main_page(self):
        self.open()

    @allure.step("Переходим в раздел 'Конструктор'")
    def click_constructor(self):
        self.click(MainPageLocators.CONSTRUCTOR_BUTTON)

    @allure.step("Переходим в раздел 'Лента заказов'")
    def click_orders_feed(self):
        self.click(MainPageLocators.ORDERS_FEED_BUTTON)

    @allure.step("Кликаем по первому ингредиенту (булке)")
    def click_first_ingredient(self):
        self.js_click(MainPageLocators.BUN_INGREDIENT)

    @allure.step("Проверяем, что окно деталей ингредиента отображается")
    def is_ingredient_details_open(self):
        return self.is_displayed(MainPageLocators.INGREDIENT_DETAILS)

    @allure.step("Закрываем окно деталей ингредиента")
    def close_ingredient_details(self):
        self.click(MainPageLocators.CLOSE_POP_UP_INGREDIENT_DETAILS_BUTTON)

    def is_ingredient_details_closed(self):
        return self.is_not_displayed(MainPageLocators.INGREDIENT_DETAILS)

    @allure.step("Получаем счётчик ингредиента (булка)")
    def get_bun_ingredient_counter(self):
        text = self.find(MainPageLocators.COUNTER).text
        try:
            return int(text)
        except ValueError:
            return 0

    @allure.step("Добавляем булку в заказ (кликаем по булке)")
    def add_bun_ingredient_to_order(self):
        self.js_click(MainPageLocators.BUN_INGREDIENT)

    @allure.step("Получаем номер созданного заказа")
    def get_order_id(self):
        return self.find(MainPageLocators.ORDER_ID).text.strip()
