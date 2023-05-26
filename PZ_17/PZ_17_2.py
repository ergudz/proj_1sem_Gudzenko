# Создание базового класса "Животное" и его наследование для создания классов
# "Собака" и "Кошка". В классе "Животное" будут общие методы, такие как "дышать"
# и "питаться", а классы-наследники будут иметь свои уникальные методы и свойства,
# такие как "гавкать" и "мурлыкать".

class Animal:  # Создание класса животное
    def __init__(self, name):
        self.name = name

    def breathe(self):
        return  "дышит"

    def eat(self):
        return "кушает"

class Dog(Animal):  # Создание класса собака
    def bark(self):
        return "гавкает"

class Cat(Animal):  # Создание класса кошка
    def purr(self):
        return "мурлыкает"

dog = Dog('Пудель')
cat = Cat('Девон-рекс')
print(dog.breathe())
print(cat.breathe())
print(dog.eat())
print(cat.eat())
print(dog.bark())
print(cat.purr())
