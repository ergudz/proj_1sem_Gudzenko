# Дан целочисленный список размера 10.
# Вывести все содержащиеся в данном списке четные числа в порядке убывания их индексов
# А также их количество K.
def list_append(n: int, list_gen: list) -> list:  # Функция генерации списка
    for _ in range(n):
        list_gen.append(input(f"Введите {(_ + 1)}-е число: "))
        while type(list_gen[_]) != int:  # Обработчик исключений элементов списка
            try:
                list_gen[_] = int(list_gen[_])
            except ValueError:
                list_gen[_] = input(f"Введите целое число {_ + 1} без лишних символов: ")
    return list_gen


def list_changer(old_list):  # Функция, сортирующая список
    new_list = []
    for i in reversed(old_list):
        if i % 2 == 0:
            new_list.append(i)
    return new_list


N = 10
lst = list_append(N, [])
print(f"Вот содержимое вашего списка: {lst}")
even_list = list_changer(lst)

print(f"Вот все четные числа из вашего списка: {even_list}")
print(f'Их количество = {len(even_list)}')
