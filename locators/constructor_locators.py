from selenium.webdriver.common.by import By


class ConstructorLocators:

    CONSTRACTOR_BUTTON = (By.XPATH, "//p[contains(., 'Конструктор')]")
    ORDER_TAB = (By.XPATH, "//p[contains(@class, 'AppHeader_header__linkText__3q_va ml-2') and contains(text(), 'Лента Заказов')]")
    ING = (By.XPATH, "*//a[@href='/ingredient/61c0c5a71d1f82001bdaaa6d']")
    BUN = (By.XPATH, '//*[@href="/ingredient/61c0c5a71d1f82001bdaaa6c"]') 
    CHECKOUT_ORDER_BUTTON = (By.XPATH, "//button[contains(., 'Оформить заказ')]")
    INGREDIENT_MODAL_TITLE = (By.XPATH, "//h2[text()='Детали ингредиента']")
    INGREDIENT_MODAL_CLOSE_BUTTON = (By.XPATH, '//button[contains(@class,"close")]')
    ORDER_MODAL = (By.XPATH, '//h2[contains(@class, "Modal_modal__title__") and contains(@class, "text_type_digits-large")]')
    ORDER_MODAL_CLOSE_BUTTON = (By.XPATH, "//div[contains(@class,'Modal_modal__')]//button")
    ORDER_NUMBER = (By.XPATH, "//div[contains(@class,'Modal_modal__')]//h2")
    DROP_SPACE = (By.XPATH, "//span[contains(@class,'constructor-element__row')]//span[text()='Перетяните булочку сюда (верх)']")
    ING_COUNTER = (By.XPATH, ('//*[@href="/ingredient/61c0c5a71d1f82001bdaaa6c"]//p[contains(@class, '
                                    '"counter__num")]'))
    LOADING = (By.XPATH, '//img[contains(@class, "Modal_modal__loading")]')
