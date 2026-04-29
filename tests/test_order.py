import allure
from pages.order_page import OrderPage
from pages.auth_page import AuthPage


class TestOrder:

    @allure.title('При создании нового заказа счётчик «Выполнено за всё время» увеличивается')
    def test_new_order_increase_total_order_counter(self, driver, user):
        auth_page = AuthPage(driver)
        auth_page.login(user["email"], user["password"])
        order_page = OrderPage(driver)
        order_page.wait_and_click_order_with_actoinchain()
        order_page.wait_total_order_counter()
        total_counter_start = order_page.check_total_order_counter()
        order_page.click_constructor_button()
        order_page.make_order_and_get_order_number()
        order_page.wait_and_click_order_with_actoinchain()
        order_page.wait_for_url_orders()
        order_page.wait_total_order_counter()
        total_counter_new = order_page.check_total_order_counter()
        assert total_counter_start < total_counter_new

    @allure.title('При создании нового заказа счётчик «Выполнено за сегодня» увеличивается;')
    def test_new_order_increase_today_order_counter(self, driver, user):
        auth_page = AuthPage(driver)
        auth_page.login(user["email"], user["password"])
        order_page = OrderPage(driver)
        order_page.wait_order_button()
        order_page.wait_and_click_order_with_actoinchain()
        order_page.wait_today_order_counter()
        today_counter_start = order_page.check_today_order_counter()
        order_page.click_constructor_button()
        order_page.wait_clickable_bun()
        order_page.make_order_and_get_order_number()
        order_page.wait_and_click_order_with_actoinchain()
        order_page.wait_for_url_orders()
        order_page.wait_today_order_counter()
        today_counter_new = order_page.check_today_order_counter()
        assert today_counter_start < today_counter_new

    @allure.title('Появление номера зказа в разделе "В работе"')
    def test_number_of_order_appeared_in_work(self, driver, user):
        auth_page = AuthPage(driver)
        auth_page.login(user["email"], user["password"])
        order_page = OrderPage(driver)
        order_number = order_page.make_order_and_get_order_number()
        order_page.wait_order_button()
        order_page.wait_and_click_order_with_actoinchain()
        order_page.wait_for_url_orders()
        order_page.wait_for_title_in_work()
        order_page.check_invisible_all_orders_are_ready()
        order_page.wait_for_number_of_order_in_work()
        order_number_in_work = order_page.check_number_order_in_work()
        assert order_number_in_work == f'0{order_number}'
