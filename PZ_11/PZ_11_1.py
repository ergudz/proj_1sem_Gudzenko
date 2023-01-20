# Средствами языка Python сформировать текстовый файл (.txt), содержащий
# последовательность из целых положительных и отрицательных чисел. Сформировать
# новый текстовый файл (.txt) следующего вида, предварительно выполнив требуемую
# обработку элементов:
# Исходные данные:
# Количество элементов:
# Индекс последнего минимального элемента:
# Сумма элементов больших 10 во второй половине:
import random


def sequence(n):  # функция генерации последовательности
    list_sequence = []
    while len(list_sequence) != n:
        list_sequence.append(str(random.randint(-50, 50)))
    list_sequence = ' '.join(list_sequence)
    return list_sequence

f1 = open('file1_1.txt', 'w', encoding='UTF-8')

file_elements = sequence(random.randint(5, 10))  # Генерируем последовательность
f1.write(file_elements)

f1.close()

f2 = open('file2_1.txt', 'w', encoding='UTF-8')  # Открываем файл

index_of_min_elements = file_elements.split().index(str(min([int(x) for x in file_elements.split(" ")])))
if len(file_elements) % 2 == 0:  # Если последовательность имеет четное количество элементов
    sum_of_elements = sum([int(x) for x in file_elements.split()[(int(len(file_elements.split())/2)):]
                       if int(x) > 10])  # считаем сумму элементов из последовательности
else:
    sum_of_elements = sum([int(x) for x in file_elements.split()[(int(len(file_elements.split()) / 2)+1):]
                           if int(x) > 10])  # # считаем сумму элементов из последовательности

print()
f2.write(f'Исходные данные: {file_elements}\n'  # Записываем обработанные данные
         f'Количество элементов: {len(file_elements.split())}\n'
         f'Индекс последнего минимального элемента: {index_of_min_elements}\n'
         f'Сумма элементов больших 10 во второй половине: {sum_of_elements}')

f2.close()  # закрываем файл
