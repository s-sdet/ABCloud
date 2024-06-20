"""
Тесты для страницы списка Ingresses.
https://paas-dev.dev-int.akbars.ru/info_system/finmarket/env/finmarket-dev/ingresses
"""
import pytest
from pytest_testrail.plugin import pytestrail
from tests.constants_test_cases import DataCasesIngresses
from data.constants import InfoSystemNotice
from fixtures.pages.info_system.environment.ingresses.ingresses import Ingresses


class TestIngresses:
    """Тесты для списка и страницы Ingresses."""

    @pytestrail.case("C15626386")
    @pytest.mark.parametrize("locator, name", DataCasesIngresses.CHECK_NAMES_TABLE_INGRESSES)
    def test_names_ingresses_table(self, app, login_user, locator, name):
        """
        Проверка, что таблица Ingresses содержит все нужные столбцы и их названия корректны
        В assert получаем название столбца и сравниваем его с константным названием
        """
        app.menu_breadcrumbs.navigate_to_ingresses()
        assert app.base_page.get_text(locator=locator) == name

    @pytestrail.case("C15626388")
    def test_return_to_env_list(self, app, login_user):
        """Проверка, что при нажатии стрелки "назад" в списке Ingresses происходит возврат в список контуров."""
        app.menu_breadcrumbs.navigate_to_ingresses()
        app.services.return_to_is()
        # Проверка, что произошел переход в список контуров ИС
        assert app.services.get_name_in_breadcrumbs() == InfoSystemNotice.NAME_IS_BACKLINK

    @pytestrail.case("C15752893", "C15752894")
    @pytest.mark.parametrize("data_list, data_page", DataCasesIngresses.CHECK_DATA_INGRESSES)
    def test_checking_data(self, app, login_user, data_list, data_page):
        """
        Проверка, что данные (HOSTNAME, SERVICES) в списке ингрессов совпадают данными на странице конкретного ингресса
        """
        app.menu_breadcrumbs.navigate_to_ingresses()
        ingress_data = app.base_page.get_text(locator=data_list)  # Получение данных в списке ингрессов
        app.ingresses.go_to_ingress()
        assert ingress_data == app.base_page.get_text(locator=data_page)

    @pytestrail.case("C15780431")
    def test_go_to_service_from_ingress_list(self, app, login_user):
        """
        Проверка, что при нажатии на сервис в списке ингрессов, происходит переход на страницу данного сервиса
        Проверки переходов в нужные сущности в fixtures/pages/info_system/environment/ingresses/ingresses.py
        """
        app.menu_breadcrumbs.navigate_to_ingresses()
        app.ingresses.checking_service_from_ingress_list(locator=Ingresses.SERVICE_LIST)

    @pytestrail.case("C15780432")
    def test_go_to_hidden_service_from_ingress_list(self, app, login_user):
        """
        Проверка, что при нажатии на +1 в списке сервисов в таблице ингрессов, происходит переход на страницу сервиса
        Проверки переходов в нужные сущности в fixtures/pages/info_system/environment/ingresses/ingresses.py
        """
        app.menu_breadcrumbs.navigate_to_ingresses()
        app.ingresses.show_hidden()
        app.ingresses.checking_service_from_ingress_list(locator=Ingresses.SERVICE_HIDDEN_LIST)

    @pytestrail.case("C15780433")
    def test_go_to_service_from_ingress_page(self, app, login_user):
        """
        Проверка, что при нажатии на сервис на странице ингресса, происходит переход на страницу данного сервиса
        Проверки переходов в нужные сущности в fixtures/pages/info_system/environment/ingresses/ingresses.py
        """
        app.menu_breadcrumbs.navigate_to_ingresses()
        app.ingresses.checking_service_from_ingress_page(locator=Ingresses.SERVICE_PAGE)
