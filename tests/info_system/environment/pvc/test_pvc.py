"""
Тесты для списка и страницы Persistent Volume Claims.
https://paas-test.test-paas.dev-int.akbars.ru/informationsystems/is4/env/is4-autotest/persistentvolumeclaims
"""
import pytest
from pytest_testrail.plugin import pytestrail
from tests.constants_test_cases import DataCasesPVC
from data.constants import PVCNotice, InfoSystemNotice
from fixtures.pages.info_system.environment.pvc.pvc import PVC


class TestPVC:
    """
    Тесты для таблицы и страниц Persistent Volume Claims.
    В тестах переход в раздел PVС выполняется фикстурой conftest.go_to_pvc_page.
    """

    @pytestrail.case("C16821648")
    @pytest.mark.parametrize("table_locator, message", DataCasesPVC.CHECK_NAMES_TABLE_PVC)
    def test_names_pvc_table(self, app, login_user, go_to_pvc_page, table_locator, message):
        """Проверка, что таблица PVC содержит все нужные столбцы и их названия корректны."""
        assert app.base_page.get_text(locator=table_locator) == message

    @pytestrail.case("C16821652")
    def test_return_to_env(self, app, login_user, go_to_pvc_page):
        """Проверка, что при нажатии стрелки "назад" в списке PVC происходит возврат в список контуров."""
        app.pvc.return_to_env()
        # Проверка, что произошел переход в список контуров ИС
        assert app.pvc.get_name_in_backlink() == InfoSystemNotice.NAME_IS_BACKLINK

    @pytestrail.case("C16821647", "C16821658", "C16821659")
    def test_go_to_pvs(self, app, login_user, go_to_pvc_page):
        """Проверка перехода в сущность при нажатии на строку в таблице."""
        assert PVCNotice.BREADCRUMBS in app.pvc.get_name_in_breadcrumbs()  # Проверка, что название раздела присутствует
        # в хлебных крошках
        app.pvc.go_to_pvc_page()  # Переход в конкретную сущность
        assert app.pvc.get_name_pvc() == PVCNotice.PVC  # Проверка отображение названия заголовка страницы

    @pytestrail.case("C16821649", "C16821650", "C16821655")
    @pytest.mark.parametrize("capacity, access, storage, capacity_data, access_data, storage_data",
                             DataCasesPVC.CHECK_DATA_PVC_LIST)
    def test_checking_date_pvc_list(self, app, login_user, go_to_pvc_page, capacity, access, storage, capacity_data,
                                    access_data, storage_data):
        """
        Проверка данных в таблице PVC;
        Проверяются значения столбцов CAPACITY, ACCESS MODES и STORAGE CLASS в статусах Pending и Bound.
        """
        assert app.base_page.get_text(locator=capacity) == capacity_data
        assert app.base_page.get_text(locator=access) == access_data
        assert app.base_page.get_text(locator=storage) == storage_data

    @pytestrail.case("C16821654")
    def test_checking_tooltip_in_table(self, app, login_user, go_to_pvc_page):
        """Проверка тултупа в столбце AGE."""
        app.pvc.show_tooltip()  # Наведение курсора, чтобы появился тултип
        assert PVCNotice.TOOLTIP in app.base_page.get_text(locator=PVC.TOOLTIP)  # Проверка, что тултуп содержит нужную инфо-ю

    @pytestrail.case("C16821663")
    def test_checking_url(self, app, login_user, go_to_pvc_page):
        """Проверка, что URL раздела PVC корректный."""
        assert app.base_page.get_url() == PVCNotice.URL.format(app.url)

    @pytestrail.case("C16824111")
    def test_checking_data_in_field_storage_class(self, app, login_user, go_to_pvc_page):
        """
        Проверка отображение данных поля STORAGE CLASS при отсутствии данных.
        В таблице должен отображаться прочерк.
        """
        assert app.base_page.get_text(locator=PVC.STORAGE_EMPTY_DATA) == PVCNotice.STORAGE_EMPTY_DATA

