import pytest
from data.constants import InfoSystemNotice
from pytest_testrail.plugin import pytestrail
from tests.constants_test_cases import DataCasesCreateIS
from fixtures.pages.info_system.create_info_system import CreateInformationSystem as CreateIS


class TestCreateInformationSystem:
    """
    Тесты для проверки создания Информационной системы.
    https://paas-dev.dev-int.akbars.ru/info_system/create
    """

    @pytestrail.case("C14784678", "C14784678", "C14979242")
    @pytest.mark.parametrize("status", [True, False])
    def test_create_information_system(self, app, login_user, status):
        """
        Тест на создание Информационной системы Pilot и Commercial
        После создания ИС проверяем, что она отображается в списке ИС - кейс "C14979242"
        После проверки отображения созданой ИС в списке всех ИС - вызывается тест на ее удаление
        """
        app.create_is.add_info_to_information_system(name=InfoSystemNotice.BUSINESS_NAME, name_is=InfoSystemNotice.NAME,
                                                     prefix=InfoSystemNotice.PREFIX,
                                                     description=InfoSystemNotice.DESCRIPTION, status_is=status)
        app.create_is.click_create_information_system()
        assert app.create_is.success_create_text() == InfoSystemNotice.SUCCESS_CREATE_IS  # Проверка, что ИС создана
        app.create_is.find_information_system(name_is=InfoSystemNotice.NAME)  # Проверка отображения ИС в списке ИС
        app.delete_is.del_information_system(name_is=InfoSystemNotice.NAME, name=InfoSystemNotice.NAME)  # Удаление ИС
        app.delete_is.click_delete_button()
        assert app.delete_is.success_delete_is_text() == InfoSystemNotice.SUCCESS_DELETE  # Проверка, что ИС удалена

    @pytestrail.case("C15311548", "C15311545")
    def test_invalid_creating_information_system(self, app, login_user):
        """
        Тест на создание Информационной системы без заполнения всех обязательных полей
        1й assert - проверка, что ИС не создана при пустых полях и мы остались в форме создания ИС
        2й assert - проверка, что у всех полей появились подсказки, что поле заполненно некорректно
        Циклом перебераются локаторы для получения подсказок из соответствующих полей ввода
        """
        app.create_is.add_info_to_information_system(name="", name_is="", prefix="", description="")
        app.create_is.click_create_information_system()
        assert app.create_is.get_breadcrumbs_create_is_text() == InfoSystemNotice.BREADCRUMBS_BACKLINK
        for locator in [CreateIS.ERROR_TEXT_BUSINESS_NAME, CreateIS.ERROR_TEXT_NAME_IS, CreateIS.ERROR_TEXT_PREFIX_IS,
                        CreateIS.ERROR_TEXT_DESCRIPTION]:
            assert InfoSystemNotice.ERROR_EMPTY_FIELDS in app.create_is.get_error_text(locator)

    @pytestrail.case("C14868479")
    def test_cancel_creating_information_system(self, app, login_user, random_name_is):
        """Тест на отмену создание Информационной системы после заполнения полей."""
        app.create_is.add_info_to_information_system(name=InfoSystemNotice.BUSINESS_NAME, name_is=random_name_is,
                                                     prefix=InfoSystemNotice.PREFIX,
                                                     description=InfoSystemNotice.DESCRIPTION)
        app.create_is.click_button_cancel_creating_information_system()
        assert app.create_is.get_breadcrumbs_text() == InfoSystemNotice.BREADCRUMBS

    @pytestrail.case("C14979410", "C14981148")
    @pytest.mark.parametrize("locator", [CreateIS.CANCEL_IS_LINK, CreateIS.BACKLINK_CREATE_IS])
    def test_cancel_creating_information_system_empty_fields(self, app, login_user, locator):
        """Тест на отмену создание Информационной системы без заполнения полей."""
        app.create_is.cancel_creating_of_information_system(locator=locator)
        assert app.create_is.get_breadcrumbs_text() == InfoSystemNotice.BREADCRUMBS

    @pytestrail.case("C15256303", "C14814973", "C15256304", "C14814979", "C14814980", "C14814981", "C14814982",
                     "C15342858", "C15342860", "C15256305", "C14868473", "C14868472", "C14868475", "C15357823",
                     "C15357824", "C15256306", "C15357826", "C16105545", "C16105546", "C16099221", "C16099226",
                     "C16099509", "C16099576", "C16100356", "C16100353", "C16100998", "C16104146", "C15004650",
                     "C16099248")
    @pytest.mark.parametrize("name, name_is, prefix, description, error, locator",
                             DataCasesCreateIS.VALIDATION_INVALID_DATA)
    def test_checking_invalid_data(self, app, login_user, name, name_is, prefix, description, error, locator):
        """Тесты на проверку полей с невалидными значениями."""
        app.create_is.add_info_to_information_system(name=name, name_is=name_is, prefix=prefix, description=description)
        app.create_is.click_create_information_system()
        assert app.create_is.get_error_text(locator=locator) == error

    @pytestrail.case("C14814972", "C15313821", "C15313826", "C16099219", "C16099225", "C16099228", "C16099506",
                     "C16099558", "C16099583", "C16099507", "C16099571", "C16099585", "C15357827", "C15357825",
                     "C16100354", "C16100355", "C16100350", "C16100351", "C16104151")
    @pytest.mark.parametrize("name, name_is, prefix, description, error, locator",
                             DataCasesCreateIS.VALIDATION_VALID_DATA)
    def test_checking_valid_data(self, app, login_user, name, name_is, prefix, description, error, locator):
        """Тесты на проверку полей с валидными значениями."""
        app.create_is.add_info_to_information_system(name=name, name_is=name_is, prefix=prefix, description=description)
        app.create_is.click_create_information_system()
        assert app.create_is.get_error_text(locator=locator) != error
