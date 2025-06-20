"""
Задание 2.

Последовательностью Фибоначчи называется
последовательность чисел a0
, a1
, ..., an
, ..., где
a0 = 0, a1 = 1,
ak = ak-1 + ak-2 (k > 1).
Требуется найти N-е число Фибоначчи
Input: 7
Output: 21
"""

# 0, 1, 1, 2, 3, 5, 8, 13, 21
a = 8
fibo_p, fibo_n = 0, 1
for _ in range(0, a - 1):
    fibo_p, fibo_n = fibo_n, fibo_p + fibo_n
print(f'{a}-e число = {fibo_n}')


def fibo_rec(a):
    if a < 2:
        return a
    return fibo_rec(a - 1) + fibo_rec(a - 2)


print(f'{a}-e число = {fibo_rec(a)}')
