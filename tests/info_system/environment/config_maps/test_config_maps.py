"""
Тесты для страницы списка Config Maps.
https://paas-stage.dev-int.akbars.ru/info_system/finmarket/env/finmarket-dev/config_maps
"""
import pytest
from pytest_testrail.plugin import pytestrail
from tests.constants_test_cases import DataCasesTableConfigMaps
from data.constants import InfoSystemNotice
from fixtures.pages.info_system.environment.config_maps.config_maps import ConfigMapsTable


class TestConfigMapsTable:
    """Тесты для таблицы ConfigMaps."""
    @pytestrail.case("C14979237")
    @pytest.mark.parametrize("locator, message", DataCasesTableConfigMaps.CHECK_NAMES_TABLE_CONFIGMAPS)
    def test_names_configmaps_table(self, app, login_user, locator, message):
        """Проверка, что таблица содержит все нужные столбы и их названия корректны."""
        app.menu_breadcrumbs.navigate_to_configmaps()
        assert app.config_maps.get_names_configmaps_table_text(locator=locator) == message

    @pytestrail.case("C15206362")
    def test_return_to_env_list(self, app, login_user):
        """Проверка, что при нажатии стрелки "назад" в списке Config Maps происходит возврат в список контуров."""
        app.menu_breadcrumbs.navigate_to_configmaps()
        app.services.return_to_is()
        # Проверка, что произошел переход в список контуров ИС
        assert app.services.get_name_in_breadcrumbs() == InfoSystemNotice.NAME_IS_BACKLINK

    @pytestrail.case("C15489745", "C15489746")
    @pytest.mark.parametrize("locator, value", DataCasesTableConfigMaps.CHECK_FIELD_CONFIGMAPS)
    def test_checking_field_is_locked(self, app, login_user, locator, value):
        """
        Проверка залочены поля или нет
        Если поле ConfigMap в таблице имеет замочек - поля на странице этого ConfigMap так же должны иметь замочек
        При отстутсвии замочка - так же должен отсутсвовать в полях на странице этого ConfigMap
        """
        app.menu_breadcrumbs.navigate_to_configmaps()
        app.config_maps.go_to_config_map(locator=locator)
        assert app.config_maps.checking_field_is_locked(locator=ConfigMapsTable.LOCKED_ICON) is value
