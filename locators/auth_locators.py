from selenium.webdriver.common.by import By


class AuthLocators:
    BUTTON_PERS_ACC = (By.XPATH, "//p[text()='Личный Кабинет']") 
    EMAIL_FIELD = (By.XPATH, "(//input[@name='name'])")
    PASS_FIELD = (By.XPATH, "(//input[@name='Пароль'])")
    BUTTON_LOGIN = (By.XPATH, '//button[text()="Войти"]')
