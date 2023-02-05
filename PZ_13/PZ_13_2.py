# В матрице элементы последней строки заменить на 0.
import random  # Импорт рандома
size_matrix = random.randint(2, 5)  # Размер матрицы
rang_matrix = range(size_matrix)
matrix = [
    [n for n in rang_matrix]  # Создать вложеный список если этот список не будет последним
    if x+1 != size_matrix else [0 for x in rang_matrix]
    for x in rang_matrix
    ]
print(matrix)
