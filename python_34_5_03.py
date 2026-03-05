# set1 = {1, 2, 3}
# set2 = {2, 1}
# set3 = {3, 2, 1}
# set4 = {4}
#
# print(set1 > set2)
# print(set1 < set2)
# print(set2 < set1)
#
# print(set1 == set3)
# print(set1 != set3)
#
# res = (set1 | set2) > (set3 | set4)
#
#
# print(set1 != set4, set1.isdisjoint(set4))
# print(len(set1 & set4) == 0)
#
#
# res = 100 | 200
# print(res)


# x = {1, 2, 3, 4, 5, 6, 7, 8}
# for item in x:
#     print(item)



# x = [10, 20, -30, -1, -2, 3, 5]
# x = set(x)
# print(x)
#
# for i in x:
#     print(i)


# numbers = [1, 2, 2, 4, 7, 8, 8, 10]
# even_numbers_set = {num for num in numbers if num % 2 == 0}
# even_numbers_list = [num for num in numbers if num % 2 == 0]
# print(even_numbers_set)
# print(even_numbers_list)
#
# res = sorted(even_numbers_set)
# print(res)


# immutable_set = frozenset([1, 2, 3, 4, 5])
# print(immutable_set)
#
# immutable_set = frozenset((1, 2, 3, 4, 5))
# print(immutable_set)
#
# immutable_set = frozenset({1, 2, 3, 4, 5})
# print(immutable_set)

# a = frozenset({1, 2, 3})
# b = frozenset({4, 5, 6})
# x = {a, b}
# print(x)


# a = frozenset({1, 2, 3})
# b = {4, 5}
#
# print(a | b)
# print(b | a)

# a.union(b)
# b.union(a)

# x = {1: 'one', True: 'true', 1.0: 'float one'}
# print(x)
#
# print(hash(1))
# print(hash(True))
# print(hash(1.0))
#
# x = 5
# x = 7
# x = 9
# print(x)
#
# my_set = {True, 1, 1.0}
# print(my_set)


# a = (1, 2)
# b = (3, 4)
# x = {a: 'one', b: 'two'}
# print(x)
#
#
# a = ([1], 2)
# b = ([3], 4)
# x = {a: 'one', b: 'two'}
# print(x)


# x = [1, 2, 3, 4, 5]
# y = tuple(x)
#
#
# y = dict(x)
# print(y)


# person = dict(name="Bob", age=25, city="London")
# print(person)

# pairs = [("name", "Charlie"), ("age", 35), ("city", ("Paris", 78))]
# person = dict(pairs)
# print(person)

# pairs = [["name", "Charlie"], ["age", 35], ["city", "Paris"]]
# person = dict(pairs)
# print(person)

# x = ['banana', 'apple', 'pear']
# y = [10, 20, 30]
#
# res = dict(zip(x, y))
# print(res)
