# x = 'Hello'
# y = 'Python'
#
# for item in zip(x,y):
#     print(item)


# x = {1, 2, 2, 2, 2, 3, 3, 4, 5}
# print(x)
#
# x = set()
# print(x)
#
# x = {}
# print(type(x))


# x = 'Hello'
#
# if x == 'Hello':
#     print('Ok')
#
# print(hash('Hello'))
# print(hash('Helo'))
#
#
# x = {1, 2, 2, 2, 2, 3, 4, 5, 6, 7, 8, 9}
# print(hash(2))
# print(hash(3))

# print(hash('Hello'))

# print(hash(1) == hash(1.0))
# print(id(1) == id(1.0))
#
# print(hash(5) == hash(5.0))
# print(id(5) == id(5.0))

# x = {1, '1'}
# print(x)


# x, y = 'Hello', 'Hello'
# print(id(x), id(y))
#
# x, y = [], []
# print(id(x), id(y))

# x = {1, 2, 3, [3, 4, 5]}
# print(x)

# x = {'a', 'а'}
# print(x)

# x = 'Python'
# print(x.__hash__())
#
# x = ['Python']
# print(x.__hash__())

# a = [1, 2, 3]
# x = (a, 2, 3, 4)
# y = {x, 1, 2, 3}
# print(y)

# import random
#
# x = [random.randint(1, 50) for _ in range(20)]
# y = set(x)
# print(x)
# print(y)
# print(20 - len(y))
#
#
# text = "hello"
# unique_chars = set(text)
# print(unique_chars)


# print(hash(True))
# print(hash(False))
#
# x = {0, False}
# print(x)

#
# x = {1, 2, 3, 4, 5}
# x.add(6)
# print(x)
#
# if 60 in x:
#     x.remove(60)
#     print(x)
#
# x.discard(6)
# print(x)
#
#
# while x:
#     y = x.pop()
#     print(y, y ** 2)

#x = {1, 2, 3, 4, 5}
#
# y = x.copy()
#
# x.add(6)
#
# print(x)
# print(y)


# friends_oleh = {"Ivan", "Anna", "Dima", "Olga"}
# friends_valeriia = {"Anna", "Olga", "Sergey", "Nina"}
#
# mutual_friends = friends_oleh & friends_valeriia
# print(mutual_friends)
#
#
# all_friends = friends_oleh | friends_valeriia
# print(all_friends)
#
#
# oleh_friends = friends_oleh - friends_valeriia
# print(oleh_friends)

#
# friends_oleh = {"Ivan", "Anna", "Dima", "Olga"}
# friends_valeriia = {"Anna", "Olga", "Sergey", "Nina"}
#
# mutual_friends = friends_oleh.intersection(friends_valeriia)
# print(mutual_friends)
#
#
# all_friends = friends_oleh.union(friends_valeriia)
# print(all_friends)
#
#
# oleh_friends = friends_oleh.difference(friends_valeriia)
# print(oleh_friends)


# a = {1, 2, 3, 4, 5}
# b = {4, 5, 6, 7}
# print(id(a))
# a.update(b)
# print(a)
# print(id(a))


x = [{1, 2, 3, 4, 5}, {2, 4, 6, 7, 8}, {1, 2, 4, 90}]

# res = x[0]
# for curr_set in x:
#     res.intersection_update(curr_set)
#
# print(res)


res = set.intersection(*x)
print(res)