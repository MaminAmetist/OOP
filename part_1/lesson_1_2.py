"""
Задание 2.
✔ Напишите программу, которая выводит
на экран числа от 1 до 100.
✔ При этом вместо чисел, кратных трем,
программа должна выводить слово «Fizz»
✔ Вместо чисел, кратных пяти — слово «Buzz».
✔ Если число кратно и 3, и 5, то программа
должна выводить слово «FizzBuzz».
✔ *Превратите решение в генераторное выражение.
"""

fizz_buzz_generate = ('FizzBuzz' if elem % 3 == 0 and elem % 5 == 0
                    else 'Fizz' if elem % 3 == 0
                    else 'Buzz' if elem % 5 == 0
                    else elem for elem in range(1, 101))
print(fizz_buzz_generate)
for elem in fizz_buzz_generate:
    print(elem)
