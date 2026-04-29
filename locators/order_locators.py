from selenium.webdriver.common.by import By


class OrderLocators:

    TOTAL_COUNTER = (
        By.XPATH,
        "//p[text()='Выполнено за все время:']/following-sibling::p"
    )
    TODAY_COUNTER = (
        By.XPATH,
        "//p[text()='Выполнено за сегодня:']/following-sibling::p"
    )
    ORDER_IN_PROGRESS = (
        By.XPATH,
        "//ul[contains(@class,'OrderFeed_orderListReady')]//li"
    )
    ORDER_NUMBER_START = (By.XPATH, '//h2[text()="9999"]')
    TITLE_IN_WORK = (By.XPATH, "//p[contains(text(), 'В работе')]")
    ORDERS_COMPLETED = (By.XPATH, '//li[text()="Все текущие заказы готовы!"]')
