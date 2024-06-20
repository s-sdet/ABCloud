"""
Тесты для страницы списка Secrets.
https://paas-stage.dev-int.akbars.ru/info_system/finmarket/env/finmarket-dev/secrets
"""
import pytest
import base64
from pytest_testrail.plugin import pytestrail
from tests.constants_test_cases import DataCasesTableSecrets
from data.constants import InfoSystemNotice, SecretsNotice
from fixtures.pages.info_system.environment.secrets.secrets import SecretsTable


class TestSecretsTable:
    """Тесты для таблицы Secrets."""

    @pytestrail.case("C15238564")
    @pytest.mark.parametrize("locator, message", DataCasesTableSecrets.CHECK_NAMES_TABLE_SECRETS)
    def test_names_secrets_table(self, app, login_user, locator, message):
        """Проверка, что таблица Secrets содержит все нужные столбцы и их названия корректны."""
        app.menu_breadcrumbs.navigate_to_secrets()
        assert app.secrets.get_names_secrets_table_text(locator=locator) == message

    @pytestrail.case("C15206363")
    def test_return_to_env_list(self, app, login_user):
        """Проверка, что при нажатии стрелки "назад" в списке секретов происходит возврат в список контуров ИС."""
        app.menu_breadcrumbs.navigate_to_secrets()
        app.services.return_to_is()
        # Проверка, что произошел переход в список контуров ИС
        assert app.services.get_name_in_breadcrumbs() == InfoSystemNotice.NAME_IS_BACKLINK

    @pytestrail.case("C15541494")
    def test_reveal_hide_secret(self, app, login_user):
        """Проверка работоспособности кнопки показать/скрыть секрет."""
        app.menu_breadcrumbs.navigate_to_secrets()
        app.secrets.go_to_secret()
        app.secrets.click_radio_button()
        # Проверка, что после повторного нажатия на радио кнопку секрет изменил статус на Reveal
        assert app.secrets.get_text_secret_state() == SecretsNotice.REVEAL_SECRET

    @pytestrail.case("C15541499")
    def test_checking_secret_copy(self, app, login_user):
        """Проверка, что секрет скопирован после нажатия на иконку копирования."""
        app.menu_breadcrumbs.navigate_to_secrets()
        app.secrets.go_to_secret()
        app.secrets.click_secret_copy()
        # Проверка, что появилась всплывашка Содержимое скопировано
        assert app.secrets.get_text_snackbar() == SecretsNotice.SUCCESS_SNACKBAR

    @pytestrail.case("C15550774")
    def test_decoding_secrets(self, app, login_user):
        """
        Декодирование секрета auth из base64
        Секрет auth содержит в себе два секрета: username и password, разделенных ':'
        """
        app.menu_breadcrumbs.navigate_to_secrets()
        app.secrets.go_to_secret()
        # Получаем секрет auth и декодируем из base64
        secret_auth = base64.b64decode(app.secrets.secret_copy(locator=SecretsTable.AUTH)).decode()
        # Проверяем, что первая часть секрета (до ':') соответствует секрету username
        assert app.secrets.secret_copy(locator=SecretsTable.USERNAME) == secret_auth.partition(':')[0]
        # Проверяем, что вторая часть секрета (после ':') соответствует секрету password
        assert app.secrets.secret_copy(locator=SecretsTable.PASSWORD) == secret_auth.partition(':')[2]
