"""
Задание 1.
Напишите класс для хранения информации о человеке:
ФИО, возраст и т.п. на ваш выбор.
У класса должны быть методы birthday для увеличения
возраста на год, full_name для вывода полного ФИО и т.п. на
ваш выбор.
Убедитесь, что свойство возраст недоступно для прямого
изменения, но есть возможность получить текущий возраст.
"""


class Person:
    def __init__(self, name, last_name, age, address):
        self.name = name
        self.last_name = last_name
        self.__age = age
        self.address = address

    def __str__(self):
        return f'Я {self.name} из города {self.address} и мне {self.__age} лет.'

    def birthday(self):
        self.__age += 1
        return self.__age

    def full_name(self):
        return f'Полное имя: {self.name} {self.last_name}'

    def move(self, new_address):
        self.address = new_address
        return self.address


person_first = Person('Alex', 'Ivanov', 25, 'Omsk')
print(person_first)
person_first.birthday()
print(person_first)
print(person_first.full_name())
person_first.move('Tomsk')
print(person_first)
