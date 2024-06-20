"""
Страница Pods.
https://paas-test.test-paas.dev-int.akbars.ru/informationsystems/is4/env/is4-autotest/pods
"""
import logging
from selenium.webdriver.common.by import By
from fixtures.pages.base_page import BasePage
from data.constants import PVCNotice

logger = logging.getLogger("ABCloud")


class Pods(BasePage):
    """Таблицы и страницы Pods."""

    # Локаторы названий столбцов таблицы Pods
    NAME = (By.XPATH, "//th[@data-testid='cells[0]-head-table-cell']")
    STATUS = (By.XPATH, "//th[@data-testid='cells[2]-head-table-cell']")
    NODE = (By.XPATH, "//th[@data-testid='cells[6]-head-table-cell']")
    AGE = (By.XPATH, "//th[@data-testid='object.metadata.creationTimestamp-head-table-cell']")

    POD = (By.XPATH, "//td[@data-testid='nginx-cells[0]-table-cell']")
    BACKLINK = (By.XPATH, "//a[@data-testid='backlink']")
    POD_NODE = (By.XPATH, "//td[@data-testid='nginx-cells[6]-table-cell']")  # NODE пода
    AGE_DATA = (By.XPATH, "//td[@data-testid='nginx-object.metadata.creationTimestamp-table-cell']/div/p")
    TOOLTIP = (By.XPATH, "//div[@data-testid='tooltip-age']")
    BREADCRUMBS = (By.XPATH, "//nav[@data-testid='breadcrumbs']")
    BUTTON = (By.XPATH, "//button[@data-testid='create-yaml-button']")

    def show_tooltip(self):
        """Наведение указателя на тултип в столбце AGE."""
        self.hover(locator=self.AGE_DATA)