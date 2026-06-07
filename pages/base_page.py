import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 35)
        self.actions = ActionChains(driver)

    @allure.step("Поиск элемента")
    def find_element(self, locator, timeout=35):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )

    @allure.step("Клик по элементу")
    def click(self, locator):
        self.find_element(locator).click()

    @allure.step("Ожидание загрузки страницы")
    def wait_page_load(self, url):
        WebDriverWait(self.driver, 10).until(
            EC.url_to_be(url))

    def click_when_clickable_2(self, locator):
        WebDriverWait(self.driver, 40).until(
            EC.element_to_be_clickable(locator))
        self.driver.find_element(*locator).click()

    @allure.step("Ввод текста в поле")
    def send_keys(self, locator, input_text):
        element = self.find_element(locator)
        element.clear()
        element.send_keys(input_text)

    @allure.step("Получение текста элемента")
    def get_text(self, locator):
        element = self.find_element(locator)
        return element.text

    @allure.step("Кликаем по элементу, когда он станет кликабельным")
    def click_when_clickable(self, locator, timeout=40):
        element = WebDriverWait(
            self.driver, timeout).until(EC.element_to_be_clickable(locator))
        element.click()

    @allure.step("Ожидаем, когда элемент станет кликабельным")
    def wait_when_clickable(self, locator, timeout=40):
        WebDriverWait(
            self.driver, timeout).until(EC.element_to_be_clickable(locator))

    @allure.step("Получение текущего URL")
    def get_current_url(self):
        return self.driver.current_url

    @allure.step("Ожидание видимости элемента")
    def wait_for_visibility(self, locator):
        return WebDriverWait(self.driver, 40).until(
            EC.visibility_of_element_located(locator)
        )

    @allure.step("Ожидание исчезнования элемента")
    def wait_until_not_visible(self, locator, timeout=25):
        return WebDriverWait(self.driver, timeout).until(
            EC.invisibility_of_element_located(locator)
        )

    @allure.step("Клик по элементу")
    def js_click(self, element):
        self.driver.execute_script("arguments[0].click();", element)

    @allure.step('Перетаскивает элемент из одного места в другое')
    def drag_and_drop_element(self, source, target):

        self.driver.execute_script("""
        const source = arguments[0];
        const target = arguments[1];

        function createEvent(type) {
            const event = new Event(type, { bubbles: true, cancelable: true });
            event.dataTransfer = {
                data: {},
                setData: function(key, value) { this.data[key] = value; },
                getData: function(key) { return this.data[key]; }
            };
            return event;
        }

        const dragStartEvent = createEvent('dragstart');
        source.dispatchEvent(dragStartEvent);

        const dropEvent = createEvent('drop');
        dropEvent.dataTransfer = dragStartEvent.dataTransfer;
        target.dispatchEvent(dropEvent);

        const dragEndEvent = createEvent('dragend');
        dragEndEvent.dataTransfer = dragStartEvent.dataTransfer;
        source.dispatchEvent(dragEndEvent);
        """, source, target)

    def wait_and_click_button_with_actoinvhain(self, locator):
        element = WebDriverWait(self.driver, 35).until(
            EC.element_to_be_clickable((locator))
        )
        actions = ActionChains(self.driver)
        actions.move_to_element(element).click().perform()
