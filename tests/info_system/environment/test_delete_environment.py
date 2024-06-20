from pytest_testrail.plugin import pytestrail
from data.constants import EnvironmentNotice


class TestDeleteEnvironment:
    """
    Тесты для проверки удаления Контура.
    https://paas-dev.dev-int.akbars.ru/info_system/finmarket
    """
    @pytestrail.case("C14784681")
    def test_delete_environment(self, app, create_env, random_name_env):
        """
        Тест удаления контура
        Перед тестом запускается фикстура на создание контура - create_env
        """
        app.delete_env.del_environment(name=random_name_env)
        assert EnvironmentNotice.SUCCESS_DELETE in app.delete_env.get_snackbar_success_text()
