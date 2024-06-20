import pytest
from pytest_testrail.plugin import pytestrail
from tests.constants_test_cases import DataCasesDeleteIS
from data.constants import InfoSystemNotice


class TestDeleteInformationSystem:
    """
    Тесты для проверки удаления Информационной системы.
    https://paas-dev.dev-int.akbars.ru/
    """
    @pytestrail.case("C14784679")
    def test_deletion_information_system(self, app, create_is):
        """
        Тесты удаления Информационной системы
        Перед тестом запускается фикстура на создание ИС - create_is
        """
        app.delete_is.del_information_system(name_is=InfoSystemNotice.NAME, name=InfoSystemNotice.NAME)
        app.delete_is.click_delete_button()
        assert app.delete_is.success_delete_is_text() == InfoSystemNotice.SUCCESS_DELETE

    @pytestrail.case("C14979421", "C14979425", "C14979437", "C14979438", "C14979439")
    @pytest.mark.parametrize("name_is, message", DataCasesDeleteIS.VALIDATION_FIELD_DELETE_IS_INVALID)
    def test_invalid_deletion_information_system(self, app, login_user, name_is, message):
        """
        Тесты удаления Информационной системы с невалидным подтверждающим словом.
        assert, что кнопка "Удалить" не стала активна в fixtures/pages/info_system/delete_info_system.py
        """
        app.delete_is.invalid_delete_information_system(name_is=name_is, message=message)

    @pytestrail.case("C14979440", "C14979442", "C14979443")
    @pytest.mark.parametrize("name_is, locator, message", DataCasesDeleteIS.VALIDATION_CANCEL_DELETE_IS)
    def test_cancel_deletion_information_system(self, app, login_user, name_is, locator, message):
        """
        Тесты отмены удаления Информационной системы с заполнением и без заполнения подтверждающего слова.
        assert в fixtures/pages/info_system/delete_info_system.py
        """
        app.delete_is.cancel_del_information_system(name_is=name_is, locator=locator, message=message)
