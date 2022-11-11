# Дан список размера N.
# Найти количество участков, на которых его элементы монотонно возрастают.
def list_append(n: int, list_gen: list) -> list:  # Функция генерации списка
    for _ in range(n):
        list_gen.append(input(f"Введите {(_ + 1)}-е число: "))
        while type(list_gen[_]) != int:  # Обработчик исключений элементов списка
            try:
                list_gen[_] = int(list_gen[_])
            except ValueError:
                list_gen[_] = input(f"Введите целое число {_ + 1} без лишних символов: ")
    return list_gen


N = input("Введите длину списка: ")

while type(N) != int:  # Обработчик исключений
    try:
        N = int(N)
    except ValueError:
        N = input("Введите целое число: ")

lst = list_append(N, [])

k = 0
flag = True
for i in range(len(lst)):  # Цикл пробегает по списку
    if lst[i-1] < lst[i]:  # Если 1 число меньше 2, то эти числа возрастают
        if flag:  # Если пара  чисел i-2 и i-1 возрастала, то условие не выполнится
            k += 1
            flag = False  # Если числа возрастают монотонно, то следущая пара не будет считаться участком
    else:
        flag = True

print(f"Количество участков на которых числа монотонно возрастают - {k}")
