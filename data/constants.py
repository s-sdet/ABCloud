"""Константы, в т.ч. тексты ошибок и уведомлений."""
from dataclasses import dataclass

class AuthNotice:
    """Страница авторизации https://paas-dev.dev-int.akbars.ru/"""
    LOGO_TEXT = "ABCloud"
    ERROR_AUTHORIZATION_TEXT = "Invalid login and password."
    AUTHORIZATION = "Sign in to your account"
    PLACEHOLDER_LOGIN = "login"
    PLACEHOLDER_PASSWORD = "password"
    HEADER_TEXT = "Log in to Your Account"
    INVALID_LOGIN = "qwerty"
    INVALID_PASSWORD = "qwerty"
    EMPTY_LOGIN = ""
    EMPTY_PASSWORD = ""


class InfoSystemNotice:
    """
    Константы для раздела Информационные системы
    https://paas-dev.dev-int.akbars.ru/
    """
    BREADCRUMBS_BACKLINK = "Создание информационной системы"  # Для проверки перехода в форму создания ИС
    BREADCRUMBS = "Информационные системы"  # Для проверки перехода в список ИС
    LABEL_BUSINESS_NAME = "Бизнес наименование информационной системы"  # Текст перед тултипом ИС
    MODAL_WINDOW = "Удаление информационной системы"  # Заголовок модального окна удаления ИС

    # Константы для поля "Бизнес наименование ИС"
    BUSINESS_NAME = "Тестовое бизнес наименование ИС"  # Валидное Бизнес наименование ИС
    BUSINESS_NAME_MAXIMUM_LENGTH = "Test бизнес наименование ИС 1 %, Test бизнес наименование ИС 1 %, Test бизнес " \
                                   "наименование ИС 1 %, Test бизнес наименование ИС 1 %, Test бизнес наименование " \
                                   "ИС 1 %, Test бизнес наименование ИС 1 %, Test бизнес наименование ИС 1 %, Test " \
                                   "бизнес наименование И"  # Для проверки на максимальную длинну = 257 символов
    BUSINESS_NAME_SPACES = "  "  # Для проверки на пробелы
    BUSINESS_NAME_RUSSIAN_LENGTH_256 = "Тестовое бизнес наименование информационной системы Тестовое бизнес " \
                                       "наименование информационной системы Тестовое бизнес наименование " \
                                       "информационной системы Тестовое бизнес наименование информационной системы " \
                                       "Тестовое бизнес наименование информационной сист"  # Кириллица 256 символов
    BUSINESS_NAME_RUSSIAN_LENGTH_2 = "Ис"  # Кириллица 2 символа
    BUSINESS_NAME_RUSSIAN_LENGTH_1 = "и"  # Кириллица 1 символ
    BUSINESS_NAME_ENGLISH_LENGTH_256 = "Test business name IS Test business name IS Test business name IS Test " \
                                       "business name IS Test business name IS Test business name IS Test business " \
                                       "name IS Test business name IS Test business name IS Test business name IS " \
                                       "Test business name IS Test businesss"  # Латиница 256 символов
    BUSINESS_NAME_ENGLISH_LENGTH_2 = "Is"  # Латиница 2 символа
    BUSINESS_NAME_ENGLISH_LENGTH_1 = "i"  # Латиница 1 символ
    BUSINESS_NAME_SPECIAL_CHARACTERS = "@$#%()*&^+-~@$#%()*&^+-~@$#%()*&^+-~@$#%()*&^+-~@$#%()*&^+-~@$#%()*&^+-~@" \
                                       "$#%()*&^+-~@$#%()*&^+-~@$#%()*&^+-~@$#%()*&^+-~@$#%()*&^+-~@$#%()*&^+-~@$" \
                                       "#%()*&^+-~@$#%()*&^+-~@$#%()*&^+-~@$#%()*&^+-~@$#%()*&^+-~@$#%()*&^+-~@$#" \
                                       "%()*&^+-~@$#%()*&^+-~@$#%()*&^+-~@$#%"  # 256 спецсимволов
    BUSINESS_NAME_NUMBERS = "12345678912345678912345678912345678912345678912345678912345678912345678912345678912" \
                            "34567891234567891234567891234567891234567891234567891234567891234567891234567891234" \
                            "56789123456789123456789123456789123456789123456789123456789123456789123456789123456" \
                            "7891234"  # 256 цифр
    BUSINESS_NAME_TEXT_WITH_SPACES = " Бизнес наименование "  # Пробелы в начале и в конце текста

    # Константы для поля "Наименование ИС"
    NAME = "bbivn"
    NAME_IS_BACKLINK = "is4"  # Название ИС в ссылке возврата в список всех ИС
    NAME_IS_UPPERCASE = "TEST-NAME"  # Для проверки на латинские символы Uppercase
    NAME_IS_CAMELCASE = "Test-Name"  # Для проверки на латинские символы CamelCase
    NAME_IS_RUSSIAN = "тестовое название"   # Для проверки на кириллические символы
    NAME_IS_MINIMUM_LENGTH = "q"  # Для проверки на минимальную длинну <2 символов
    NAME_IS_MAXIMUM_LENGTH = "testtesttesttesttesttesttettesttestteqwer"  # Для проверки на максимальную длинну
    NAME_IS_SPACES = "     "  # Для проверки на пробелы

    # Константы для поля "Префикс ИС"
    PREFIX = "bbivn"  # Валидный Префикс ИС
    PREFIX_IS_UPPERCASE = "TNMS"  # Для проверки на латинские символы Uppercase
    PREFIX_IS_CAMELCASE = "Tnms"  # Для проверки на латинские символы CamelCase
    PREFIX_IS_RUSSIAN_LENGTH_1 = "П"  # Для проверки на минимальную длинну <2 символов
    PREFIX_IS_RUSSIAN_LENGTH_5 = "ТНМСВ"  # Для проверки на кириллические символы Uppercase
    PREFIX_IS_RUSSIAN_LENGTH_6 = "ТНМСВА"  # Для проверки на кириллические символы Uppercase
    PREFIX_IS_MINIMUM_LENGTH = "q"  # Для проверки на минимальную длинну <2 символов
    PREFIX_IS_MAXIMUM_LENGTH = "tnmstnms"  # Для проверки на максимальную длинну >5 символов
    PREFIX_IS_SPACES = "     "  # Для проверки на пробелы
    PREFIX_IS_NUMBERS = "12345"  # Для проверки на цифры

    # Константы для поля "Описание"
    DESCRIPTION = "Тестовая ИС, можно удалять"  # Валидное описание ИС
    DESCRIPTION_MAXIMUM_LENGTH = "Тестовая ИС, можно удалять Тестовая ИС, можно удалять Тестовая ИС, можно удалять " \
                                 "Тестовая ИС, можно удалять Тестовая ИС, можно удалять Тестовая ИС, можно удалять " \
                                 "Тестовая ИС, можно удалять Тестовая ИС, можно удалять Тестовая ИС, можно удалять " \
                                 "Тестовая ИС, м"  # Для проверки на максимальную длинну 256 символов
    DESCRIPTION_IS_SPACES = "     "  # Для проверки на пробелы

    # Константы для проверки удаления ИС
    DELETE_CONFIRMATION = "is4"  # Для проверки подтверждения удаления ИС
    DELETE_CONFIRMATION_SPECIAL_CHARACTERS = "<@$%&*"  # Для проверки подтверждения удаления ИС со спец. символами
    DELETE_CONFIRMATION_ENGLISH = "qwerty"  # Для проверки подтверждения удаления ИС из латинских символов
    DELETE_CONFIRMATION_INVALID_RUSSIAN = "ОбЛаКо"  # Для проверки подтверждения удаления ИС с невалидным словом
    DELETE_CONFIRMATION_INVALID_NUMBERS = "123456"  # Для проверки подтверждения удаления ИС с цифрами
    DELETE_CONFIRMATION_SPACES = "     "  # Для проверки подтверждения удаления ИС с пробелами

    # Уведомления об успешном создании и удалении Информационной системы
    SUCCESS_CREATE_IS = "Информационная система создана"
    SUCCESS_DELETE_IS = "Информационная система удалена"

    # Предупреждения об ошибках заполнения полей:
    ERROR_PREFIX = "Поле должно содержать только символы латиницы в нижнем регистре и цифры"
    ERROR_TRANSLITERATION = "Поле должно содержать символы латиницы в нижнем регистре, допустимы цифры и дефисы"
    ERROR_MAXIMUM_LENGTH_256 = "Поле должно содержать до 256 символов"
    # ERROR_MINIMUM_LENGTH_5 = "Поле должно содержать минимум 5 символов"
    ERROR_MAXIMUM_LENGTH_40 = "Поле должно содержать до 40 символов"
    ERROR_MINIMUM_LENGTH_2 = "Поле должно содержать минимум 2 символа"
    ERROR_MAXIMUM_LENGTH_5 = "Поле должно содержать до 5 символов"
    ERROR_EMPTY_FIELDS = "Поле обязательно для ввода"
    ERROR_SPACES = "Значение не может начинаться или заканчиваться пробелом"

    # Уведомления об успешном создании и удалении ИС
    SUCCESS_CREATE = "Информационная система создана"
    SUCCESS_DELETE = "Информационная система удалена"


class EnvironmentNotice:
    """
    Константы для раздела Environment
    https://paas-dev.dev-int.akbars.ru/info_system/finmarket
    """
    BACKLINK = "Создание контура"  # Backlink в форме создания Контура
    NAME_IS_BACKLINK = "finmarket"  # Название ИС в ссылке возврата в список всех ИС
    DELETION_CONFIRMATION_ENV = "Удаление контура"  # Текст в форме подтверждения удаления контура. Для assert

    # Константы для поля "Название"
    NAME = "autotest"  # Валидное название Контура
    NAME_MINIMUM_LENGTH = "qq"  # Для проверки на минимальную длинну <3 символов
    NAME_LENGTH_3 = "qwe"  # Для проверки на минимальную длинну <3 символов
    NAME_LENGTH_24 = "qwertyqwertyqwertyqwerty"  # Для проверки на максимальную длинну >25 символов
    NAME_LENGTH_20 = "qwertyqwertyqwertyqw"  # Для проверки на длинну =20 символов
    NAME_MAXIMUM_LENGTH = "qwertyqwertyqwertyqwe"  # Для проверки на длинну 21 символ
    NAME_SPACES = "     "  # Для проверки на пробелы в названии
    NAME_NUMBERS = "1234567"  # Для проверки на цифры
    NAME_SPECIAL_CHARACTERS = "№;%?(/)"  # Для проверки на спецсимволы
    NAME_RUSSIAN = "Контур"  # Для проверки на кириллические символы

    # Константы для поля "Описание контура"
    DESCRIPTION = "Тестовый контур, можно удалять."  # Валидное описание Контурая
    DESCRIPTION_LENGTH_256 = "Тестовый контур, можно удалять Тестовый контур, можно удалять Тестовый контур, можно " \
                             "удалять Тестовый контур, можно удалять Тестовый контур, можно удалять Тестовый контур, " \
                             "можно удалять Тестовый контур, можно удалять Тестовый контур, можно удалять " \
                             "Тестовый"  # Невалидное описание Контура
    DESCRIPTION_LENGTH_257 = "Тестовый контур, можно удалять Тестовый контур, можно удалять Тестовый контур, можно " \
                             "удалять Тестовый контур, можно удалять Тестовый контур, можно удалять Тестовый контур, " \
                             "можно удалять Тестовый контур, можно удалять Тестовый контур, можно удалять " \
                             "Тестовый."  # Невалидное описание Контура
    DESCRIPTION_SPACES = " "  # Для проверки на пробел

    # Константы для поля "Чат ID"
    CHAT_ID = "1234567"  # Валидный номер Чат ID
    CHAT_ID_MAXIMUM_LENGTH = "1234567123456712345671234567123456712345671234567123456712345671"  # Чат ID 64 цифры
    CHAT_ID_LENGTH_65 = "12345671234567123456712345671234567123456712345671234567123456712"  # Чат ID 65 цифр
    CHAT_ID_SPECIAL_CHARACTERS = "№;%?(/)"  # Для проверки на спецсимволы
    CHAT_ID_SPACES = "     "  # Для проверки на пробелы
    CHAT_ID_ENGLISH = "cahtid"  # Для проверки на латинские символы
    CHAT_ID_RUSSIAN = "облако"  # Для проверки на кириллические символы

    # Предупреждения об ошибках заполнения полей:
    ERROR_EMPTY_FIELDS = "Поле обязательно для ввода"
    ERROR = "Значение введено с ошибками"
    ERROR_ONLY_NUMBERS = "Поле может содержать только цифры"
    ERROR_MINIMUM_LENGTH = "Поле должно содержать минимум 3 символа"
    ERROR_MAXIMUM_LENGTH = "Поле должно содержать до 20 символов"
    ERROR_MAXIMUM_LENGTH_256 = "Поле должно содержать до 256 символов"
    ERROR_MAXIMUM_LENGTH_64 = "Поле должно содержать до 64 символов"

    # Уведомления об успешном создании и удалении конутра
    SUCCESS_CREATE = "Контур создан"
    SUCCESS_DELETE = "удален"


class BreadcrumbsNotice:
    """
    Константы для хлебных крошек
    """
    BREADCRUMBS = "is4"  # Название в хлебных крошках, для проверки перехода в таблицу Контуров


class PodsNotice:
    """
    Константы для раздела Pods
    https://paas-stage.dev-int.akbars.ru/info_system/finmarket/env/finmarket-dev/pods
    """
    BREADCRUMBS = "Pods"  # Название в хлебных крошках, для проверки перехода в таблицу Pods
    POD = "nginx"
    PODS_NODE = "t-paas1-wrk01"
    TOOLTIP = "UTC"
    URL = "{}informationsystems/is4/env/is4-autotest/pods"

    # Названия столбцов таблицы Pods
    NAME = "NAME"
    STATUS = "STATUS"
    NODE = "NODE"
    AGE = "AGE"


class DeploymentsNotice:
    """
    Константы для раздела Deployments
    https://paas-stage.dev-int.akbars.ru/info_system/finmarket/env/finmarket-dev/deployments
    """
    BREADCRUMBS = "Deployments"  # Название в хлебных крошках, для проверки перехода в таблицу Deployments


class ServicesNotice:
    """
    Константы для раздела Сервисов
    https://paas-stage.dev-int.akbars.ru/info_system/finmarket/env/finmarket-dev/services
    """
    BREADCRUMBS = "Services"  # Название в хлебных крошках, для проверки перехода в таблицу Сервисы

    # Названия столбцов таблицы Services
    NAME = "NAME"
    TYPE = "TYPE"
    CLUSTER_IP = "CLUSTER IP"
    EXTERNAL_IP = "EXTERNAL IP"
    PORTS = "PORTS"
    TARGET_PORTS = "TARGET PORTS"
    SELECTORS = "SELECTORS"
    AGE = "AGE"
    PODS = "PODS"
    STATUS = "STATUS"
    CONTAINERS_READY = "CONTAINERS READY"
    RESTARTS = "RESTARTS"
    TRAFFIC = "TRAFFIC"


class ConfigMapsNotice:
    """
    Константы для раздела ConfigMaps
    https://paas-stage.dev-int.akbars.ru/info_system/finmarket/env/finmarket-dev/config_maps
    """
    BREADCRUMBS = "Config Maps"  # Название в хлебных крошках, для проверки перехода в таблицу Config Maps

    # Названия столбцов таблицы ConfigMaps
    NAME = "NAME"
    AGE = "AGE"
    IMMUTABLE = "IMMUTABLE"


class SecretsNotice:
    """
    Константы для раздела Secrets
    https://paas-stage.dev-int.akbars.ru/info_system/finmarket/env/finmarket-dev/secrets
    """
    BREADCRUMBS = "Secrets"  # Название в хлебных крошках, для проверки перехода в таблицу Secrets
    REVEAL_SECRET = "Reveal secret"  # Показать секрет
    HIDE_SECRET = "Hide secret"  # Скрыть секрет
    SUCCESS_SNACKBAR = "Содержимое скопировано"  # Текст уведомления, что секрет успешно скопирован

    # Названия столбцов таблицы Secrets
    NAME = "NAME"
    TYPE = "TYPE"
    AGE = "AGE"


class IngressesNotice:
    """
    Константы для раздела Ingresses
    https://paas-dev.dev-int.akbars.ru/info_system/finmarket/env/finmarket-dev/ingresses
    """
    BREADCRUMBS = "Ingresses"  # Название в хлебных крошках, для проверки перехода в таблицу Ingresses

    # Названия столбцов таблицы Ingresses
    INGRESS = "INGRESS"
    HOSTNAME = "HOSTNAME"
    SERVICES = "SERVICES"


class PVCNotice:
    """
    Константы для раздела Persistent Volume Claims
    https://paas-dev.dev-int.akbars.ru/info_system/finmarket/env/finmarket-dev/persistentvolumeclaims
    """
    BREADCRUMBS = "Persistent Volume Claims"  # Название в хлебных крошках, для проверки перехода в таблицу PVC
    PVC = "pvc-local"
    TOOLTIP = "UTC"
    URL = "{}informationsystems/is4/env/is4-autotest/persistentvolumeclaims"

    # Названия столбцов таблицы PVC
    NAME = "NAME"
    CAPACITY = "CAPACITY"
    STATUS = "STATUS"
    ACCESS_MODES = "ACCESS MODES"
    STORAGE_CLASS = "STORAGE CLASS"
    AGE = "AGE"

    # Данные в таблице PVC
    CAPACITY_STATUS_PENDING = "–"
    ACCESS_MODES_STATUS_PENDING = "–"
    STORAGE_STATUS_PENDING = "local-storage"
    CAPACITY_STATUS_BOUND = "10Mi"
    ACCESS_MODES_STATUS_BOUND = "ReadWriteOnce"
    STORAGE_STATUS_BOUND = "longhorn"
    STORAGE_EMPTY_DATA = "–"