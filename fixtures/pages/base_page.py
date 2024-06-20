from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains


class BasePage:
    def __init__(self, app):
        self.app = app

    def _find_element(self, locator, wait_time=20):
        element = WebDriverWait(self.app.driver, wait_time) \
            .until(expected_conditions.presence_of_element_located(locator),
                   message=f"Can't find element by locator {locator}")
        return element

    def _find_elements(self, locator, wait_time=20):
        elements = WebDriverWait(self.app.driver, wait_time) \
            .until(expected_conditions.presence_of_all_elements_located(locator),
                   message=f"Can't find elements by locator {locator}")
        return elements

    def open_page(self, url: str):
        """Открытие страницы авторизации."""
        self.app.driver.get(url)

    def element_is_visible(self, locator, wait_time=10):
        """Проверка, что елемент не пресудствует на странице."""
        self._find_element(locator, wait_time)

    def element_is_enabled(self, locator, wait_time=10):
        """Проверка, что елемент пресудствует на странице и активен."""
        element = self._find_element(locator, wait_time)
        return element.is_enabled()

    def click(self, locator, wait_time=20):
        """Клик по элементу."""
        element = self._find_element(locator, wait_time)
        element.click()

    def clear(self, locator, wait_time=20):
        """Очистка поля ввода."""
        element = self._find_element(locator, wait_time)
        element.clear()

    def send_keys(self, locator, value: str, wait_time=20):
        """Ввод данных."""
        element = self._find_element(locator, wait_time)
        element.send_keys(value)

    def text(self, locator, wait_time=20) -> str:
        """Получение текста."""
        element = self._find_element(locator, wait_time)
        return element.text

    def get_text(self, locator, wait_time=20) -> str:
        """Получение текста."""
        element = self._find_element(locator, wait_time)
        return element.text

    def get_attribute(self, locator, attribute: str, wait_time=20) -> str:
        """Получение текста из атрибутов."""
        element = self._find_element(locator, wait_time)
        return element.get_attribute(attribute)

    def hover(self, locator, wait_time=20):
        """Наведение указателя мыши без клика."""
        element = self._find_element(locator, wait_time)
        ActionChains(self.app.driver).move_to_element(element).perform()

    def get_url(self) -> str:
        """Получить URL."""
        element = self.app.driver.current_url
        return element