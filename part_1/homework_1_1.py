"""
# Задание 1
# ✔ Создайте функцию генератор четных чисел от 0 до n.
# """


def generate_even(n):
    for elem in range(0, n + 1):
        if elem % 2 == 0:
            yield elem


gnrtr = generate_even(10)
print(gnrtr)
for elem in gnrtr:
    print(elem)
