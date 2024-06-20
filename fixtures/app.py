from fixtures.pages.base_page import BasePage
from fixtures.pages.authorization import Authorization
from fixtures.pages.info_system.info_system import InformationSystem
from fixtures.pages.info_system.create_info_system import CreateInformationSystem
from fixtures.pages.info_system.delete_info_system import DeleteInformationSystem
from fixtures.pages.info_system.environment.services.services import ServicesTable
from fixtures.pages.info_system.environment.config_maps.config_maps import ConfigMapsTable
from fixtures.pages.menu_breadcrumbs import MenuBreadcrumbs
from fixtures.pages.info_system.environment.secrets.secrets import SecretsTable
from fixtures.pages.info_system.environment.create_environment import CreateEnvironment
from fixtures.pages.info_system.environment.delete_environment import DeleteEnvironment
from fixtures.pages.info_system.environment.ingresses.ingresses import Ingresses
from fixtures.pages.info_system.environment.pvc.pvc import PVC
from fixtures.pages.info_system.environment.pods.pods import Pods


class Application:
    def __init__(self, driver, url: str):
        self.driver = driver
        self.url = url
        self.base_page = BasePage(self)
        self.auth_page = Authorization(self)
        self.info_system = InformationSystem(self)
        self.create_is = CreateInformationSystem(self)
        self.delete_is = DeleteInformationSystem(self)
        self.services = ServicesTable(self)
        self.config_maps = ConfigMapsTable(self)
        self.menu_breadcrumbs = MenuBreadcrumbs(self)
        self.secrets = SecretsTable(self)
        self.create_env = CreateEnvironment(self)
        self.delete_env = DeleteEnvironment(self)
        self.ingresses = Ingresses(self)
        self.pvc = PVC(self)
        self.pods = Pods(self)

    def quit(self):
        self.driver.quit()
