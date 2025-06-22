import pytest
import allure
from pages.main_page import MainPage
from pages.feed_page import FeedPage

@allure.feature("Счётчики заказов")
class TestOrderCounter:

    @pytest.fixture(autouse=True)
    def setup(self, browser):
        self.main_page = MainPage(browser)
        self.feed_page = FeedPage(browser)
        self.main_page.open_main_page()
        self.feed_page.open_feed_page()

    @allure.story("Проверка счётчиков заказов")
    @allure.title("Проверяем, что счётчики 'Выполнено за всё время' и 'Выполнено за сегодня' отображаются")
    def test_order_counters_visibility(self):
        total = self.feed_page.get_total_orders_count()
        today = self.feed_page.get_today_orders_count()

        assert total is not None and total >= 0, "Общее количество заказов отсутствует или меньше 0"
        assert today is not None and today >= 0, "Количество заказов за сегодня отсутствует или меньше 0"
