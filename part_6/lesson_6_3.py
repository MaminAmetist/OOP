"""
Задание 93.
📌 Создайте класс с базовым исключением и дочерние классы-
исключения:
○ ошибка уровня,
○ ошибка доступа.
"""


class MyException(Exception):
    """Базовое исключение"""
    pass


class LevelError(MyException):
    """Исключение, связанное с ошибками уровня"""

    def __init__(self, message):
        super().__init__('ошибка уровня')


class AccessError(MyException):
    """Исключение, связанное с ошибками доступа"""

    def __init__(self, message):
        super().__init__('ошибка доступа')


try:
    raise LevelError('Что-то пошло не так с уровнем')
except LevelError as exc:
    print(exc)

try:
    raise AccessError('Что-то пошло не так с доступом')
except AccessError as exc:
    print(exc)
