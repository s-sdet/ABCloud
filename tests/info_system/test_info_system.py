"""
Тесты для страницы списка Информационных систем.
https://paas-dev.dev-int.akbars.ru/
"""
import pytest
from pytest_testrail.plugin import pytestrail
from data.data import UserGroups


class TestInformationSystemPage:
    """Тесты для проверки отображения кнопки создания ИС."""

    @pytestrail.case("C15256563")
    @pytest.mark.parametrize("username, password, message", UserGroups.GROUP_USERS)
    def test_create_info_system_button_is_visible(self, app, open_auth_page, username, password, message):
        """Проверка, что у пользователей с разными правами отображается или не отображается кнопка 'Создать' ИС"""
        app.info_system.entry_data_authorization(username=username, password=password)
        assert app.info_system.check_button_visible_or_not() is message
