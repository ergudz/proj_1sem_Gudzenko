# Дан список размера N.
# Заменить каждый элемент списка на среднее арифметическое этого элемента и его соседей.
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
print(lst)

for index in range(len(lst)):  # Цикл, который будет складывать все элементы
    if index == 0 and index != (len(lst) - 1):
        lst[index] = round(sum(lst[index:index + 2]) / 2, 5)

    if len(lst) - 1 > index > 0:
        lst[index] = round(sum(lst[index - 1:index + 2]) / 3, 5)

    if index == (len(lst) - 1) and index != 0:
        lst[index] = round(sum(lst[index - 1:index + 1]) / 2, 5)

print(lst)
