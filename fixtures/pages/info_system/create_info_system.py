import logging
from selenium.webdriver.common.by import By
from fixtures.pages.base_page import BasePage
from data.constants import InfoSystemNotice

logger = logging.getLogger("ABCloud")


class CreateInformationSystem(BasePage):
    """
    Страница создания Информационной системы.
    https://paas-dev.dev-int.akbars.ru/info_system/create
    """
    BACK_LINK_TEXT = (By.XPATH, "//a[@data-testid='backlink']")  # Хлебные крошки для assert, что мы в форме создания ИС
    BREADCRUMBS_TEXT = (By.XPATH, "//h4[@data-testid='infosystem-list-page-header']")  # Хлебные крошки для assert,
    # что мы в списке ИС
    CREATE_IS_LINK = (By.XPATH, "//a[@data-testid='create-info-system-link']")  # Кнопка "Создать"
    BUSINESS_NAME_IS = (By.XPATH, "//div[@data-testid='businessname-input']/label")  # Поле "Бизнес наименование ИС"
    NAME_IS = (By.XPATH, "//div[@data-testid='info-system-name-input']/label")  # Поле "Наименование ИС"
    PREFIX = (By.XPATH, "//div[@data-testid='prefix-input']/label")  # Поле "Префикс ИС"
    DESCRIPTION = (By.XPATH, "//div[@data-testid='description-input']/label")  # Поле "Описание"
    STATUS_PILOT = (By.XPATH, "//div[@data-testid='status-radio-group']/div[position()=1]")  # Чекбокс "Pilot"
    STATUS_COMMERCIAL = (By.XPATH, "//div[@data-testid='status-radio-group']/div[position()=2]")  # Чекбокс "Commercial"
    CREATE_IS_BUTTON = (By.XPATH, "//button[@data-testid='create-info-system-button']")  # Кнопка "Создать" в форме ИС
    CANCEL_IS_LINK = (By.XPATH, "//a[@data-testid='cancel-button']")  # Кнопка "Отменить" в форме ИС
    BACKLINK_CREATE_IS = (By.XPATH, "//a[@data-testid='backlink']")  # Стрелка вернуться к списку ИС в форме создания ИС
    SUCCESS_CREATE_TEXT = (By.XPATH, "//div[@data-testid='create-infosystem-snackbar-success']")  # ИС создана
    BREADCRUMBS_ABCLOUD_LINK = (By.XPATH, "//a[@data-testid='ABCloud-link']")  # Хлебные крошки, ABCloud

    # Предупреждения об ошибках при создании ИС
    ERROR_TEXT_BUSINESS_NAME = (By.XPATH, "//div[@data-testid='businessname-input']/div")
    ERROR_TEXT_NAME_IS = (By.XPATH, "//div[@data-testid='info-system-name-input']/div")
    ERROR_TEXT_PREFIX_IS = (By.XPATH, "//div[@data-testid='prefix-input']/div")
    ERROR_TEXT_DESCRIPTION = (By.XPATH, "//div[@data-testid='description-input']/div")

    def add_info_to_information_system(self, name, name_is, prefix, description, status_is: bool = True):
        """
        1. Клик по кнопке "Создать", чтобы открылась форма создания ИС
        2. Ввод данных в форму создания Информационной системы.
        3. Клик выбор варианта статуса ИС
        :param status_is: По умолчанию Pilot, если status_is=False -> Commercial задается в автотестах
        tests/info_system/test_create_info_system.py
        """
        logger.info(f"Creation Information System. Business Name IS: {InfoSystemNotice.BUSINESS_NAME}, "
                    f"Name IS: {InfoSystemNotice.NAME}, Prefix: {InfoSystemNotice.PREFIX}, "
                    f"Description: {InfoSystemNotice.DESCRIPTION}")
        self.click(locator=self.CREATE_IS_LINK)
        # Проверяем, что произошел переход в форму создания Информационной системы
        assert self.text(locator=self.BACK_LINK_TEXT) == InfoSystemNotice.BREADCRUMBS_BACKLINK
        self.send_keys(locator=self.BUSINESS_NAME_IS, value=name)
        self.send_keys(locator=self.NAME_IS, value=name_is)
        self.send_keys(locator=self.PREFIX, value=prefix)
        self.send_keys(locator=self.DESCRIPTION, value=description)
        # Выбор варианта статуса при создании ИС
        status = self.STATUS_PILOT if status_is else self.STATUS_COMMERCIAL
        self.click(locator=status)

    def cancel_creating_of_information_system(self, locator):
        """Отмена создания информационной системы без заполнения полей."""
        self.click(locator=self.CREATE_IS_LINK)
        # Проверяем, что произошел переход в форму создания Информационной системы
        assert self.text(locator=self.BACK_LINK_TEXT) == InfoSystemNotice.BREADCRUMBS_BACKLINK
        self.click(locator=locator)

    def click_create_information_system(self):
        """Клик по кнопке 'Создать' в форме создания ИС."""
        self.click(locator=self.CREATE_IS_BUTTON)

    def find_information_system(self, name_is):
        """Проверка, что после создания ИС она появилась в списке всех ИС."""
        self.click(locator=self.BREADCRUMBS_ABCLOUD_LINK)  # Преход/возврат в список ИС через хлебные крошки
        self.element_is_visible(locator=(By.XPATH, f"//td[@data-testid='{name_is}-name-table-cell']"))
        self.click(locator=(By.XPATH, f"//td[@data-testid='{name_is}-name-table-cell']"))

    def click_button_cancel_creating_information_system(self):
        """Клик по кнопке 'Отменить' в форме создания ИС."""
        self.click(locator=self.CANCEL_IS_LINK)

    def success_create_text(self) -> str:
        """Получение текста всплывашки, что ИС успешно создана."""
        element = self.text(locator=self.SUCCESS_CREATE_TEXT)
        return element

    def get_breadcrumbs_text(self) -> str:
        """Получение текста из h3 в списке ИС, для проверки возвращения в список после отмены создания"""
        element = self.text(locator=self.BREADCRUMBS_TEXT)
        logger.info(f"Text h3: {element}")
        return element

    def get_breadcrumbs_create_is_text(self) -> str:
        """Получение текста из h3 в форме создания ИС, для проверки, что не вернулись в список ИС."""
        element = self.text(locator=self.BACK_LINK_TEXT)
        logger.info(f"Text h3: {element}")
        return element

    def get_error_text(self, locator) -> str:
        """Получение теста предупреждения при вводе невалидных данных значений."""
        element = self.text(locator=locator)
        logger.info(f"Error text: {element}")
        return element
