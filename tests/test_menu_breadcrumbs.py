"""
Тесты для проверки навигации по боковому меню и хлебным крошкам.
https://paas-stage.dev-int.akbars.ru/
"""
from pytest_testrail.plugin import pytestrail


class TestMenuBreadcrumbs:
    """
    Тесты для навигации по меню и хлебным крошкам.
    Все assert в fixtures/pages/menu_breadcrumbs.py
    """
    @pytestrail.case("C15039147")
    def test_check_menu_and_breadcrumbs(self, app, login_user):
        app.menu_breadcrumbs.navigate_to_group_workloads()  # Проверка разделов в группе Workloads
        app.menu_breadcrumbs.return_to_is_breadcrumbs()  # Возврат через хлебные крошки
        app.menu_breadcrumbs.navigate_to_group_networking()  # Проверка разделов в группе Networking
        app.menu_breadcrumbs.return_to_is_breadcrumbs()  # Возврат через хлебные крошки
        app.menu_breadcrumbs.navigate_to_group_configs()  # Проверка разделов в группе Configs
