import logging
from selenium.webdriver.common.by import By
from fixtures.pages.base_page import BasePage
from data.data import Auth
from data.constants import AuthNotice

logger = logging.getLogger("ABCloud")


class Authorization(BasePage):
    """
    Страница авторизации AbCloud.
    https://paas-dev.dev-int.akbars.ru/
    """
    USERNAME_FIELD = (By.NAME, "login")
    PASSWORD_FIELD = (By.NAME, "password")
    LOGIN_BUTTON = (By.ID, "submit-login")
    LOGO_TEXT = (By.XPATH, "//a[@data-testid='sidebar-logo-link']")
    HEADER_TEXT = (By.CLASS_NAME, "theme-heading")
    ERROR_AUTHORIZATION_TEXT = (By.ID, "login-error")
    USER_PROFILE_INFO = (By.XPATH, "//div[@data-testid='user-info']")
    USER_LOGOUT_LINK = (By.XPATH, "//a[@data-testid='user-logout-link']")

    def open_authorization_page(self):
        """Открытие страницы авторизации."""
        self.open_page(self.app.url)

    def entry_data_authorization(self):
        """Ввод логина и пароля в форму авторизации."""
        logger.info(f"Authorization data. login: {Auth.login}")
        self.send_keys(locator=self.USERNAME_FIELD, value=Auth.login)
        self.send_keys(locator=self.PASSWORD_FIELD, value=Auth.password)

    def entry_invalid_data_authorization(self, login, password):
        """Ввод невалидных логина и пароля в форму авторизации."""
        self.send_keys(locator=self.USERNAME_FIELD, value=login)
        self.send_keys(locator=self.PASSWORD_FIELD, value=password)

    def click_login(self):
        """Клик кнопки 'Login'"""
        self.click(locator=self.LOGIN_BUTTON)

    def logout_profile(self):
        """Выход из профиля."""
        self.click(locator=self.USER_PROFILE_INFO)
        self.click(locator=self.USER_LOGOUT_LINK)

    def success_authorization_text(self) -> str:
        """Получение текста рядом с логотипом, для подтверждения перехода в аккаунт после авторизации."""
        element = self.text(locator=self.LOGO_TEXT)
        return element

    def get_placeholder(self, locator, attribute):
        """Получение плейсхолдера в полях login и password."""
        element = self.get_attribute(locator=locator, attribute=attribute)
        return element

    def get_header_text(self) -> str:
        """Получение текста заголовка в форме авторизации."""
        element = self.text(locator=self.HEADER_TEXT)
        logger.info(f"Header text: {element}")
        return element

    def get_error_text(self) -> str:
        """Получение текста сообщения, что авторизация не успешна."""
        element = self.text(locator=self.ERROR_AUTHORIZATION_TEXT)
        logger.info(f"Header text: {element}")
        return element
