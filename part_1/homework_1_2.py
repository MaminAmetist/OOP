"""
# Задание 2
# ✔ Создайте функцию генератор чисел Фибоначчи (см. Википедию).
# """


def generate_fibonacci(n):
    a, b = 0, 1
    for _ in range(1, n + 1):
        yield a
        a, b = b, a + b


gnrtr = generate_fibonacci(10)
print(gnrtr)
for elem in gnrtr:
    print(elem)
