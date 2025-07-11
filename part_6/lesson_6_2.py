"""
Задание 92.
📌 Создайте функцию аналог get для словаря.
📌 Помимо самого словаря функция принимает ключ и
значение по умолчанию.
📌 При обращении к несуществующему ключу функция должна
возвращать дефолтное значение.
📌 Реализуйте работу через обработку исключений.
"""


def get_value(kwargs, key, value=None):
    try:
        return kwargs[key]
    except KeyError:
        return value


my_dict = {True: 'да', 1: 'нет', 1.0: 'может быть'}
print(get_value(my_dict, 1))
print(get_value(my_dict, 0))
