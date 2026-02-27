# a = [1, 2, 3]
# b = a
# c = [1, 2, 3]
#
# print(id(a), id(b), id(c))
#
# a = (1, 2, 3)
# b = a
# c = (1, 2, 3)
#
# print(id(a), id(b), id(c))
# print(hash(a), hash(b), hash(c))
#
# a = ([1, 2], 3)
# b = a
# c = ([1, 2], 3)
#
# print(id(a), id(b), id(c))

# a = 'Hello'
# b = a
#
# print(a is b)
# print(id(a) == id(b))

# print(type(id(123)))

# x = 7
# z = 8
# y = x ** 4 + z ** 0.5

# list_elements = [[1, 2, 3], [4, 5], 6, [7], [8, 9]]
# print(list_elements)
#
# print(len(list_elements))

# # Кортеж со списками
# lists_tuple = ([1, 2], [3, 4], [5, 6])
# print(lists_tuple)

# # Список со списками
# lists = [[1, 2], [3, 4]]
# print(lists)


# a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# a[0], a[2] = a[2], a[0]
# print(a)

# list_elements = [[1, 2, 3], [4, 5], 6, [7, [8, [9], 10]]]
#


# print(list_elements[3][1][1][0])


# x = [1, 2, 3]
#
# y = x * 5
# del x
#
#
# y[0][0] = 100
# print(y)
# print(x)
#
#
# del x
#



# x = ([1, 2, 3], 4)
# y = x * 3
#
# print(y)
#
# x[0][0] = 100
# print(y)



# x = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# total = 0
# for row in x:
#     for item in row:
#         total += item
# print(total)
#
# total = 0
# for row in x:
#     total += sum(row)
# print(total)
#
# total = 0
# for i in range(3):
#     for j in range(3):
#         total += x[i][j]
# print(total)


# x = [1, 2, 3, 4, 5]
# y = x.copy()
#
# y[0] = 100
#
# print(x)
# print(y)



# x = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# y = x.copy()
#
# y[0][0] = 100
# print(x)
# print(y)

#
# import copy
# x = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
#
# y = copy.deepcopy(x)
#
# x[0][0] = 100
#
# print(x)
# print(y)

# # VERY BAD
# x = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# y = []
#
# for item in x:
#     y.append(item.copy())
#
# x[0][0] = 100
# print(x)
# print(y)








