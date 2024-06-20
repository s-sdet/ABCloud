"""
Страница Persistent Volume Claims.
https://paas-test.test-paas.dev-int.akbars.ru/informationsystems/is4/env/is4-autotest/persistentvolumeclaims
"""
import logging
from selenium.webdriver.common.by import By
from fixtures.pages.base_page import BasePage
from data.constants import PVCNotice

logger = logging.getLogger("ABCloud")


class PVC(BasePage):
    """Таблицы и страницы Persistent Volume Claims."""

    # Локаторы названий столбцов таблицы Persistent Volume Claims
    NAME = (By.XPATH, "//th[@data-testid='cells[0]-head-table-cell']")
    CAPACITY = (By.XPATH, "//th[@data-testid='cells[3]-head-table-cell']")
    STATUS = (By.XPATH, "//th[@data-testid='cells[1]-head-table-cell']")
    ACCESS_MODES = (By.XPATH, "//th[@data-testid='cells[4]-head-table-cell']")
    STORAGE_CLASS = (By.XPATH, "//th[@data-testid='cells[5]-head-table-cell']")
    AGE = (By.XPATH, "//th[@data-testid='object.metadata.creationTimestamp-head-table-cell']")

    BREADCRUMBS = (By.XPATH, "//nav[@data-testid='breadcrumbs']")  # Хлебные крошки
    BACKLINK = (By.XPATH, "//a[@data-testid='backlink']")  # Стрелка назад в хлебных крошках
    PVC = (By.XPATH, "//td[@data-testid='pvc-local-cells[0]-table-cell']")
    AGE_DATA = (By.XPATH, "//td[@data-testid='pvc-local-object.metadata.creationTimestamp-table-cell']/div/p")
    TOOLTIP = (By.XPATH, "//div[@data-testid='tooltip-age']")

    # Локаторы данных в таблице PVC
    CAPACITY_STATUS_PENDING = (By.XPATH, "//td[@data-testid='pvc-local-cells[3]-table-cell']")
    ACCESS_MODES_STATUS_PENDING = (By.XPATH, "//td[@data-testid='pvc-local-cells[4]-table-cell']")
    STORAGE_STATUS_PENDING = (By.XPATH, "//td[@data-testid='pvc-local-cells[5]-table-cell']")
    CAPACITY_STATUS_BOUND = (By.XPATH, "//td[@data-testid='pvc-longhorn-cells[3]-table-cell']")
    ACCESS_MODES_STATUS_BOUND = (By.XPATH, "//td[@data-testid='pvc-longhorn-cells[4]-table-cell']")
    STORAGE_STATUS_BOUND = (By.XPATH, "//td[@data-testid='pvc-longhorn-cells[5]-table-cell']")
    STORAGE_EMPTY_DATA = (By.XPATH, "//td[@data-testid='aws-pvc-kuber-cells[5]-table-cell']")

    def return_to_env(self):
        """Возврат в список контуров через стрелку "назад" в хлебных крошках."""
        self.click(locator=self.BACKLINK)

    def get_name_in_backlink(self) -> str:
        """Получение названия ИС для проверки возврата в список контуров."""
        element = self.text(locator=self.BACKLINK)
        return element

    def get_name_in_breadcrumbs(self) -> str:
        """Получение названия PVC в хлебных крошках."""
        element = self.text(locator=self.BREADCRUMBS)
        return element

    def go_to_pvc_page(self):
        """Переход на страницу PVC: pvc-local"""
        self.click(locator=self.PVC)

    def get_name_pvc(self) -> str:
        """Получение названия PVC на его странице."""
        element = self.text(locator=self.BACKLINK)
        logger.info(f"Name PVC: {element}")
        return element

    def show_tooltip(self):
        """Наведение указателя на тултип в столбце AGE."""
        self.hover(locator=self.AGE_DATA)