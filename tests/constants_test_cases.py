"""Для параметризации тестов."""

from data.constants import InfoSystemNotice as IS
from data.data import Auth
from data.constants import AuthNotice, ServicesNotice, ConfigMapsNotice, SecretsNotice, EnvironmentNotice, \
    IngressesNotice, PVCNotice, PodsNotice
from fixtures.pages.authorization import Authorization
from fixtures.pages.info_system.create_info_system import CreateInformationSystem as CreateIS
from fixtures.pages.info_system.delete_info_system import DeleteInformationSystem
from fixtures.pages.info_system.environment.services.services import ServicesTable
from fixtures.pages.info_system.environment.config_maps.config_maps import ConfigMapsTable
from fixtures.pages.info_system.environment.secrets.secrets import SecretsTable
from fixtures.pages.info_system.environment.create_environment import CreateEnvironment
from fixtures.pages.info_system.environment.ingresses.ingresses import Ingresses
from fixtures.pages.info_system.environment.pvc.pvc import PVC
from fixtures.pages.info_system.environment.pods.pods import Pods


class DataCasesAuthorization:
    """Проверка негативных вариантов авторизации."""
    FORM_CONTROL_CHECK = [
        ["", Auth.password, AuthNotice.ERROR_AUTHORIZATION_TEXT],
        [Auth.login, "", AuthNotice.ERROR_AUTHORIZATION_TEXT],
    ]

    # Проверка отображения плейсхолдера в полях login и password.
    CHECK_FORM_PLACEHOLDER = [
        [Authorization.USERNAME_FIELD, "placeholder", AuthNotice.PLACEHOLDER_LOGIN],
        [Authorization.PASSWORD_FIELD, "placeholder", AuthNotice.PLACEHOLDER_PASSWORD],
    ]

    # Варианты авторизации с недалидными данными.
    AUTHORIZATION_WITH_INVALID_DATA = [
        [AuthNotice.INVALID_LOGIN, Auth.password],
        [Auth.login, AuthNotice.INVALID_PASSWORD],
    ]

    # Варианты авторизации с пустыми данными.
    AUTHORIZATION_WITH_EMPTY_DATA = [
        [AuthNotice.EMPTY_LOGIN, Auth.password],
        [Auth.login, AuthNotice.EMPTY_PASSWORD],
    ]


class DataCasesCreateIS:
    """Проверка негативных вариантов создания Информационной системы."""

    # Проверка пустых полей и невалидных значений при создании Информационной системы
    # 1-бизнес наименование, 2-наименование, 3-префикс, 4-описание, 5-текст ошибки для assert, 6-локатор ошибки
    VALIDATION_INVALID_DATA = [
        # Пустое поле "Бизнес наименование ИС"
        ["", IS.NAME, IS.PREFIX, IS.DESCRIPTION, IS.ERROR_EMPTY_FIELDS, CreateIS.ERROR_TEXT_BUSINESS_NAME],
        # Поле "Бизнес наименование ИС" > 256 символов
        [IS.BUSINESS_NAME_MAXIMUM_LENGTH, "", "", "", IS.ERROR_MAXIMUM_LENGTH_256, CreateIS.ERROR_TEXT_BUSINESS_NAME],
        # Пустое поле "Наименование ИС"
        [IS.BUSINESS_NAME, "", IS.PREFIX, IS.DESCRIPTION, IS.ERROR_EMPTY_FIELDS, CreateIS.ERROR_TEXT_NAME_IS],
        # "Наименование ИС" на кириллице
        ["", IS.NAME_IS_RUSSIAN, "", "", IS.ERROR_TRANSLITERATION, CreateIS.ERROR_TEXT_NAME_IS],
        # "Наименование ИС" на латинице в Uppercase
        ["", IS.NAME_IS_UPPERCASE, "", "", IS.ERROR_TRANSLITERATION, CreateIS.ERROR_TEXT_NAME_IS],
        # "Наименование ИС" < 5 символов
        ["", IS.NAME_IS_MINIMUM_LENGTH, "", "", IS.ERROR_MINIMUM_LENGTH_2, CreateIS.ERROR_TEXT_NAME_IS],
        # "Наименование ИС" > 40 символов
        ["", IS.NAME_IS_MAXIMUM_LENGTH, "", "", IS.ERROR_MAXIMUM_LENGTH_40, CreateIS.ERROR_TEXT_NAME_IS],
        # "Наименование ИС" на латинице в CamelCase
        ["", IS.NAME_IS_CAMELCASE, "", "", IS.ERROR_TRANSLITERATION, CreateIS.ERROR_TEXT_NAME_IS],
        # Только пробелы в поле "Наименование ИС"
        ["", IS.NAME_IS_SPACES, "", "", IS.ERROR_TRANSLITERATION, CreateIS.ERROR_TEXT_NAME_IS],
        # Пустое поле "Префикс ИС"
        [IS.BUSINESS_NAME, IS.NAME, "", IS.DESCRIPTION, IS.ERROR_EMPTY_FIELDS, CreateIS.ERROR_TEXT_PREFIX_IS],
        # "Префикс ИС" на латинице в Uppercase
        ["", "", IS.PREFIX_IS_UPPERCASE, "", IS.ERROR_PREFIX, CreateIS.ERROR_TEXT_PREFIX_IS],
        # "Префикс ИС" на кириллице 6 символов в Uppercase
        ["", "", IS.PREFIX_IS_RUSSIAN_LENGTH_6, "", IS.ERROR_PREFIX, CreateIS.ERROR_TEXT_PREFIX_IS],
        # "Префикс ИС" > 5 символов
        ["", "", IS.PREFIX_IS_MAXIMUM_LENGTH, "", IS.ERROR_MAXIMUM_LENGTH_5, CreateIS.ERROR_TEXT_PREFIX_IS],
        # "Префикс ИС" на латинице в Camelcase
        ["", "", IS.PREFIX_IS_CAMELCASE, "", IS.ERROR_PREFIX, CreateIS.ERROR_TEXT_PREFIX_IS],
        # Только пробелы в поле "Префикс ИС"
        ["", "", IS.PREFIX_IS_SPACES, "", IS.ERROR_PREFIX, CreateIS.ERROR_TEXT_PREFIX_IS],
        # Пустое поле "Описание"
        [IS.BUSINESS_NAME, IS.NAME, IS.PREFIX, "", IS.ERROR_EMPTY_FIELDS, CreateIS.ERROR_TEXT_DESCRIPTION],
        # Поле "Описание" > 256 символов
        ["", "", "", IS.DESCRIPTION_MAXIMUM_LENGTH, IS.ERROR_MAXIMUM_LENGTH_256, CreateIS.ERROR_TEXT_DESCRIPTION],
        # "Префикс ИС" на кириллице 5 символов в Uppercase
        ["", "", IS.PREFIX_IS_RUSSIAN_LENGTH_5, "", IS.ERROR_PREFIX, CreateIS.ERROR_TEXT_PREFIX_IS],
        # "Префикс ИС" на кириллице 1 символ в Uppercase
        ["", "", IS.PREFIX_IS_RUSSIAN_LENGTH_1, "", IS.ERROR_PREFIX, CreateIS.ERROR_TEXT_PREFIX_IS],

        # Поле "Бизнес наименование ИС" 1 символ на латинице в lowercase
        [IS.BUSINESS_NAME_ENGLISH_LENGTH_1, "", "", "", IS.ERROR_MINIMUM_LENGTH_2, CreateIS.ERROR_TEXT_BUSINESS_NAME],
        # Поле "Бизнес наименование ИС" 1 символ на латинице в Uppercase
        [IS.BUSINESS_NAME_ENGLISH_LENGTH_1.upper(), "", "", "", IS.ERROR_MINIMUM_LENGTH_2,
         CreateIS.ERROR_TEXT_BUSINESS_NAME],

        # Поле "Бизнес наименование ИС" 1 символ на кириллице в lowercase
        [IS.BUSINESS_NAME_RUSSIAN_LENGTH_1, "", "", "", IS.ERROR_MINIMUM_LENGTH_2, CreateIS.ERROR_TEXT_BUSINESS_NAME],
        # Поле "Бизнес наименование ИС" 1 символ на латинице в Uppercase
        [IS.BUSINESS_NAME_RUSSIAN_LENGTH_1.upper(), "", "", "", IS.ERROR_MINIMUM_LENGTH_2,
         CreateIS.ERROR_TEXT_BUSINESS_NAME],

        # "Бизнес наименование ИС" 1 спецсимвол
        [IS.BUSINESS_NAME_SPECIAL_CHARACTERS[0:1], "", "", "", IS.ERROR_MINIMUM_LENGTH_2,
         CreateIS.ERROR_TEXT_BUSINESS_NAME],

        # "Бизнес наименование ИС" 1 цифра
        [IS.BUSINESS_NAME_NUMBERS[0:1], "", "", "", IS.ERROR_MINIMUM_LENGTH_2, CreateIS.ERROR_TEXT_BUSINESS_NAME],

        # "Бизнес наименование ИС" с пробелом в начале текста
        [IS.BUSINESS_NAME_TEXT_WITH_SPACES, "", "", "", IS.ERROR_SPACES, CreateIS.ERROR_TEXT_BUSINESS_NAME],
        # "Бизнес наименование ИС" с пробелом в конце текста
        [IS.BUSINESS_NAME_TEXT_WITH_SPACES, "", "", "", IS.ERROR_SPACES, CreateIS.ERROR_TEXT_BUSINESS_NAME],

        # 2 пробела в поле "Бизнес наименование ИС"
        [IS.BUSINESS_NAME_SPACES, "", "", "", IS.ERROR_SPACES, CreateIS.ERROR_TEXT_BUSINESS_NAME],
        # 1 пробел пробелы в поле "Бизнес наименование ИС"
        [IS.BUSINESS_NAME_SPACES[0:1], "", "", "", IS.ERROR_MINIMUM_LENGTH_2, CreateIS.ERROR_TEXT_BUSINESS_NAME],
    ]

    # Проверка валидных значений при создании Информационной системы
    # 1-бизнес наименование, 2-наименование, 3-префикс, 4-описание, 5-текст ошибки для assert, 6-локатор ошибки
    VALIDATION_VALID_DATA = [
        # "Бизнес наименование ИС" 256 символов на латинице в lowercase
        [IS.BUSINESS_NAME_ENGLISH_LENGTH_256.lower(), "", "", "", IS.ERROR_SPACES, CreateIS.ERROR_TEXT_BUSINESS_NAME],
        # "Бизнес наименование ИС" 256 символов на латинице в Uppercase
        [IS.BUSINESS_NAME_ENGLISH_LENGTH_256.upper(), "", "", "", IS.ERROR_SPACES, CreateIS.ERROR_TEXT_BUSINESS_NAME],
        # "Бизнес наименование ИС" 256 символов на латинице в CamelCase
        [IS.BUSINESS_NAME_ENGLISH_LENGTH_256, "", "", "", IS.ERROR_SPACES, CreateIS.ERROR_TEXT_BUSINESS_NAME],

        # "Бизнес наименование ИС" 2 символа на латинице в lowercase
        [IS.BUSINESS_NAME_ENGLISH_LENGTH_2.lower(), "", "", "", IS.ERROR_SPACES, CreateIS.ERROR_TEXT_BUSINESS_NAME],
        # "Бизнес наименование ИС" 2 символа на латинице в Uppercase
        [IS.BUSINESS_NAME_ENGLISH_LENGTH_2.upper(), "", "", "", IS.ERROR_SPACES, CreateIS.ERROR_TEXT_BUSINESS_NAME],
        # "Бизнес наименование ИС" 2 символа на латинице в CamelCase
        [IS.BUSINESS_NAME_ENGLISH_LENGTH_2, "", "", "", IS.ERROR_SPACES, CreateIS.ERROR_TEXT_BUSINESS_NAME],

        # "Бизнес наименование ИС" 256 символов на кириллице в lowercase
        [IS.BUSINESS_NAME_RUSSIAN_LENGTH_256.lower(), "", "", "", IS.ERROR_SPACES, CreateIS.ERROR_TEXT_BUSINESS_NAME],
        # "Бизнес наименование ИС" 256 символов на кириллице в Uppercase
        [IS.BUSINESS_NAME_RUSSIAN_LENGTH_256.upper(), "", "", "", IS.ERROR_SPACES, CreateIS.ERROR_TEXT_BUSINESS_NAME],
        # "Бизнес наименование ИС" 256 символов на кириллице в CamelCase
        [IS.BUSINESS_NAME_RUSSIAN_LENGTH_256, "", "", "", IS.ERROR_SPACES, CreateIS.ERROR_TEXT_BUSINESS_NAME],

        # "Бизнес наименование ИС" 2 символа на кириллице в lowercase
        [IS.BUSINESS_NAME_RUSSIAN_LENGTH_2.lower(), "", "", "", IS.ERROR_SPACES, CreateIS.ERROR_TEXT_BUSINESS_NAME],
        # "Бизнес наименование ИС" 2 символа на кириллице в Uppercase
        [IS.BUSINESS_NAME_RUSSIAN_LENGTH_2.upper(), "", "", "", IS.ERROR_SPACES, CreateIS.ERROR_TEXT_BUSINESS_NAME],
        # "Бизнес наименование ИС" 2 символа на кириллице в CamelCase
        [IS.BUSINESS_NAME_RUSSIAN_LENGTH_2, "", "", "", IS.ERROR_SPACES, CreateIS.ERROR_TEXT_BUSINESS_NAME],

        # Только пробелы в поле "Описание"
        ["", "", "", IS.DESCRIPTION_IS_SPACES, IS.ERROR_PREFIX, CreateIS.ERROR_TEXT_DESCRIPTION],
        # Только цифры в поле "Префикс ИС"
        ["", "", IS.PREFIX_IS_NUMBERS, "", IS.ERROR_PREFIX, CreateIS.ERROR_TEXT_PREFIX_IS],

        # "Бизнес наименование ИС" 256 спецсимволов
        [IS.BUSINESS_NAME_SPECIAL_CHARACTERS, "", "", "", IS.ERROR_SPACES, CreateIS.ERROR_TEXT_BUSINESS_NAME],
        # "Бизнес наименование ИС" 2 спецсимвола
        [IS.BUSINESS_NAME_SPECIAL_CHARACTERS[0:2], "", "", "", IS.ERROR_SPACES, CreateIS.ERROR_TEXT_BUSINESS_NAME],

        # "Бизнес наименование ИС" 256 цифр
        [IS.BUSINESS_NAME_NUMBERS, "", "", "", IS.ERROR_SPACES, CreateIS.ERROR_TEXT_BUSINESS_NAME],
        # "Бизнес наименование ИС" 2 цифры
        [IS.BUSINESS_NAME_NUMBERS[0:2], "", "", "", IS.ERROR_SPACES, CreateIS.ERROR_TEXT_BUSINESS_NAME],

        # "Бизнес наименование ИС" с пробелом внутри текста
        [IS.BUSINESS_NAME, "", "", "", IS.ERROR_SPACES, CreateIS.ERROR_TEXT_BUSINESS_NAME],
    ]


class DataCasesDeleteIS:
    """Проверка позитивных и негативных вариантов удаления Информационной системы."""

    # Проверка удаления ИС с невалидным подтверждающим словом
    VALIDATION_FIELD_DELETE_IS_INVALID = [
        [IS.DELETE_CONFIRMATION_SPECIAL_CHARACTERS, False],
        [IS.DELETE_CONFIRMATION_ENGLISH, False],
        [IS.DELETE_CONFIRMATION_INVALID_RUSSIAN, False],
        [IS.DELETE_CONFIRMATION_INVALID_NUMBERS, False],
        [IS.DELETE_CONFIRMATION_SPACES, False],
    ]

    # Проверка отмены удаления ИС
    VALIDATION_CANCEL_DELETE_IS = [
        [IS.DELETE_CONFIRMATION, DeleteInformationSystem.CANCEL_BUTTON, IS.NAME_IS_BACKLINK],
        ["", DeleteInformationSystem.CANCEL_BUTTON, IS.NAME_IS_BACKLINK],
        ["", DeleteInformationSystem.CANCEL_CROSS, IS.NAME_IS_BACKLINK],
    ]


class DataCasesEnvironment:
    """Проверка позитивных и негативных вариантов создания Контура."""

    # Проверка невалидных значений при создании Контура
    # 1-название, 2-описание, 3-чат id, 4-локатор ошибки, 5-текст ошибки для assert
    VALIDATION_INVALID_DATA = [
        # Пустое поле Название
        ["", "", "", CreateEnvironment.ERROR_TEXT_EMPTY_NAME, EnvironmentNotice.ERROR_EMPTY_FIELDS],
        # Пустое поле Описание
        ["", "", "", CreateEnvironment.ERROR_TEXT_EMPTY_DESCRIPTION, EnvironmentNotice.ERROR_EMPTY_FIELDS],
        # Название < 3 символов
        [EnvironmentNotice.NAME_MINIMUM_LENGTH, "", "", CreateEnvironment.ERROR_TEXT_EMPTY_NAME,
         EnvironmentNotice.ERROR_MINIMUM_LENGTH],
        # Название > 20 символов
        [EnvironmentNotice.NAME_MAXIMUM_LENGTH, "", "", CreateEnvironment.ERROR_TEXT_EMPTY_NAME,
         EnvironmentNotice.ERROR_MAXIMUM_LENGTH],
        # Название из 5 пробелов
        [EnvironmentNotice.NAME_SPACES, "", "", CreateEnvironment.ERROR_TEXT_EMPTY_NAME, EnvironmentNotice.ERROR],
        # Название из спецсимволов
        [EnvironmentNotice.NAME_SPECIAL_CHARACTERS, "", "", CreateEnvironment.ERROR_TEXT_EMPTY_NAME,
         EnvironmentNotice.ERROR],
        # Название на кириллице
        [EnvironmentNotice.NAME_RUSSIAN, "", "", CreateEnvironment.ERROR_TEXT_EMPTY_NAME, EnvironmentNotice.ERROR],
        # Описание > 256 символов
        ["", EnvironmentNotice.DESCRIPTION_LENGTH_257, "", CreateEnvironment.ERROR_TEXT_EMPTY_DESCRIPTION,
         EnvironmentNotice.ERROR_MAXIMUM_LENGTH_256],
        # Чат ID 65 символов
        ["", "", EnvironmentNotice.CHAT_ID_LENGTH_65, CreateEnvironment.ERROR_TEXT_EMPTY_CHAT_ID,
         EnvironmentNotice.ERROR_MAXIMUM_LENGTH_64],
        # Чат ID из спецсимволов
        ["", "", EnvironmentNotice.CHAT_ID_SPECIAL_CHARACTERS, CreateEnvironment.ERROR_TEXT_EMPTY_CHAT_ID,
         EnvironmentNotice.ERROR_ONLY_NUMBERS],
        # Чат ID 5 пробелов
        ["", "", EnvironmentNotice.CHAT_ID_SPACES, CreateEnvironment.ERROR_TEXT_EMPTY_CHAT_ID,
         EnvironmentNotice.ERROR_ONLY_NUMBERS],
        # Чат ID на латинице
        ["", "", EnvironmentNotice.CHAT_ID_ENGLISH, CreateEnvironment.ERROR_TEXT_EMPTY_CHAT_ID,
         EnvironmentNotice.ERROR_ONLY_NUMBERS],
        # Чат ID на латинице
        ["", "", EnvironmentNotice.CHAT_ID_RUSSIAN, CreateEnvironment.ERROR_TEXT_EMPTY_CHAT_ID,
         EnvironmentNotice.ERROR_ONLY_NUMBERS],
    ]

    # Проверка валидных значений при создании Контура
    # 1-название, 2-описание, 3-чат id, 4-локатор ошибки, 5-текст ошибки для assert
    VALIDATION_VALID_DATA = [
        # Название 3 символа
        [EnvironmentNotice.NAME_LENGTH_3, "", "", CreateEnvironment.ERROR_TEXT_EMPTY_NAME,
         EnvironmentNotice.ERROR_MINIMUM_LENGTH],
        # Название 20 символов
        [EnvironmentNotice.NAME_LENGTH_20, "", "", CreateEnvironment.ERROR_TEXT_EMPTY_NAME,
         EnvironmentNotice.ERROR_MAXIMUM_LENGTH],
        # Название из 7 цифр
        [EnvironmentNotice.NAME_NUMBERS, "", "", CreateEnvironment.ERROR_TEXT_EMPTY_NAME, EnvironmentNotice.ERROR],
        # Описание 256 символов
        ["", EnvironmentNotice.DESCRIPTION_LENGTH_256, "", CreateEnvironment.ERROR_TEXT_EMPTY_DESCRIPTION,
         EnvironmentNotice.ERROR_MAXIMUM_LENGTH_256],
        # Чат ID 64 символа
        ["", "", EnvironmentNotice.CHAT_ID_MAXIMUM_LENGTH, CreateEnvironment.ERROR_TEXT_EMPTY_CHAT_ID,
         EnvironmentNotice.ERROR_MAXIMUM_LENGTH_64],
        # Описание 1 пробел
        ["", EnvironmentNotice.DESCRIPTION_SPACES, "", CreateEnvironment.ERROR_TEXT_EMPTY_DESCRIPTION,
         EnvironmentNotice.ERROR],

    ]


class DataCasesTableServices:
    """
    Проверки для таблицы и страниц Services
    1-локатор элемента, 2-название столбца таблицы
    """

    # Проверка, что таблица в списке Services содержит все нужные столбцы и их названия корректны.
    CHECK_NAMES_TABLE_SERVICES = [
        [ServicesTable.NAME, ServicesNotice.NAME],
        [ServicesTable.TYPE, ServicesNotice.TYPE],
        [ServicesTable.CLUSTER_IP, ServicesNotice.CLUSTER_IP],
        [ServicesTable.EXTERNAL_IP, ServicesNotice.EXTERNAL_IP],
        [ServicesTable.PORTS, ServicesNotice.PORTS],
        [ServicesTable.TARGET_PORTS, ServicesNotice.TARGET_PORTS],
        [ServicesTable.SELECTORS, ServicesNotice.SELECTORS],
        [ServicesTable.AGE, ServicesNotice.AGE],
    ]

    # Проверка, что таблица на странице Services содержит все нужные столбы и их названия корректны.
    CHECK_NAMES_TABLE_SERVICES_PAGE = [
        [ServicesTable.PODS, ServicesNotice.PODS],
        [ServicesTable.STATUS, ServicesNotice.STATUS],
        [ServicesTable.CONTAINERS_READY, ServicesNotice.CONTAINERS_READY],
        [ServicesTable.RESTARTS, ServicesNotice.RESTARTS],
        [ServicesTable.AGE_PAGE, ServicesNotice.AGE],
        [ServicesTable.TRAFFIC, ServicesNotice.TRAFFIC],
    ]

    # Проверка, что значений в таблице сервиса совпадают с значениями на странице этого сервиса.
    CHECK_PORTS_SERVICES_PAGE = [
        [ServicesTable.PORTS_LIST, ServicesTable.PORTS_PAGE],
        [ServicesTable.TARGET_PORTS_LIST, ServicesTable.TARGET_PORTS_PAGE],
        [ServicesTable.EXTERNAL_IP_LIST, ServicesTable.EXTERNAL_IP_PAGE],
    ]


class DataCasesTableConfigMaps:
    """
    Проверка названий столбцов таблицы Config Maps
    1-локатор элемента, 2-название столбца таблицы Config Maps
    """
    CHECK_NAMES_TABLE_CONFIGMAPS = [
        [ConfigMapsTable.NAME, ConfigMapsNotice.NAME],
        [ConfigMapsTable.AGE, ConfigMapsNotice.AGE],
        [ConfigMapsTable.IMMUTABLE, ConfigMapsNotice.IMMUTABLE],
    ]

    # Проверка полей в таблице Config Maps и на страницы Config Maps.
    CHECK_FIELD_CONFIGMAPS = [
        # Проверка, что поле с замочком в таблице Config Maps так же имеет замочек на странице Config Maps
        [ConfigMapsTable.LOCKED_CONFIG_MAPS, True],
        # Проверка, что поле без замочка в таблице Config Maps так же не имеет замочек на странице Config Maps
        [ConfigMapsTable.NOT_LOCKED_CONFIG_MAPS, False],
    ]


class DataCasesTableSecrets:
    """
    Проверка названий столбцов таблицы Secrets.
    1-локатор элемента, 2-название столбца таблицы Secrets
    """
    CHECK_NAMES_TABLE_SECRETS = [
        [SecretsTable.NAME, SecretsNotice.NAME],
        [SecretsTable.TYPE, SecretsNotice.TYPE],
        [SecretsTable.AGE, SecretsNotice.AGE],
    ]


class DataCasesIngresses:
    """
    Проверка названий столбцов таблицы Ingresses.
    1-локатор элемента, 2-название столбца таблицы Ingresses
    """
    CHECK_NAMES_TABLE_INGRESSES = [
        [Ingresses.INGRESS, IngressesNotice.INGRESS],
        [Ingresses.HOSTNAME, IngressesNotice.HOSTNAME],
        [Ingresses.SERVICES, IngressesNotice.SERVICES],
    ]

    """
    Проверка, что данные Hostname и Service совпадают в списке ингрессов и на странице ингресса.
    1-локатор данных в списке ингрессов, 2-локатор данных на странице ингресса
    """
    CHECK_DATA_INGRESSES = [
        [Ingresses.HOSTNAME_LIST, Ingresses.HOSTNAME_PAGE],
        [Ingresses.SERVICE_LIST, Ingresses.SERVICE_PAGE],
    ]


class DataCasesPVC:
    """
    Проверка названий столбцов таблицы Persistent Volume Claims:
    1-локатор элемента, 2-название столбца таблицы Persistent Volume Claims.
    """
    CHECK_NAMES_TABLE_PVC = [
        [PVC.NAME, PVCNotice.NAME],
        [PVC.CAPACITY, PVCNotice.CAPACITY],
        [PVC.STATUS, PVCNotice.STATUS],
        [PVC.ACCESS_MODES, PVCNotice.ACCESS_MODES],
        [PVC.STORAGE_CLASS, PVCNotice.STORAGE_CLASS],
        [PVC.AGE, PVCNotice.AGE],
    ]

    """
    Проверка данных в таблице PVC:
    1-локатор CAPACITY, 2-локатор ACCESS MODES, 3-локатор STORAGE CLASS 4-данные CAPACITY, 5-данные ACCESS MODES, 
    6-данные STORAGE CLASS.
    """
    CHECK_DATA_PVC_LIST = [
        [PVC.CAPACITY_STATUS_PENDING, PVC.ACCESS_MODES_STATUS_PENDING, PVC.STORAGE_STATUS_PENDING,
         PVCNotice.CAPACITY_STATUS_PENDING, PVCNotice.ACCESS_MODES_STATUS_PENDING, PVCNotice.STORAGE_STATUS_PENDING],
        [PVC.CAPACITY_STATUS_BOUND, PVC.ACCESS_MODES_STATUS_BOUND, PVC.STORAGE_STATUS_BOUND,
         PVCNotice.CAPACITY_STATUS_BOUND, PVCNotice.ACCESS_MODES_STATUS_BOUND, PVCNotice.STORAGE_STATUS_BOUND],
    ]


class DataCasesPods(PodsNotice):
    """
    Проверка названий столбцов таблицы Pods:
    1-локатор элемента, 2-название столбца таблицы Pods.
    """
    CHECK_NAMES_TABLE_PODS = [
        [Pods.NAME, PodsNotice.NAME],
        [Pods.STATUS, PodsNotice.STATUS],
        [Pods.NODE, PodsNotice.NODE],
        [Pods.AGE, PodsNotice.AGE],
    ]