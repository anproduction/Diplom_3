import allure

@allure.feature("Счётчики заказов")
class TestOrderCounter:

    @allure.story("Проверка счётчиков заказов")
    @allure.title("Проверяем, что счётчики 'Выполнено за всё время' и 'Выполнено за сегодня' отображаются")
    def test_order_counters_visibility(self, main_page, feed_page):
        total = feed_page.get_total_orders_count()
        today = feed_page.get_today_orders_count()

        assert total is not None and total >= 0, "Общее количество заказов отсутствует или меньше 0"
        assert today is not None and today >= 0, "Количество заказов за сегодня отсутствует или меньше 0"
