import logging
from selenium.webdriver.common.by import By
from fixtures.pages.base_page import BasePage
from data.constants import InfoSystemNotice, EnvironmentNotice

logger = logging.getLogger("ABCloud")


class CreateEnvironment(BasePage):
    """
    Страница создания Контура.
    https://paas-dev.dev-int.akbars.ru/info_system/finmarket/env/create
    """
    NAME_IS = (By.XPATH, "//td[@data-testid='is4-name-table-cell']")  # Выбор нужной ИС
    NAME_BACKLINK = (By.XPATH, "//a[@data-testid='backlink']")  # Название ИС в форме создания Контура
    LINK_CREATE_ENV = (By.XPATH, "//a[@data-testid='createEnvButton']")  # Кнопка Создать контур (открывает форму
    # создания конутра)
    NAME_ENV = (By.XPATH, "//div[@data-testid='name-input']/label")  # Поле ввода названия контура
    DESCRIPTION_ENV = (By.XPATH, "//div[@data-testid='description-input']/label")  # Поле ввода описание контура
    CHAT_ID = (By.XPATH, "//div[@data-testid='chat-id-input']/label")  # Поле ввода номера Чат ID
    BUTTON_CREATE_ENV = (By.XPATH, "//button[@data-testid='create-environment-button']")  # Кнопка Создать контур
    ERROR_TEXT_EMPTY_NAME = (By.XPATH, "//div[@data-testid='name-input']/div")  # Ошибка поля Имя
    ERROR_TEXT_EMPTY_DESCRIPTION = (By.XPATH, "//div[@data-testid='description-input']/div")  # Ошибка поля Оптсание
    ERROR_TEXT_EMPTY_CHAT_ID = (By.XPATH, "//div[@data-testid='chat-id-input']/div")  # Ошибка поля Чат ID
    SUCCESS_CREATE_ENV = (By.XPATH, "//div[@data-testid='create-environment-snackbar-success']")  # Контур создан

    def add_info_to_environment(self, name, description, chat_id):
        logger.info(f"Creation Environment. Name: {name}, Description: {description}, Chat ID: {chat_id}")
        self.click(locator=self.NAME_IS)  # Клик по нужной ИС
        assert self.text(locator=self.NAME_BACKLINK) == InfoSystemNotice.NAME_IS_BACKLINK  # Проверка, что произошел
        # переход в список Контуров
        self.click(locator=self.LINK_CREATE_ENV)  # Клик по кнопка Создать контура
        assert self.text(locator=self.NAME_BACKLINK) == EnvironmentNotice.BACKLINK  # Проверка, что произошел
        # переход в форму создания Контура
        self.send_keys(locator=self.NAME_ENV, value=name)  # Ввод названия контура
        self.send_keys(locator=self.DESCRIPTION_ENV, value=description)  # Ввод описания контура
        self.send_keys(locator=self.CHAT_ID, value=chat_id)  # Ввод Чат ID

    def click_button_create_env(self):
        """Клик по кнопке Создать контур в списке контуров."""
        self.click(locator=self.BUTTON_CREATE_ENV)  # Клик по кнопка Создать контура

    def empty_fields_error_text(self, locator) -> str:
        """Получение теста предупреждения полей при создании Контура с невалидными значениями."""
        element = self.text(locator=locator)
        logger.info(f"Error text: {element}")
        return element

    def get_snackbar_success_text(self) -> str:
        """Получение текста всплывашки, что конутр успешно создан."""
        element = self.text(locator=self.SUCCESS_CREATE_ENV)
        return element
