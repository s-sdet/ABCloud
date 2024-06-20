import logging
from selenium.webdriver.common.by import By
from fixtures.pages.base_page import BasePage

logger = logging.getLogger("ABCloud")


class DeleteEnvironment(BasePage):
    """
    Страница удаления Контура.
    https://paas-dev.dev-int.akbars.ru/info_system/finmarket
    """
    TEXT_CONFIRMATION = (By.XPATH, "//div[@data-testid='confirm-modal-control-string-input']/label")  # Поле для
    # подтверждающего слова
    BUTTON_DELETE = (By.XPATH, "//button[@data-testid='modal-confirm-button']")
    SUCCESS_DELETE_ENV = (By.XPATH, "//div[@data-testid='delete-resource-snackbar-success']")  # Контур удален

    def del_environment(self, name):
        """Удаление контура."""
        self.click(locator=(By.XPATH, f"//td[@data-testid='is4-{name}-actions-table-cell']/div"))  # Клик на
        # три точки для вызова выпадающего меню "Удалить"
        self.click(locator=(By.XPATH, f"//div[@data-testid='is4-{name}-delete-button']"))  # Клик по "Удалить"
        self.send_keys(locator=self.TEXT_CONFIRMATION, value=f"is4-{name}")  # Ввод подтверждающего текста
        self.click(locator=self.BUTTON_DELETE)  # Клик по кнопке Удалить

    def get_snackbar_success_text(self) -> str:
        """Получение текста всплывашки, что конутр успешно удален."""
        element = self.text(locator=self.SUCCESS_DELETE_ENV)
        return element
