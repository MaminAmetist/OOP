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
    __light_dict = {'red': 7, 'yellow': 2, 'green': 4}

    @staticmethod
    def running():
        for key, value in TrafficLight.__light_dict.items():
            __color = key
            print(__color)
            sleep(value)


traffic_light = TrafficLight()
print(traffic_light.running())
