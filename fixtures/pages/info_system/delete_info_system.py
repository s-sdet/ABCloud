from selenium.webdriver.common.by import By
from fixtures.pages.base_page import BasePage
from data.constants import InfoSystemNotice


class DeleteInformationSystem(BasePage):
    """
    Страница списка Информационных систем.
    https://paas-dev.dev-int.akbars.ru/
    """
    NAME_IS = (By.XPATH, "//td[@data-testid='is4-name-table-cell']")  # Информационная система
    DELETE_INPUT = (By.XPATH, "//div[@data-testid='confirm-modal-control-string-input']/label")  # Поле для ввода
    # подтверждения на удаление ИС
    DELETE_BUTTON = (By.XPATH, "//button[@data-testid='modal-confirm-button']")  # Кнопка Удалить
    CANCEL_BUTTON = (By.XPATH, "//button[@data-testid='modal-dismiss-button']")  # Кнопка Отмена
    CANCEL_CROSS = (By.XPATH, "//button[@name='close']")  # Крестик закрытия окна удаления ИС
    BREADCRUMBS_TEXT = (By.XPATH, "//h2[@data-testid='infosystem-list-page-header']")  # Хлебные крошки в списке ИС
    SUCCESS_DELETE_TEXT = (By.XPATH, "//div[@data-testid='delete-infosystem-snackbar-success']")  # ИС удалена
    BACKLINK = (By.XPATH, "//a[@data-testid='backlink']")  # Ссылка возврата в список ИС в хлебных крошках
    MODAL_WINDOW = (By.XPATH, "//h2[@data-testid='confirm-modal-title']")  # Заголовок удаления ИС

    def go_to_information_system(self, name_is):
        """Переход в нужную информационную систему."""
        name = self.get_text(locator=self.NAME_IS)
        self.click(locator=self.NAME_IS)  # Клик по нужной информационной системе
        self.del_information_system(name_is, name=name)

    def del_information_system(self, name_is, name):
        """Удаление информационной системы."""
        self.element_is_visible(locator=(By.XPATH, f"//button[@data-testid='{name}-actions-menu-button']"))
        self.click(locator=(By.XPATH, f"//button[@data-testid='{name}-actions-menu-button']"))  # Клик по меню справа
        self.click(locator=(By.XPATH, f"//div[@data-testid='{name}-delete-button']"))  # Клик по ссылке Удалить
        assert InfoSystemNotice.MODAL_WINDOW in self.get_name_modal_window()  # Проверка, что окно открылось
        self.send_keys(locator=self.DELETE_INPUT, value=name_is)  # Ввод названия ИС для подтверждения удаления

    def invalid_delete_information_system(self, name_is, message):
        """Удаление информационной системы с невалидным подтверждающим словом."""
        self.go_to_information_system(name_is=name_is)
        assert self.element_is_enabled(locator=self.DELETE_BUTTON) == message  # Проверка, что кнопка не стала активна

    def cancel_del_information_system(self, name_is, locator, message):
        """Отмена удаления информационной системы."""
        self.go_to_information_system(name_is=name_is)
        self.click(locator=locator)  # Клик по кнопке Отмена или крестику
        assert self.get_name_is_text() == message  # Проверка, что после отмены удаления сама ИС не удалилась

    def click_delete_button(self):
        """Клик по кнопке удаления"""
        self.click(locator=self.DELETE_BUTTON)

    def success_delete_is_text(self) -> str:
        """Получение текста всплывашки, что ИС успешно удалена."""
        element = self.text(locator=self.SUCCESS_DELETE_TEXT)
        return element

    def get_name_is_text(self) -> str:
        """Получение название информационной системы"""
        element = self.text(locator=self.BACKLINK)
        return element

    def get_name_modal_window(self) -> str:
        """Получение текста заголовка модального окна удаления ИС"""
        element = self.text(locator=self.MODAL_WINDOW)
        return element

    def go_back_to_list_is(self):
        """Вовзрат в список ИС после создания ИС через фикстуру create_is"""
        self.click(locator=self.BACKLINK)
