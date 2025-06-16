"""
Задание 1.
✔ Создайте генератор чётных чисел от нуля до 100.
✔ Из последовательности исключите
числа, сумма цифр которых равна 8.
✔ Решение в одну строку.
"""

even_generate = (elem for elem in range(0, 101) if elem % 2 == 0)

print(even_generate)
for elem in even_generate:
    print(elem)
