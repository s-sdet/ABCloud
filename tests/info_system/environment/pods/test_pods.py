"""
Тесты для списка и страницы Pods.
https://paas-test.test-paas.dev-int.akbars.ru/informationsystems/is4/env/is4-autotest/pods
"""
import pytest
from pytest_testrail.plugin import pytestrail
from tests.constants_test_cases import DataCasesPods
from data.constants import PodsNotice, PVCNotice, InfoSystemNotice
from fixtures.pages.info_system.environment.pvc.pvc import PVC
from fixtures.pages.info_system.environment.pods.pods import Pods
import time


class TestPods:
    """
    Тесты для таблицы и страниц Pods.
    В тестах переход в раздел PVС выполняется фикстурой conftest.go_to_pods_list.
    """

    @pytestrail.case("C17054672", "C17054682")
    @pytest.mark.parametrize("table_name_locator, table_name", DataCasesPods.CHECK_NAMES_TABLE_PODS)
    def test_checking_names_pods_table(self, app, login_user, go_to_pods_page, table_name_locator, table_name):
        """
        Проверка, что таблица Pods содержит все нужные столбцы и их названия корректны.
        C17054682 - Проверка отображения названия страницы Pods, проверяется в фикстуре 'go_to_pods_list'.
        """
        assert app.base_page.get_text(locator=table_name_locator) == table_name

    @pytestrail.case("C17054671")
    def test_go_to_pod_page(self, app, login_user, go_to_pods_page):
        """Переход в конкретный Pod при нажатии на строку в таблице списка Pods."""
        app.base_page.click(locator=Pods.POD)
        assert app.base_page.get_text(locator=Pods.BACKLINK) == PodsNotice.POD

    @pytestrail.case("C17054679", "C17054678", "C17054684")
    def test_checking_date_in_pods_table(self, app, login_user, go_to_pods_page):
        """Проверка данных в таблице Pods."""
        assert app.base_page.get_text(locator=Pods.POD_NODE) == PodsNotice.PODS_NODE  # Проверка данных в поле NODE
        app.pods.show_tooltip()  # Наведение курсора, чтобы появился тултип
        assert PodsNotice.TOOLTIP in app.base_page.get_text(locator=Pods.TOOLTIP)  # Проверка даты создания в тултипе
        assert PodsNotice.BREADCRUMBS in app.pods.get_text(locator=Pods.BREADCRUMBS)  # Проверка названия раздела
        # в хлебных крошках

    @pytestrail.case("C17054686")
    def test_checking_url(self, app, login_user, go_to_pods_page):
        """Проверка, что URL раздела Pods корректный."""
        assert app.base_page.get_url() == PodsNotice.URL.format(app.url)

    @pytestrail.case("C17054681")
    def test_checking_button_is_visible(self, app, login_user, go_to_pods_page):
        """Проверка что кнопка Создать отображается при наличии доступа к системе."""
        assert app.base_page.element_is_enabled(locator=Pods.BUTTON) == True
