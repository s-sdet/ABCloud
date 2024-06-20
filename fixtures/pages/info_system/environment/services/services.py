"""
Страница списка Сервисов.
https://paas-stage.dev-int.akbars.ru/info_system/finmarket/env/finmarket-dev/services
"""
import logging
from selenium.webdriver.common.by import By
from fixtures.pages.base_page import BasePage

logger = logging.getLogger("ABCloud")


class ServicesTable(BasePage):
    """Таблица Сервисов."""
    BACKLINK = (By.XPATH, "//a[@data-testid='backlink']")  # Стрелка назад в хлебных крошках
    CONTOUR_LINK = (By.XPATH, "//a[@data-testid='bc-env-link']")  # Ссылка на контур в хлебных крошках
    LABEL_BUSINESS_NAME = (By.XPATH, "//div[@class='Info_infoValueName__T1kTx']")  # Лейбл Бизнес наименование ИС
    SERVICE_NAME = (By.XPATH, "//td[@data-testid='web-stage-service-name-table-cell']")  # Локатор имени Сервиса

    # Название столбцов в списке Services
    NAME = (By.XPATH, "//th[@data-testid='name-head-table-cell']")
    TYPE = (By.XPATH, "//th[@data-testid='type-head-table-cell']")
    CLUSTER_IP = (By.XPATH, "//th[@data-testid='clusterIp-head-table-cell']")
    EXTERNAL_IP = (By.XPATH, "//th[@data-testid='externalIPs-head-table-cell']")
    PORTS = (By.XPATH, "//th[@data-testid='ports-head-table-cell']")
    TARGET_PORTS = (By.XPATH, "//th[@data-testid='ports-head-table-cell'][2]")
    SELECTORS = (By.XPATH, "//th[@data-testid='selector-head-table-cell']")
    AGE = (By.XPATH, "//th[@data-testid='creationTimestamp-head-table-cell']")

    # Название столбцов на странице Services
    PODS = (By.XPATH, "//th[@data-testid='cells[0]-head-table-cell']")
    STATUS = (By.XPATH, "//th[@data-testid='cells[2]-head-table-cell']")
    CONTAINERS_READY = (By.XPATH, "//th[@data-testid='cells[1]-head-table-cell']")
    RESTARTS = (By.XPATH, "//th[@data-testid='cells[3]-head-table-cell']")
    AGE_PAGE = (By.XPATH, "//th[@data-testid='object.metadata.creationTimestamp-head-table-cell']")
    TRAFFIC = (By.XPATH, "//th[@data-testid='cells[1]-head-table-cell'][2]")

    # Данные на странице сервиса
    HOSTNAME = (By.XPATH, "//p[@data-testid='service-hostname']")
    TYPE_PAGE = (By.XPATH, "//p[@data-testid='service-type']")
    PORTS_PAGE = (By.XPATH, "//p[@data-testid='service-ports-0']")
    TARGET_PORTS_PAGE = (By.XPATH, "//p[@data-testid='service-target-ports-0']")
    EXTERNAL_IP_PAGE = (By.XPATH, "//p[@data-testid='service-external-ips']")

    # Данные в списке сервисов
    TYPE_LIST = (By.XPATH, "//td[@data-testid='my-service-type-table-cell']")
    CLUSTER_IP_LIST = (By.XPATH, "//td[@data-testid='web-stage-service-clusterIp-table-cell']")
    PORTS_LIST = (By.XPATH, "//td[@data-testid='web-stage-service-ports-table-cell']")
    TARGET_PORTS_LIST = (By.XPATH, "//td[@data-testid='web-stage-service-ports-table-cell'][2]")
    EXTERNAL_IP_LIST = (By.XPATH, "//td[@data-testid='web-stage-service-externalIPs-table-cell']")

    def get_names_services_table_text(self, locator) -> str:
        """Получение названия столбцов таблицы Сервисов."""
        element = self.text(locator=locator)
        logger.info(f"Table column name Service: {element}")
        return element

    def return_to_is(self):
        """Возврат в список контуров ИС через стрелку "назад" в хлебных крошках."""
        self.click(locator=self.BACKLINK)

    def get_name_in_breadcrumbs(self) -> str:
        """Получение названия ИС для проверки возврата в список контуров."""
        element = self.text(locator=self.BACKLINK)
        return element

    def go_to_service(self):
        """Переход на страницу сервиса."""
        self.click(locator=self.SERVICE_NAME)

    def get_data_service_page(self, locator) -> str:
        """Получение данных со страницы сервиса."""
        element = self.text(locator=locator)
        logger.info(f"Data on the Service page: {element}")
        return element

    def get_data_service_table(self, locator) -> str:
        """Получение данных из таблицы сервиса."""
        element = self.text(locator=locator)
        logger.info(f"Data in the Service table: {element}")
        return element
