# data = ['2024-03-01 12:00:01 - Info: System started successfully.',
#         '2024-03-01 12:05:32 - Error: Failed to connect to the database.',
#         '2024-03-01 12:10:15 - Warning: Low memory detected.',
#         '2024-03-01 12:15:47 - Error: Access denied to the file.',
#         '2024-03-01 12:20:02 - Info: User logged in.',
#         '2024-03-01 12:25:19 - Error: Network connection lost.',
#         '2024-03-01 12:30:41 - Info: System shutdown completed.'
#         ]
#
# for log in data:
#     if 'Error' in log:
#         print(log)

# data = ['Info: System started successfully.',
#         'Error: Failed to connect to the database.',
#         'Warning: Low memory detected.',
#         'Error: Access denied to the file.',
#         'Info: User logged in. Maybe in future it will be Error',
#         'Error: Network connection lost.',
#         'Info: System shutdown completed.'
#         ]
#
# for log in data:
#     if log.startswith('Error'):
#         print(log)
#
#     if log.endswith('Error'):
#         print(log)

# x = 'Hello'
# for i, item in enumerate(x):
#     print(item)
#     print(id(item))
#     print(id(x[i]))
#     print(id(x))
#     print('-' * 20)


# x = [10, 20, 30, 40]
# it = x.__iter__()
#
# print(it)
#
# item = it.__next__()
# print(item)
#
# item = it.__next__()
# print(item)
#
# item = it.__next__()
# print(item)
#
# item = it.__next__()
# print(item)
#
#
# item = it.__next__()
# print(item)


# x = [10, 20, 30, 40]
#
# print(x.__next__())

# x = [10, 20, 30, 40]
#
# it = iter(x) # x.__iter__()
# print(next(it)) # it.__next__()
# print(next(it))
# print(next(it))
# print(next(it))
#
# print(x.__len__()) # len(x)

# x = [10, 20, 30, 40]
# for item in x:
#     print(item)
#
#
#
# it = iter(x)
# while True:
#     try:
#         item = next(it)
#         print(item)
#     except StopIteration:
#         break
#
# print('Finish')


# n = 5
#
# for i in range(n): # 1 step - создание итератора с n = 5, остальные шаги - работа с итератором при n = 5
#     print(i)
#     n += 1


# x = [1, 2, 3, 4, 5]
# for item in x:
#     print(item)
#     x.append(item)

# x = [1, 2, 3, 4, 5]
# for i in range(len(x)):
#     print(x[i])
#     x.append(x[i])

# x = (1, 2, 3)
# for item in x:
#     print(item)
#     x = (item, )
#     print(x)

# x = {'a', 'b', 'c'}
# for item in x:
#     print(item)
#     x.add(f'{item}1')


# import sys
#
# numbers_list = [x for x in range(1_000_000)]
# print("Размер списка:", sys.getsizeof(numbers_list), "байт")
#
#
# numbers_iterator = numbers_list.__iter__()
# print("Размер итератора:", sys.getsizeof(numbers_iterator), "байт")
#
#
# numbers = [5, 10, 15]
# iterator = iter(numbers)

# for num in iterator: # __iter__
#     print(num)
# for num in iterator:
#     print(num)

# for number in iterator:
#     print(number)
#     print(next(iterator))


import itertools

# counter = itertools.count(start=0, step=5)
#
# i = 0
# while i < 10:
#     print(next(counter))
#     i += 1

# cycle = itertools.cycle(['A', 'B', 'C', 'D'])
#
# print(next(cycle))
# print(next(cycle))
# print(next(cycle))
# print(next(cycle))
# print(next(cycle))
# print(next(cycle))
# print(next(cycle))

import sys

# a = [1, 2, 3, 7, 9, 0]
# b = ['a', 'b', 'c']
#
# chain = itertools.chain(a, b)
# for i in chain:
#     print(i)
#
#
# merged = a + b
# print(merged)
# print(sys.getsizeof(chain))
# print(sys.getsizeof(merged))


# x = [1, 2, 3]
# y = ['A', 'B', 'C']
#
#
# for i in x:
#     for j in y:
#         print(i, j)
#
#
#
# prod = itertools.product(x, y)
# for i in prod:
#     print(i)


# x = ['A', 'B', 'C']
#
#
# res = itertools.permutations(x)
#
# for i in res:
#     print(i)

# alphabet = 'absdef12345_'
#
# res = itertools.permutations(alphabet, 5)
#
#
# for i, item in enumerate(res):
#     print(i, item)
#
#


# x = [i for i in range(100)]
# print(sum(x))
# print(sys.getsizeof(x))
#
# x = (i for i in range(100))
# print(x)
# print(sum(x))
# print(sys.getsizeof(x))


# x = (i for i in range(100))
# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))



with open('test.txt') as f:
    res = sum(int(line) for line in f)
    print(res)


























