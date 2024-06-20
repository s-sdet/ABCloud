"""
Проверка навигации по боковому меню и хлебным крошкам.
https://paas-stage.dev-int.akbars.ru/
"""
import logging
from selenium.webdriver.common.by import By
from fixtures.pages.base_page import BasePage
from data.constants import PodsNotice, BreadcrumbsNotice, DeploymentsNotice, ServicesNotice, ConfigMapsNotice, \
    InfoSystemNotice, SecretsNotice, IngressesNotice, PVCNotice
import time
logger = logging.getLogger("ABCloud")


class MenuBreadcrumbs(BasePage):
    """Боковое меню и хлебные крошки."""
    MENU_IS = (By.XPATH, "//div[@data-testid='infoSystem-select']/div")  # Клик в меню по ИС
    MENU_NAME_IS = (By.XPATH, "//div[@class='List List_size_xs']/div[position()=2]")  # Клик в меню по имени ИС
    MENU_CONTUR = (By.XPATH, "//div[@data-testid='contours-select']")  # Клик в меню по Контуру
    MENU_NAME_CONTUR = (By.XPATH, "//div[@class='List List_size_xs']/div[position()=1]")  # Клик по конкретному Контуру
    MENU_PODS = (By.XPATH, "//a[@data-testid='sidebar-navigation-link-pods']")  # Клик по Pods
    MENU_DEPLOYMENTS = (By.XPATH, "//a[@data-testid='sidebar-navigation-link-deployments']")  # Клик по Deployments
    MENU_SERVICES = (By.XPATH, "//a[@data-testid='sidebar-navigation-link-services']")  # Клик по Services
    MENU_CONFIGMAPS = (By.XPATH, "//a[@data-testid='sidebar-navigation-link-config-maps']")  # Клик по Config Maps
    MENU_SECRETS = (By.XPATH, "//a[@data-testid='sidebar-navigation-link-secrets']")  # Клик по Secrets
    MENU_INGRESSES = (By.XPATH, "//a[@data-testid='sidebar-navigation-link-ingresses']")  # Клик по Ingresses
    MENU_PVC = (By.XPATH, "//a[@data-testid='sidebar-navigation-link-persistentvolumeclaims']")  # Клик по PVC
    BREADCRUMBS = (By.XPATH, "//nav[@data-testid='breadcrumbs']")  # Хлебные крошки
    BREADCRUMBS_IS_NAME_LINK = (By.XPATH, "//a[@data-testid='bc-infosystem-link']")  # Хлебные крошки, название ИС
    BREADCRUMBS_ABCLOUD_LINK = (By.XPATH, "//a[@data-testid='ABCloud-link']")  # Хлебные крошки, ABCloud
    IS_TEXT = (By.XPATH, "//h2[@data-testid='infosystem-list-page-header']")  # H2 Информационные системы
    WORKLOADS = (By.XPATH, "//div[@data-testid='sidebar-navigation-group-workloads']")
    NETWORKING = (By.XPATH, "//div[@data-testid='sidebar-navigation-group-networking']")
    CONFIGS = (By.XPATH, "//div[@data-testid='sidebar-navigation-group-configs']")
    STORAGE = (By.XPATH, "//div[@data-testid='sidebar-navigation-group-storage']")

    def navigate_to_contur(self):
        """Навигация по левому меню до выбора контура."""
        time.sleep(0.2)
        self.element_is_visible(locator=self.MENU_IS)
        self.click(locator=self.MENU_IS)  # Клик по Информационные системы
        self.element_is_visible(locator=self.MENU_NAME_IS)  # Проверка, что список Ис в меню стал видимым
        self.click(locator=self.MENU_NAME_IS)  # Клик по нужной Информационной системе
        time.sleep(0.2)
        self.element_is_visible(locator=self.MENU_NAME_CONTUR)  # Проверка, что пункты выпадающего меню стали видимыми
        self.click(locator=self.MENU_NAME_CONTUR)  # Клик по нужному Контуру
        time.sleep(0.2)

    def navigate_to_kubernetes_resources(self, menu, breadcrumbs_text):
        """
        Навигация по левому меню до нужной сущности Kubernetes."""
        time.sleep(0.2)
        self.element_is_visible(locator=menu)  # Проверка, что элемент меню стал видимым
        self.click(locator=menu)  # Клик по нужному разделу ресурсов
        # Проверка, что произошел переход на страницу этого ресурса
        assert breadcrumbs_text in self.get_breadcrumbs_text()

    def open_group_in_sidebar_navigation(self, group):
        """Клик по группе в сайтбаре для раскрытия разделов."""
        self.click(locator=group)

    def navigate_to_group_workloads(self):
        """Навигация по группе Workloads в сайтбаре."""
        self.navigate_to_contur()
        self.element_is_visible(locator=self.WORKLOADS)
        self.open_group_in_sidebar_navigation(group=self.WORKLOADS)
        self.navigate_to_kubernetes_resources(menu=self.MENU_PODS, breadcrumbs_text=PodsNotice.BREADCRUMBS)
        self.return_to_is_breadcrumbs()
        self.navigate_to_contur()
        self.navigate_to_kubernetes_resources(menu=self.MENU_DEPLOYMENTS,
                                              breadcrumbs_text=DeploymentsNotice.BREADCRUMBS)

    def navigate_to_group_networking(self):
        """Навигация по группе Networking в сайтбаре."""
        self.navigate_to_contur()
        time.sleep(0.2)
        self.element_is_visible(locator=self.NETWORKING)
        self.open_group_in_sidebar_navigation(group=self.NETWORKING)
        self.navigate_to_kubernetes_resources(menu=self.MENU_SERVICES, breadcrumbs_text=ServicesNotice.BREADCRUMBS)
        self.return_to_is_breadcrumbs()
        self.navigate_to_contur()
        self.navigate_to_kubernetes_resources(menu=self.MENU_INGRESSES, breadcrumbs_text=IngressesNotice.BREADCRUMBS)

    def navigate_to_group_configs(self):
        """Навигация по группе Configs в сайтбаре."""
        self.navigate_to_contur()
        time.sleep(0.2)
        self.element_is_visible(locator=self.CONFIGS)
        self.open_group_in_sidebar_navigation(group=self.CONFIGS)
        self.navigate_to_kubernetes_resources(menu=self.MENU_CONFIGMAPS, breadcrumbs_text=ConfigMapsNotice.BREADCRUMBS)
        self.return_to_is_breadcrumbs()
        self.navigate_to_contur()
        self.navigate_to_kubernetes_resources(menu=self.MENU_SECRETS, breadcrumbs_text=SecretsNotice.BREADCRUMBS)

    def navigate_to_pods(self):
        """Навигация по левому меню до Pods."""
        self.navigate_to_contur()
        self.open_group_in_sidebar_navigation(group=self.WORKLOADS)
        self.navigate_to_kubernetes_resources(menu=self.MENU_PODS, breadcrumbs_text=PodsNotice.BREADCRUMBS)

    def navigate_to_deployments(self):
        """Навигация по левому меню до Deployments."""
        self.navigate_to_contur()
        self.open_group_in_sidebar_navigation(group=self.WORKLOADS)
        self.navigate_to_kubernetes_resources(menu=self.MENU_DEPLOYMENTS,
                                              breadcrumbs_text=DeploymentsNotice.BREADCRUMBS)

    def navigate_to_services(self):
        """Навигация по левому меню до Services."""
        self.navigate_to_contur()
        self.open_group_in_sidebar_navigation(group=self.NETWORKING)
        self.navigate_to_kubernetes_resources(menu=self.MENU_SERVICES, breadcrumbs_text=ServicesNotice.BREADCRUMBS)

    def navigate_to_ingresses(self):
        """Навигация по левому меню до Ingresses."""
        self.navigate_to_contur()
        self.open_group_in_sidebar_navigation(group=self.NETWORKING)
        self.navigate_to_kubernetes_resources(menu=self.MENU_INGRESSES, breadcrumbs_text=IngressesNotice.BREADCRUMBS)

    def navigate_to_configmaps(self):
        """Навигация по левому меню до Config Maps."""
        self.navigate_to_contur()
        self.open_group_in_sidebar_navigation(group=self.CONFIGS)
        self.navigate_to_kubernetes_resources(menu=self.MENU_CONFIGMAPS, breadcrumbs_text=ConfigMapsNotice.BREADCRUMBS)

    def navigate_to_secrets(self):
        """Навигация по левому меню до Secrets."""
        self.navigate_to_contur()
        self.open_group_in_sidebar_navigation(group=self.CONFIGS)
        self.navigate_to_kubernetes_resources(menu=self.MENU_SECRETS, breadcrumbs_text=SecretsNotice.BREADCRUMBS)

    def navigate_to_pvc(self):
        """Навигация по левому меню до Persistent Volume Claims."""
        self.navigate_to_contur()
        self.open_group_in_sidebar_navigation(group=self.STORAGE)
        self.navigate_to_kubernetes_resources(menu=self.MENU_PVC, breadcrumbs_text=PVCNotice.BREADCRUMBS)

    def return_to_is_breadcrumbs(self):
        """Возврат в Информационную систему через хлебные крошки."""
        self.click(locator=self.BREADCRUMBS_IS_NAME_LINK)  # Преход/возврат в ИС через хлебные крошки
        # Проверка, что произошел переход на страницу Информационной системы через хлебные крошки
        assert BreadcrumbsNotice.BREADCRUMBS in self.get_breadcrumbs_text()
        self.click(locator=self.BREADCRUMBS_ABCLOUD_LINK)  # Преход/возврат в список ИС через хлебные крошки
        # Проверка, что произошел переход в список ИС через хлебные крошки
        assert self.get_is_text() == InfoSystemNotice.BREADCRUMBS

    def get_breadcrumbs_text(self) -> str:
        """Получение текста из хлебных крошек."""
        element = self.text(locator=self.BREADCRUMBS)
        logger.info(f"Breadcrumbs text: {element}")
        return element

    def get_is_text(self) -> str:
        """Получение текста h2 Информационные системы в списке ИС."""
        element = self.text(locator=self.IS_TEXT)
        logger.info(f"Text h2: {element}")
        return element
