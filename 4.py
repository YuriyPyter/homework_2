words = input('Введите несколько слов через пробел: ').split()
for ind, el in enumerate(words, 1):
    print(ind, el[:][:10])


