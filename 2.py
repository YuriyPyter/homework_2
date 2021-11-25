my_list = input('Заполните список элементов через запятую: ').split(',')
print(my_list)
my_list[:-1:2], my_list[1::2] = my_list[1::2], my_list[:-1:2]
print(my_list)
