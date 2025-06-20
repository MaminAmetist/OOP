"""
Задание 3.


Дано натуральное число N и
последовательность из N элементов.
Требуется вывести эту последовательность в
обратном порядке.
Примечание. В программе запрещается
объявлять массивы и использовать циклы
(даже для ввода и вывода).
Input: 2 -> 3 4
Output: 4 3
"""

orig = '3 4'


def func_2(str_obj):
    res = ''
    for el in reversed(str_obj):
        res += el
    return res


print(func_2(orig))


def revers_rec(something):
    if len(something) == 1:
        return something
    return something[-1] + revers_rec(something[:-1])


print(revers_rec(orig))
