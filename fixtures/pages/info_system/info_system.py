"""
Страница Информационных систем.
https://paas-dev.dev-int.akbars.ru/
"""
import logging
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from fixtures.pages.base_page import BasePage

logger = logging.getLogger("ABCloud")


class InformationSystem(BasePage):
    USERNAME_FIELD = (By.NAME, "login")
    PASSWORD_FIELD = (By.NAME, "password")
    LOGIN_BUTTON = (By.ID, "submit-login")
    CREATE_IS_BUTTON = (By.XPATH, "//a[@data-testid='create-info-system-link']")

    def entry_data_authorization(self, username, password):
        """Ввод данных в форму авторизации."""
        logger.info(f"Authorization data. login: {username}, password: {password}")
        self.send_keys(locator=self.USERNAME_FIELD, value=username)
        self.send_keys(locator=self.PASSWORD_FIELD, value=password)
        self.click(locator=self.LOGIN_BUTTON)

    def check_button_visible_or_not(self):
        """
        Проверяем видима ли кнопка создания ИС или нет.
        wait_time=10 задается в fixtures/pages/base_page.py
        """
        try:
            self.element_is_visible(locator=self.CREATE_IS_BUTTON)
            return True
        except TimeoutException:
            return False
