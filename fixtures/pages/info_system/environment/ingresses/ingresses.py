"""
Страница списка Ingresses.
https://paas-dev.dev-int.akbars.ru/info_system/finmarket/env/finmarket-dev/ingresses
"""
import logging
from selenium.webdriver.common.by import By
from fixtures.pages.base_page import BasePage

logger = logging.getLogger("ABCloud")


class Ingresses(BasePage):
    """Список и страница Ingresses."""

    # Названия столбцов таблицы Ingresses
    INGRESS = (By.XPATH, "//th[@data-testid='metadata.name-head-table-cell']")
    HOSTNAME = (By.XPATH, "//th[@data-testid='spec.rules.host-head-table-cell']")
    SERVICES = (By.XPATH, "//th[@data-testid='spec.rules.http.paths-head-table-cell']")

    # Данные в списке ингрессов
    HOSTNAME_LIST = (By.XPATH, "//td[@data-testid='ingress-qa-spec.rules.host-table-cell']")
    SERVICE_LIST = (By.XPATH, "//a[@data-testid='example-svc-service-link']")
    SERVICE_HIDDEN_LIST = (By.LINK_TEXT, "web-stage-service")

    # Данные на странице ингрессов
    HOSTNAME_PAGE = (By.XPATH, "//a[@data-testid='ingress-qa.dev-int.akbars.ru-hostname-link']")
    SERVICE_PAGE = (By.XPATH, "//a[@data-testid='example-svc-service-link-0']")
    INGRESS_PAGE = (By.XPATH, "//a[@data-testid='ingress-qa-ingress-link']")

    SERVICE_TOOLTIP_LIST = (By.XPATH, "//div[@class='Tag Tag_variant_neutral Tag_size_xs']")  # Тултип
    BACKLINK_NAME = (By.XPATH, "//a[@data-testid='backlink']")  # Название раздела в хлебных крошках

    def go_to_ingress(self):
        """Переход на страницу ингресса."""
        self.click(locator=self.INGRESS_PAGE)

    def go_to_service(self, locator):
        """Переход на страницу сервиса."""
        self.click(locator=locator)

    def get_name_ingress(self, locator) -> str:
        """Получение название ингресса для проверки перехода в ингресс."""
        element = self.text(locator=locator)
        return element

    def get_name_service(self, locator) -> str:
        """Получение название сервиса для проверки перехода в сервис из ингресса."""
        element = self.text(locator=locator)
        return element

    def show_hidden(self):
        """Наведение на тултип, чтобы отобразился скрытый элемент."""
        self.click(locator=self.SERVICE_TOOLTIP_LIST)

    def checking_service_from_ingress_list(self, locator):
        """Переход на страницу сервиса."""
        name_service = self.get_name_ingress(locator=locator)
        self.go_to_service(locator=locator)
        # Проверка перехода на страницу секрета
        assert name_service == self.get_name_service(locator=Ingresses.BACKLINK_NAME)

    def checking_service_from_ingress_page(self, locator):
        """Переход на страницу ингресса с дальнейшим вызовом метода для перехода на страницу сервиса."""
        name_ingress = self.get_name_ingress(locator=Ingresses.INGRESS_PAGE)
        self.go_to_ingress()
        # Проверка перехода на страницу ингресса
        assert name_ingress == self.get_name_ingress(locator=Ingresses.BACKLINK_NAME)
        self.checking_service_from_ingress_list(locator=locator)

