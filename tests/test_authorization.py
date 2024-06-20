import pytest
from data.constants import AuthNotice
from pytest_testrail.plugin import pytestrail
from tests.constants_test_cases import DataCasesAuthorization


class TestLoginPage:
    """
    Тесты для страницы авторизации AbCloud.
    https://paas-dev.dev-int.akbars.ru/
    """
    @pytestrail.case("C13217511")
    def test_authorization(self, app, open_auth_page):
        """Тест авторизации с валидными данными."""
        app.auth_page.entry_data_authorization()
        app.auth_page.click_login()
        assert app.auth_page.success_authorization_text() == AuthNotice.LOGO_TEXT

    @pytestrail.case("C15215885", "C15215886")
    @pytest.mark.parametrize("locator, attribute, text", DataCasesAuthorization.CHECK_FORM_PLACEHOLDER)
    def test_check_placeholder(self, app, open_auth_page, locator, attribute, text):
        """Проверка наличия плейсхолдера в полях login и password."""
        assert app.auth_page.get_placeholder(locator=locator, attribute=attribute) == text

    @pytestrail.case("C15215887")
    def test_header_text(self, app, open_auth_page):
        """Проверка текста заголовка формы авторизации."""
        assert app.auth_page.get_header_text() == AuthNotice.HEADER_TEXT

    @pytestrail.case("C15215890", "C15215896")
    @pytest.mark.parametrize("login, password", DataCasesAuthorization.AUTHORIZATION_WITH_INVALID_DATA)
    def test_authorization_with_invalid_data(self, app, open_auth_page, login, password):
        """Тест авторизации с невалидными данными."""
        app.auth_page.entry_invalid_data_authorization(login=login, password=password)
        app.auth_page.click_login()
        assert app.auth_page.get_error_text() == AuthNotice.ERROR_AUTHORIZATION_TEXT

    @pytestrail.case("C13222170", "C13222142")
    @pytest.mark.parametrize("login, password", DataCasesAuthorization.AUTHORIZATION_WITH_EMPTY_DATA)
    def test_authorization_with_empty_data(self, app, open_auth_page, login, password):
        """Тест авторизации с незаполненными данными."""
        app.auth_page.entry_invalid_data_authorization(login=login, password=password)
        app.auth_page.click_login()
        assert app.auth_page.get_header_text() == AuthNotice.HEADER_TEXT

    @pytestrail.case("C13224118")
    def test_logout_profile(self, app, login_user):
        """Тест проверки выхода из профиля при нажатии на ФИО в боковом меню"""
        app.auth_page.logout_profile()
        assert app.auth_page.get_header_text() == AuthNotice.HEADER_TEXT
