import allure
from pages.constructor_page import ConstractorPage
from urls import ORDER_URL, BASE_URL
from data import MODAL_ORDER_TITLE, ING_COUNTER


class TestConstructorPage:
    @allure.title('Переход по клику на раздел «Лента заказов»')
    def test_orders_page_open(self, driver):
        constructor_page = ConstractorPage(driver)
        constructor_page.wait_order_button()
        constructor_page.order_click_when_clickable_2()
        constructor_page.wait_for_url_orders()
        current_url = constructor_page.get_current_url()
        assert current_url == ORDER_URL

    @allure.title('Переход по клику на «Конструктор»"')
    def test_constructor_page_open(self, driver):
        constructor_page = ConstractorPage(driver)
        constructor_page.wait_order_button()
        constructor_page.auth_page_click()
        constructor_page.click_constructor_button()
        current_url = constructor_page.get_current_url()
        assert current_url == BASE_URL

    @allure.title('При клике на ингредиент, появляется всплывающее окно с деталями')
    def test_modal_window_with_ing_details(self, driver):
        constructor_page = ConstractorPage(driver)
        constructor_page.wait_clickable_bun()
        constructor_page.click_bun()
        constructor_page.wait_modal_details_ingredients()
        modal_title = constructor_page.get_text_ing_modal()
        assert modal_title == MODAL_ORDER_TITLE

    @allure.title('Закрытие всплывающего окна с деталями ингридиента кликом на крестик')
    def test_close_modal_window_with_ing_details_by_cross(self, driver):
        constructor_page = ConstractorPage(driver)
        constructor_page.wait_clickable_bun()
        constructor_page.click_bun()
        constructor_page.wait_modal_details_ingredients()
        constructor_page.click_cross_at_modal_details_window()
        assert constructor_page.ingredient_modal_is_not_visible()

    @allure.title('При добавлении ингредиента в заказ счётчик увеличивается')
    def test_ingredient_counter_increase(self, driver):
        constructor_page = ConstractorPage(driver)
        constructor_page.add_filling_to_order()
        constructor_page.wait_for_ing_counter_raise()
        counter = constructor_page.check_counter_of_ingredients()
        assert counter == ING_COUNTER
