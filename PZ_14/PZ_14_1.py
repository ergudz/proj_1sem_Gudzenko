import re  # импорт модуля с регулярными выражениями

with open("Dostoevsky.txt", encoding="utf-8") as file:  # Открываю текствовый файл
    data = len(set(re.findall(r'(?<=«)[\w\s]+', file.read())))  # Считаю кол-во произведений писателя
print(data)  # Вывод результата