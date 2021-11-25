my_list = [7, 5, 3, 3, 2]
while True:
    number = int(input('Введите натуральное число: '))
    my_list.insert(0, number)
    my_list.sort(reverse=True)
    print(my_list)
    question = input('Желаете продолжить? (да/нет): ')
    if question == 'да':
        continue
    else:
        print(my_list)
        break