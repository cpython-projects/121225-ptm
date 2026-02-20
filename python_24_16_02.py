# y = 786876
# x = f'{y}'
#
# print(x)
#
# print(x.format(4))


# x = '{y}'
#
# print(x.format(y=1))
# print(x.format(y=2))

# y = 1
# print(f'{y}')
# y = 2
# print(f'{y}')


# x = [1, 2, 3, 4, 5]
# x[0] = 100
# print(x[0])
# x = 'Python'
# # x[0] = 'p'
# print(x[0])



# x = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# print(x)


# my_tuple = (1, 2, 3, "apple", True)
# print(my_tuple)
#
# print(my_tuple[-1])


#
# x = [1, 2, 3]
# y = [4, 5, 6]
#
# test = (x, y)
#
# print(type(test), id(test), len(test))
# print(test)
#
#
# x[0] = 100
# y[0] = 400
# print(test)
#
# x = [40, 50, 60]
# print(test)
#
# x[0] = -100
# print(test)


# x = ()
# print(type(x))


# x = (1, )
# print(x, type(x))



# x = tuple('Python')
# print(x)
#
# x = [1, 2, 3, 4, 5]
# y = tuple(x)
# print(y)

# x = tuple(['Python', 6])


# tuple1 = (1, 2)
# tuple2 = (3, 4)
# print(tuple2 + tuple1) # Конкатенация кортежей
#
# my_tuple = (1, 2)
# print(my_tuple * 3) # Повторение кортежей
#
#
#
#
# my_tuple = (10, 20, 30)
# print(20 in my_tuple) # Проверка на наличие элемента
# my_tuple = (1, 2, 3, 4, 5)
# print(len(my_tuple)) # Длина кортежа
# # Сравнение кортежей происходит аналогично спискам, то есть поэлементно
# tuple1 = (1, 2, 3)
# tuple2 = (1, 2, 4)
# print(tuple1 == tuple2) # Сравнение кортежей
#
#
#
# print(min(my_tuple))
# print(max(my_tuple))
# print(sum(my_tuple))


# my_tuple = (1, 2, 3, 4, 5, 6, 7, 8)
# y = my_tuple[2:]
# print(y)
# print(my_tuple[::-1])

# my_tuple = tuple(['Python', 6])
# print(my_tuple)
#
# x = (1, 2, 3, 4, 5)
# y = list(x)
# print(y)

# a = 1, 2, 3
# print(a)
#
# x = (1, 2, 3)
# a, b, c = x
# print(a, b, c)
#
# a, b, c = 'Pyt'
# print(a, b, c)
#
# a, b, c = [10, 20, 30]
# print(a, b, c)


# x = 'P', 'y', 't'
# print(x)


# x = (100, 20, 30, 40, 50)
#
# *a, b, c = x
# print(a, b, c)
#
# a, *b, c = x
# print(a, b, c)
#
# a, b, *c = x
# print(a, b, c)


# x = (40, 50)
# *a, b, c = x
# print(a, b, c)


# x = (40, )
# *a, b, c = x
# print(a, b, c)



# x = (10, 20, 30, 40)
# *a, *b, c = x
# print(x)


# x = 'Python'
# *a, b, c = x
# print(a, b, c)


test = [
    '1 Bob Simson 19.58$ decorations',
    '2 Mary 66.7$ food',
    '3 Mary 98.91$ toys',
    '4 Aleksa 72.29$ drinks',
    '5 Maria Simson 84.48$ food',
]

# amount = 0
# for line in test:
#     data = line.split()
#     amount += float(data[-2].replace('$', ''))
#
# print(f'{amount:.2f}')

# bob = mary = maria = aleksa = 0
# for line in test:
#     _, *name, money, category = line.split() # ['Aleksa'], ['Bob', 'Simson']
#     name = ' '.join(name)
#     money = float(money.replace('$', ''))
#     if name == 'Bob Simson':
#         bob += money
#     elif name == 'Mary':
#         mary += money
#     elif name == 'Maria':
#         maria += money
#     else:
#         aleksa += money
#
# print(aleksa)



# x = (1, 2, 3, 4, 5, 6, 78, 0)
# print(*x, sep='\n')


# x = 'Python'
# x = list(enumerate(x))
# print(x)


x = [1, 2, 3, 4, 5, 6, 7, 8]
# for i in range(len(x)):
#     if x[i] % 2:
#         x[i] = x[i] ** 2
#
# print(x)


for i, item in enumerate(x):
    if item % 2:
        x[i] = item ** 2
print(x)

