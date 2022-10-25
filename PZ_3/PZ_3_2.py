a, b = input('Введите число 1: '), input('Введите число 2: ')  #Ввод чисел

while type(a) != int:                                          #Обработка исключений
    try:
        a = int(a)
    except ValueError:
        print('Неправильный ввод числа')
        a = input('Введите число 1: ')

while type(b) != float:                                        #Обработка исключений
    try:
        b = float(b)
    except ValueError:
        print('Неправильный ввод числа')
        b = input('Введите число 2: ')

if a == 1:
    print(b / 10)
elif a == 2:
    print(b * 1000)
elif a == 3:
    print(b)
elif a == 4:
    print(b / 1000)
elif a == 5:
    print(b / 100)
else:
    print('Неправильный ввод числа')
