while True:
    name = input('Введите название: ')
    price = int(input('Введите цену: '))
    quantity = int(input('Введите количество: '))
    question = input('Хотите продолжить? (да/нет): ')
    my_dict = {'название': name, 'цена': price, 'количество': quantity, 'ед': 'шт'}
    my_list_1 = []
    for i, x in enumerate(my_dict):
        my_dict = [(x, my_dict)]
        my_list_1.append(my_dict)
    if question == 'да':
        continue
    else:
        print(my_list_1)
        break