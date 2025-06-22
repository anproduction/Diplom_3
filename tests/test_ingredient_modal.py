import pytest
import allure
from pages.main_page import MainPage

@allure.feature("Модальное окно ингредиента")
class TestIngredientModal:

    @pytest.fixture(autouse=True)
    def setup(self, browser):
        self.page = MainPage(browser)
        self.page.open_main_page()

    @allure.story("Открытие модального окна ингредиента")
    @allure.title("Проверяем, что по клику на ингредиент открывается модальное окно с деталями")
    def test_open_ingredient_modal(self):
        with allure.step("Кликаем по первому ингредиенту"):
            self.page.click_first_ingredient()

        with allure.step("Проверяем, что модальное окно открылось"):
            assert self.page.is_ingredient_details_open(), "Модальное окно с деталями ингредиента не открылось"

    @allure.story("Закрытие модального окна ингредиента")
    @allure.title("Проверяем, что модальное окно закрывается по клику на крестик")
    def test_close_ingredient_modal(self):
        with allure.step("Кликаем по первому ингредиенту, чтобы открыть модальное окно"):
            self.page.click_first_ingredient()

        with allure.step("Закрываем модальное окно"):
            self.page.close_ingredient_details()

        with allure.step("Проверяем, что модальное окно закрылось"):
            assert self.page.is_ingredient_details_closed(), "Модальное окно не закрылось"
