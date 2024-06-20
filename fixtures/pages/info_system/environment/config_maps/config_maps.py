"""
Страница списка Config Maps.
https://paas-stage.dev-int.akbars.ru/info_system/finmarket/env/finmarket-dev/config_maps
"""
import logging
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from fixtures.pages.base_page import BasePage

logger = logging.getLogger("ABCloud")


class ConfigMapsTable(BasePage):
    """Таблица ConfigMaps."""
    # Название столбцов списка ConfigMaps
    NAME = (By.XPATH, "//th[@data-testid='name-head-table-cell']")
    AGE = (By.XPATH, "//th[@data-testid='creationTimestamp-head-table-cell']")
    IMMUTABLE = (By.XPATH, "//th[@data-testid='immutable-head-table-cell']")

    LOCKED_ICON = (By.XPATH, "//div[@data-testid='key-field-0']/div/div")
    LOCKED_CONFIG_MAPS = (By.XPATH, "//td[@data-testid='immutable-test-immutable-table-cell']")  # Поле с замочком
    NOT_LOCKED_CONFIG_MAPS = (By.XPATH, "//td[@data-testid='envsecret-name-table-cell']")  # Поле без замочка

    def get_names_configmaps_table_text(self, locator) -> str:
        """Получение названия столбцов таблицы Config Maps."""
        element = self.text(locator=locator)
        logger.info(f"Table column name Config Maps: {element}")
        return element

    def checking_field_is_locked(self, locator):
        """
        Проверка имеет поле замочек или нет
        wait_time=10 задается в fixtures/pages/base_page.py
        """
        try:
            self.element_is_visible(locator=locator)
            return True
        except TimeoutException:
            return False

    def go_to_config_map(self, locator):
        """Переход на страницу Config Map."""
        self.click(locator=locator)
