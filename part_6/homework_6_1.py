"""
Задание 1.

Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля
в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
"""


class Zero(Exception):
    def __init__(self, numerator, divider):
        self.numerator = numerator
        self.divider = divider

    def return_division(self):
        if self.divider != 0:
            return self.numerator / self.divider
        else:
            return 'На ноль делить нельзя'


a, b = 1, 0
try:
    print(Zero(a, b).return_division())
except Zero as exc:
    print(exc)
