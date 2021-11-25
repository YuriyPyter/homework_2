month = int(input('Введите месяц: '))
# Список
month_list = [[12, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11]]
if month in month_list[0]:
    print('Зима')
elif month in month_list[1]:
    print('Весна')
elif month in month_list[2]:
    print('Лето')
elif month in month_list[3]:
    print('Осень')
else:
    print('Такого месяца нет. Вы инициативный!')
# Словарь
month_dict = {'Зима': (12, 1, 2), 'Весна': (3, 4, 5), 'Лето': (6, 7, 8), 'Осень': (9, 10, 11)}
for key in month_dict.keys(): # в key записываются все ключи
    if month in month_dict[key]:
        print(key)


