
import allure

from locators.auth_locators import AuthLocators
from pages.base_page import BasePage
from urls import AUTH_URL


class AuthPage(BasePage):

    @allure.step('Авторизация в личном кабинете')
    def login(self, email, password):
        self.wait_and_click_button_with_actoinvhain(
            AuthLocators.BUTTON_PERS_ACC)
        self.wait_page_load(AUTH_URL)
        self.send_keys(AuthLocators.EMAIL_FIELD, email)
        self.send_keys(AuthLocators.PASS_FIELD, password)
        self.click(AuthLocators.BUTTON_LOGIN)
