# В матрице элементы столбца N (N задать с клавиатуры) увеличить в два раза.
N = int(input("Введите N: "))-1  # Ввод числа N
count = range(5)  # Размер матрицы


def tri(num, index):  # Функия проверяющая столбец
    if index == N:
        num *= 2
    return num


matrix = [  # Генератор списков для генерации матрицы размера "count"
    [tri(n, ind) for ind, n in enumerate(count)] for x in count
    ]
print(matrix)
