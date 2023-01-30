# Составить генератор (yield), который преобразует все буквенные символы в
# заглавные.
import random  # Нужен нам для генерации строки
from string import ascii_lowercase as ascii_lower  # Воспользуемся буквами ascii


def my_gen(sybols):  # Объявление функции
    for symb in sybols:
        yield symb.upper()  # Изменения символов


gen_string = ''.join(  # Создадим строку
    [ascii_lower[random.randint(0, len(ascii_lower) - 1)]
     for x in range(random.randint(5, 25))
     ])
print(f"Строка до использования генератора: {gen_string}")
g = my_gen(gen_string)
print(f"Строка после использования генератора: " + ''.join(g))  # Вывод с помощью join, что бы не использовать next()
