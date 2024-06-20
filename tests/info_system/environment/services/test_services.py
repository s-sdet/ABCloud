"""
Тесты для страницы списка Сервисов.
https://paas-stage.dev-int.akbars.ru/info_system/finmarket/env/finmarket-dev/services
"""
import pytest
from pytest_testrail.plugin import pytestrail
from tests.constants_test_cases import DataCasesTableServices
from data.constants import InfoSystemNotice
from fixtures.pages.info_system.environment.services.services import ServicesTable


class TestServicesTable:
    """Тесты для таблицы Services."""
    @pytestrail.case("C14968093")
    @pytest.mark.parametrize("locator, name", DataCasesTableServices.CHECK_NAMES_TABLE_SERVICES)
    def test_names_services_table(self, app, login_user, locator, name):
        """Проверка, что таблица содержит все нужные столбы и их названия корректны."""
        app.menu_breadcrumbs.navigate_to_services()
        assert app.services.get_names_services_table_text(locator=locator) == name

    @pytestrail.case("C15206360")
    def test_return_to_env_list(self, app, login_user):
        """Проверка, что при нажатии стрелки "назад" в списке Services происходит возврат в список контуров."""
        app.menu_breadcrumbs.navigate_to_services()
        app.services.return_to_is()
        # Проверка, что произошел переход в список контуров ИС
        assert app.services.get_name_in_breadcrumbs() == InfoSystemNotice.NAME_IS_BACKLINK

    @pytestrail.case("C15431909")
    @pytest.mark.parametrize("locator, name", DataCasesTableServices.CHECK_NAMES_TABLE_SERVICES_PAGE)
    def test_names_services_page_table(self, app, login_user, locator, name):
        """Проверка, что таблица на странице сущности содержит все нужные столбцы и их названия корректны."""
        app.menu_breadcrumbs.navigate_to_services()
        app.services.go_to_service()
        assert app.services.get_names_services_table_text(locator=locator) == name

    @pytestrail.case("C15461257")
    @pytest.mark.parametrize("hostname, name_service, name_env", [(ServicesTable.HOSTNAME, ServicesTable.BACKLINK,
                                                                   ServicesTable.CONTOUR_LINK)])
    def test_checking_hostname(self, app, login_user, hostname, name_service, name_env):
        """
        Тест на проверку корректности отображения Hostname на странице сервиса
        Hostname состоит из имя сервиса + имя контура + svc.cluster.local. Имена берутся из хлебных крошек
        """
        app.menu_breadcrumbs.navigate_to_services()
        app.services.go_to_service()
        service = app.services.get_data_service_page(locator=name_service)
        env = app.services.get_data_service_page(locator=name_env)
        assert app.services.get_data_service_page(locator=hostname) == "%s.is4-%s.%s" % (service, env, "svc.cluster.local")

    @pytestrail.case("C15461258")
    @pytest.mark.parametrize("type_data, cluster_ip_data, type_list",
                             [(ServicesTable.TYPE_LIST, ServicesTable.CLUSTER_IP_LIST, ServicesTable.TYPE_PAGE)])
    def test_checking_type(self, app, login_user, type_data, cluster_ip_data, type_list):
        """
        Тест на проверку корректности отображения Type на странице сервиса
        Значение Type сравнивается с данными из таблицы списка сервисов, столбцы TYPE и CLUSTER IP
        """
        app.menu_breadcrumbs.navigate_to_services()
        type_data = app.services.get_data_service_table(locator=type_data)
        cluster_ip_data = app.services.get_data_service_table(locator=cluster_ip_data)
        app.services.go_to_service()
        assert app.services.get_data_service_page(locator=type_list) == "%s %s" % (type_data, cluster_ip_data)

    @pytestrail.case("C15461259", "C15461260", "C15462320")
    @pytest.mark.parametrize("data_table, data_page", DataCasesTableServices.CHECK_PORTS_SERVICES_PAGE)
    def test_checking_service_data(self, app, login_user, data_table, data_page):
        """
        Тест на проверку корректности отображения Ports, Target ports, External IP на странице сервиса
        Значение Ports и Target сравниваются с данными из таблицы списка сервисов, столбцы PORTS и TARGET PORTS соот-но
        Значение External IP сравнивается с данными из таблицы списка сервисов, столбец External IP
        """
        app.menu_breadcrumbs.navigate_to_services()
        element = app.services.get_data_service_table(locator=data_table)
        app.services.go_to_service()
        assert app.services.get_data_service_page(locator=data_page) == element
