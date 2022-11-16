# Дано целое число N (>0) и символ C. Вывести строку длины N, которая состоит из символов C.
N = input('Введите число: ')
while type(N) != int:  # Обработчик исключений
    try:
        N = int(N)
        if N <= 0:
            raise AttributeError
    except ValueError:
        N = input('Введите число N без лишних символов: ')
    except AttributeError:
        N = input('Введите число N > 0 ещё раз без лишних символов: ')

print(N * "C")
