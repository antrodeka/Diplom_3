import allure

from locators.order_locators import OrderLocators
from locators.constructor_locators import ConstructorLocators

from pages.constructor_page import ConstractorPage


class OrderPage(ConstractorPage):

    @allure.step('Количество заказов за все время')
    def check_total_order_counter(self):
        return self.get_text(OrderLocators.TOTAL_COUNTER)

    @allure.step('Количество заказов за сегодня')
    def check_today_order_counter(self):
        return self.get_text(OrderLocators.TODAY_COUNTER)

    @allure.step('Получение номера заказа в работе')
    def check_number_order_in_work(self):
        return self.get_text(OrderLocators.ORDER_IN_PROGRESS)

    @allure.step('Ожидание надписи количество заказов за сегодня')
    def wait_today_order_counter(self):
        return self.wait_for_visibility(OrderLocators.TODAY_COUNTER)

    @allure.step('Ожидание надписи количество заказов за все время')
    def wait_total_order_counter(self):
        return self.wait_for_visibility(OrderLocators.TOTAL_COUNTER)

    @allure.step('Клик по кнопке Лента заказов')
    def click_order_button(self):
        return self.click_when_clickable_2(ConstructorLocators.ORDER_TAB)

    @allure.step('Ожидание кнопки Лента заказов')
    def wait_order_button(self):
        return self.wait_for_visibility(ConstructorLocators.ORDER_TAB)

    @allure.step('Ожидание и клик по кнопке Лента заказов с actoinvhain')
    def wait_and_click_order_with_actoinchain(self):
        return self.wait_and_click_button_with_actoinvhain(
            ConstructorLocators.ORDER_TAB)

    @allure.step('Ожидание надписи В работе')
    def wait_for_title_in_work(self):
        return self.wait_for_visibility(OrderLocators.TITLE_IN_WORK)

    @allure.step('Ожидание номера заказа в разделе В работе')
    def wait_for_number_of_order_in_work(self):
        return self.wait_for_visibility(OrderLocators.TITLE_IN_WORK)

    @allure.step('Ожидание исчезновения надписи "Все текущие заказы готовы"')
    def check_invisible_all_orders_are_ready(self):
        return self.wait_until_not_visible(OrderLocators.ORDERS_COMPLETED)
