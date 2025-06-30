"""
Задание 1

Напишите декоратор для замеров времени выполнения любой функции
Для реализации замеров воспользуйтесь модулем timeit

Реализуйте декоратор в виде функции и класса
"""

from timeit import timeit


def decor(func):
    def wrapper(*args, **kwargs):
        sum_time = timeit(lambda: func(*args, **kwargs), number=100000000)
        result = func(*args, **kwargs)
        return result, sum_time
    return wrapper


@decor
def summator(num_1, num_2):
    return num_1 + num_2


print(summator(2, 3))
