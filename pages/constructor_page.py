import allure

from locators.constructor_locators import ConstructorLocators
from locators.auth_locators import AuthLocators
from locators.order_locators import OrderLocators
from pages.base_page import BasePage
from urls import BASE_URL, ORDER_URL


class ConstractorPage(BasePage):

    @allure.step('Клик по кнопке Конструктор')
    def click_constructor_button(self):
        return self.click(ConstructorLocators.CONSTRACTOR_BUTTON)

    @allure.step('Клик по кнопке Лента заказов')
    def click_order_button(self):
        return self.click_when_clickable(ConstructorLocators.ORDER_TAB)

    @allure.step('Ожидание кнопки Лента заказов')
    def wait_order_button(self):
        return self.wait_for_visibility(ConstructorLocators.ORDER_TAB)

    @allure.step('Ожидание и клик кнопки ЛЕНТА')
    def order_click_when_clickable_2(self):
        return self.click_when_clickable_2(ConstructorLocators.ORDER_TAB)

    @allure.step('Ожидание и клик кнопки БУЛКА')
    def bun_click_when_clickable_2(self):
        return self.click_when_clickable_2(ConstructorLocators.BUN)

    @allure.step('Ожидание и открытие кнопки ЛК')
    def auth_page_click(self):
        return self.click_when_clickable_2(AuthLocators.BUTTON_PERS_ACC)

    @allure.step('Ожидаем открытие страницы Конструктор')
    def wait_for_url_costructor(self):
        return self.wait_page_load(BASE_URL)

    @allure.step('Ожидаем открытия страницы Лента заказов')
    def wait_for_url_orders(self):
        return self.wait_page_load(ORDER_URL)

    @allure.step('Ожидаем кликабельности булки')
    def wait_clickable_bun(self):
        return self.wait_when_clickable(ConstructorLocators.BUN)

    @allure.step('Клик по булочке')
    def click_bun(self):
        return self.click_when_clickable(ConstructorLocators.BUN)

    @allure.step('Ожидаем появление окна с деталями ингридиентов')
    def wait_modal_details_ingredients(self):
        return self.wait_for_visibility(
            ConstructorLocators.INGREDIENT_MODAL_TITLE)

    @allure.step('Клик по крестику всплывающего окна')
    def click_cross_at_modal_details_window(self):
        return self.click(ConstructorLocators.ORDER_MODAL_CLOSE_BUTTON)

    @allure.step('Добавление булки в заказ')
    def add_filling_to_order(self):
        source = self.find_element(ConstructorLocators.BUN)
        target = self.find_element(ConstructorLocators.DROP_SPACE)
        return self.drag_and_drop_element(source,
                                          target)

    @allure.step('Получение названия модального окна')
    def get_text_ing_modal(self):
        return self.get_text(ConstructorLocators.INGREDIENT_MODAL_TITLE)

    @allure.step('Поиск всплывающего окна с деталями ингридиентов')
    def find_modal_details_window(self):
        return self.find_element(ConstructorLocators.INGREDIENT_MODAL_TITLE)

    @allure.step("Проверка, что модальное окно ингредиента не отображается")
    def ingredient_modal_is_not_visible(self, timeout=5):
        return self.wait_until_not_visible(
            ConstructorLocators.INGREDIENT_MODAL_TITLE, timeout)

    @allure.step('Ожидание увеличения счетчика ингредиента')
    def wait_for_ing_counter_raise(self):
        return self.wait_for_visibility(ConstructorLocators.ING_COUNTER)

    @allure.step('Получение значения на счетчике ингредиентов')
    def check_counter_of_ingredients(self):
        return self.get_text(ConstructorLocators.ING_COUNTER)

    @allure.step('Создание заказа и получение его номера')
    def make_order_and_get_order_number(self):
        self.add_filling_to_order()
        self.click(ConstructorLocators.CHECKOUT_ORDER_BUTTON)
        self.wait_for_visibility(ConstructorLocators.ORDER_NUMBER)
        self.wait_until_not_visible(OrderLocators.ORDER_NUMBER_START)
        order_number = self.get_text(ConstructorLocators.ORDER_NUMBER)
        self.click(ConstructorLocators.ORDER_MODAL_CLOSE_BUTTON)
        return order_number
