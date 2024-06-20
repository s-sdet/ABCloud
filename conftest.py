import pytest
import logging
import random
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from fixtures.app import Application
from data.constants import InfoSystemNotice, AuthNotice, EnvironmentNotice, PodsNotice
from fixtures.pages.info_system.environment.pods.pods import Pods

logger = logging.getLogger("ABCloud")


def pytest_addoption(parser):
    parser.addoption(
        "--url",
        action="store",
        default="https://***.akbars.ru/",
        help="ABCloud",
    ),
    parser.addoption("--headless", action="store_true", help="Headless mode"),


@pytest.fixture
def app(request):
    url = request.config.getoption("--url")
    headless = request.config.getoption("--headless")
    options = Options()
    options.add_argument("--start-maximized")
    options.add_argument("--allow-running-insecure-content")
    options.add_argument("--ignore-certificate-errors")
    if headless:
        options.add_argument("--headless")
    logger.info(f"Start app on {url}")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    app = Application(driver, url)
    yield app
    app.quit()


@pytest.fixture
def open_auth_page(app):
    """Фикстура открытия страницы авторизации."""
    app.auth_page.open_authorization_page()


@pytest.fixture
def login_user(app, open_auth_page):
    """Фикстура авторизации пользователя."""
    app.auth_page.entry_data_authorization()
    app.auth_page.click_login()
    assert app.auth_page.success_authorization_text() == AuthNotice.LOGO_TEXT


@pytest.fixture
def create_is(app, login_user):
    """Фикстура создания ИС для автотеста удаления ИС."""
    app.create_is.add_info_to_information_system(name=InfoSystemNotice.BUSINESS_NAME, name_is=InfoSystemNotice.NAME,
                                                 prefix=InfoSystemNotice.PREFIX,
                                                 description=InfoSystemNotice.DESCRIPTION)
    app.create_is.click_create_information_system()
    assert app.create_is.success_create_text() == InfoSystemNotice.SUCCESS_CREATE_IS


@pytest.fixture
def random_name_is(app):
    """Фикстура генерации Бизнес наименования ИС."""
    random_name = InfoSystemNotice.NAME + str(random.randint(1, 100))
    return random_name


@pytest.fixture
def random_name_env(app):
    """Фикстура генерации название Контура."""
    random_name = EnvironmentNotice.NAME + str(random.randint(1, 100))
    return random_name


@pytest.fixture
def create_env(app, login_user, random_name_env):
    """Фикстура создания Конутра для автотеста удаления Контура."""
    app.create_env.add_info_to_environment(name=random_name_env, description=EnvironmentNotice.DESCRIPTION,
                                           chat_id=EnvironmentNotice.CHAT_ID)
    app.create_env.click_button_create_env()
    assert app.create_env.get_snackbar_success_text() == EnvironmentNotice.SUCCESS_CREATE


@pytest.fixture
def go_to_pvc_page(app):
    """Навигация по левому меню до раздела Persistent Volume Claims."""
    app.menu_breadcrumbs.navigate_to_pvc()


@pytest.fixture
def go_to_pods_page(app):
    """Навигация по левому меню до раздела Pods."""
    app.menu_breadcrumbs.navigate_to_pods()
    assert app.base_page.get_text(locator=Pods.BACKLINK) == PodsNotice.BREADCRUMBS  # Проверка перехода в нужный раздел
