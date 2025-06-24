"""
Задание 1.

Создать класс TrafficLight (светофор)
и определить у него один приватный атрибут color (цвет)
и публичный метод running (запуск).

В рамках метода running реализовать переключение светофора в режимы:
красный, желтый, зеленый. Продолжительность первого состояния (красный)
составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый) —
на ваше усмотрение.

Переключение между режимами должно осуществляться только
в указанном порядке (красный, желтый, зеленый).

Проверить работу примера, создав экземпляр и вызвав описанный метод.
"""
from time import sleep


class TrafficLight:
    def __init__(self, color=None):
        self.__color = color

    def running(self):
        light_dict = {'red': 7, 'yellow': 2, 'green': 4}
        for key, value in light_dict.items():
            self.__color = key
            print(self.__color)
            sleep(value)


traffic_light = TrafficLight()
print(traffic_light.running())
