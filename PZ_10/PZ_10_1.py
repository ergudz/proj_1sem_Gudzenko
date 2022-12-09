# В магазинах имеются следующие товары. Магнит – молоко, соль, сахар.
# Пятерочка – мясо, молоко, сыр. Перекресток – молоко, творог, сыр, сахар. Определить:
# 1. в каких магазинах нельзя приобрести сыр.
# 2. в каких магазинах можно приобрести одновременно молоко и сахар.
# 3. в каких магазинах можно приобрести соль.

shops = {
    'Магнит': ['молоко', 'соль', 'сахар', ],
    'Пятерочка': ['мясо', 'молоко', 'сыр', ],
    'Перекресток': ['молоко', 'творог', 'сыр', 'сахар', ],
}
shops_havent_cheese = []
shops_with_milk_cheese = []
shops_with_solt = []

for x in shops.keys():
    if 'сыр' not in shops[x]:
        shops_havent_cheese.append(x)
    if 'молоко' in shops[x] and 'сахар' in shops[x]:
        shops_with_milk_cheese.append(x)
    if 'соль' in shops[x]:
        shops_with_solt.append(x)

print(f'Магазины в которых нельзя приобрести сыр: {(", ".join(shops_havent_cheese))}')
print(f'Магазины в которых можно приобрести одновременно молоко и сахар: {(", ".join(shops_with_milk_cheese))}')
print(f'Магазины в которых можно приобрести соль: {(", ".join(shops_with_solt))}')
