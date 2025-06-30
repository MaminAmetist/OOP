"""
Задание 1.
Создайте декоратор с параметром.
Параметр - целое число, количество запусков декорируемой
функции.
"""
from time import sleep


def decor_param(param):
    def decor(func):
        def wrapper(*args, **kwargs):
            for _ in range(param):
                res = func(*args, **kwargs)
            return res

        return wrapper

    return decor


@decor_param(5)
def sleeping():
    sleep(2)
    print('Это результат вызова функции sleeping')


sleeping()
