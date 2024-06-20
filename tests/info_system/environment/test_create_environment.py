import pytest
from pytest_testrail.plugin import pytestrail
from tests.constants_test_cases import DataCasesEnvironment
from data.constants import EnvironmentNotice


class TestCreateEnvironment:
    """
    Тесты для проверки создания Контура.
    https://paas-dev.dev-int.akbars.ru/info_system/finmarket/env/create
    """

    @pytestrail.case("C14784680")
    def test_create_environment(self, app, login_user, random_name_env):
        """
        Тест на создание Контура
        Сразу после создания контура запускается тест на его удаление
        """
        app.create_env.add_info_to_environment(name=random_name_env, description=EnvironmentNotice.DESCRIPTION,
                                               chat_id=EnvironmentNotice.CHAT_ID)
        app.create_env.click_button_create_env()
        assert app.create_env.get_snackbar_success_text() == EnvironmentNotice.SUCCESS_CREATE
        app.delete_env.del_environment(name=random_name_env)  # Удаление созданного контура
        assert EnvironmentNotice.SUCCESS_DELETE in app.delete_env.get_snackbar_success_text()

    @pytestrail.case("C15004735", "C15177733", "C15004720", "C15004733", "C15004736", "C15004741",
                     "C15004742", "C15390965", "C15390968", "C15390969", "C15390970", "C15390971", "C15390972")
    @pytest.mark.parametrize("name, description, chat_id, locator, message",
                             DataCasesEnvironment.VALIDATION_INVALID_DATA)
    def test_checking_invalid_data(self, app, login_user, name, description, chat_id, locator, message):
        """Тесты на проверку полей с невалидными значениями."""
        app.create_env.add_info_to_environment(name=name, description=description, chat_id=chat_id)
        app.create_env.click_button_create_env()
        assert app.create_env.empty_fields_error_text(locator=locator) == message

    @pytestrail.case("C15004721", "C15004732", "C15004740", "C15390964", "C15390967", "C15390966")
    @pytest.mark.parametrize("name, description, chat_id, locator, message", DataCasesEnvironment.VALIDATION_VALID_DATA)
    def test_checking_valid_data(self, app, login_user, name, description, chat_id, locator, message):
        """Тесты на проверку полей с валидными значениями."""
        app.create_env.add_info_to_environment(name=name, description=description, chat_id=chat_id)
        assert app.create_env.empty_fields_error_text(locator=locator) != message
