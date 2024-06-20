from dataclasses import dataclass


@dataclass
class Auth:
    login: str = "***"
    password: str = "***"


class UserGroups:
    """Проверка доступности кнопки Создать ИС для разных прав пользователей."""
    GROUP_USERS = [
        ["***", "***", False],
        ["***", "***", False],
        ["***", "***", False],
        ["***", "***", True],
    ]
