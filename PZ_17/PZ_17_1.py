# Создайте класс "Человек" с атрибутами "имя", "возраст" и "пол". Напишите метод,
# который выводит информацию о человеке в формате "Имя: имя, Возраст: возраст,
# Пол: пол".

class Human:  # Создание класса Человек
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def __str__(self):   # Переопределение магического метода при обращении к экземпляру через print
        return f"Имя: {self.name}, Возраст: {self.age}, Пол: {self.gender}"

print(Human("Алина", 20, 'женский'))
