"""
Страница списка Secrets.
https://paas-stage.dev-int.akbars.ru/info_system/finmarket/env/finmarket-dev/secrets
"""
import logging
from selenium.webdriver.common.by import By
from fixtures.pages.base_page import BasePage
from data.constants import SecretsNotice

logger = logging.getLogger("ABCloud")


class SecretsTable(BasePage):
    """Таблица Secrets."""
    # Названия столбцов таблицы Secrets
    NAME = (By.XPATH, "//th[@data-testid='metadata.name-head-table-cell']")
    TYPE = (By.XPATH, "//th[@data-testid='type-head-table-cell']")
    AGE = (By.XPATH, "//th[@data-testid='metadata.creationTimestamp-head-table-cell']")

    SECRET = (By.XPATH, "//td[@data-testid='artifactory-metadata.name-table-cell']")  # Переход в нужный Secret
    BUTTON = (By.XPATH, "//span[@data-testid='secret-button-switch']")  # Кнопка статуса секрета
    SECRET_STATE = (By.XPATH, "//p[@data-testid='secret-show-status']")  # Статус секрета
    SECRET_COPY = (By.XPATH, "//div[@data-testid='secret-button-copy-auth']")  # Иконка копирования секрета
    SNACKBAR = (By.XPATH, "//div[@data-testid='copy-success-snackbar']")  # Всплывашка, что секрет скопирован

    # Секреты
    AUTH = (By.XPATH, "//div[@class='_root_yg9u8_1'][1]/div")
    USERNAME = (By.XPATH, "//div[@class='_root_yg9u8_1'][2]/div")
    PASSWORD = (By.XPATH, "//div[@class='_root_yg9u8_1'][3]/div")

    def get_names_secrets_table_text(self, locator) -> str:
        """Получение названия столбцов таблицы Secrets."""
        element = self.text(locator=locator)
        logger.info(f"Table column name Secrets: {element}")
        return element

    def go_to_secret(self):
        """
        Переход на страницу секрета
        После загрузки страницы секрет имеет статус Reveal
        """
        self.click(locator=self.SECRET)  # Переход на страницу секрета
        # Проверка, что после загрузки страницы секрет имеет статус Reveal
        assert self.get_text_secret_state() == SecretsNotice.REVEAL_SECRET
        self.click_radio_button()
        # Проверка, что после нажатия на радио кнопку секрет изменил статус на Hide
        assert self.get_text_secret_state() == SecretsNotice.HIDE_SECRET

    def click_radio_button(self):
        """Переключение показать/скрыть секрет."""
        self.click(locator=self.BUTTON)

    def get_text_secret_state(self) -> str:
        """Получение текста статуса секрета."""
        element = self.text(locator=SecretsTable.SECRET_STATE)
        return element

    def click_secret_copy(self):
        """Клик на иконку скопировать секрет."""
        self.click(locator=self.SECRET_COPY)

    def get_text_snackbar(self) -> str:
        """Получение текста всплывашки, что секрет скопирован."""
        element = self.text(locator=self.SNACKBAR, wait_time=20)
        return element

    def secret_copy(self, locator):
        """Копирование секрета."""
        element = self.text(locator=locator)
        return element
