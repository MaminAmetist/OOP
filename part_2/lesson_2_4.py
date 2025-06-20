"""
Задание
4.

Выведите
строку
по
частям

Hello
Hell
Hel
He
H
"""

data = "Hello"


def func_1(data):
    while len(data) != 0:
        print(data)
        data = data[:-1]


func_1(data)


def split_rec(text):
    print(text)
    if len(text) == 1:
        return text
    return split_rec(text[:-1])


split_rec(data)
