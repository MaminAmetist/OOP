"""
Задание 1
📌 Создайте прямоугольник с методами расчета периметра и площади
📌 Добавьте сравнение прямоугольников по площади
📌 Должны работать все шесть операций сравнения
"""


class Rectangle:
    def __init__(self, weight, height):
        self.weight = weight
        self.height = height

    def __str__(self):
        return f'Это прямоугольник шириной {self.weight} и высотой {self.height}'

    def get_perimetr(self):
        return (self.weight + self.height) * 2

    def get_area(self):
        return self.height * self.weight

    def __eq__(self, other):
        return self.height * self.weight == other.get_area()

    def __gt__(self, other):
        return self.height * self.weight > other.get_area()

    def __lt__(self, other):
        return self.height * self.weight < other.get_area()

    def __ge__(self, other):
        return self.height * self.weight >= other.get_area()

    def __le__(self, other):
        return self.height * self.weight <= other.get_area()


one = Rectangle(5, 10)
two = Rectangle(5, 5)

print(one, two)
print(one.get_perimetr())
print(two.get_area())
# print(one > two)
# print(one >= two)
# print(one < two)
# print(one <= two)
# print(one == two)
print(one != two)
