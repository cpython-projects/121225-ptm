# def greetings(name):
#     return f"Hello {name}"
#
#
#
# print(greetings("John"))
#
# x = greetings
#
# print(x('Oleh'))




# def filter_odd(numbers):
#     res = []
#     for number in numbers:
#         if number % 2:
#             res.append(number)
#     return res
#
#
# def filter_even(numbers):
#     res = []
#     for number in numbers:
#         if number % 2 == 0:
#             res.append(number)
#     return res

# x = [1, 2, -4, 5, 7, 89, -34, 123, -4556, 32]
# y = filter_odd(x)
# print(y)
#
# y = filter_even(x)
# print(y)


# def is_odd(item):
#     return item % 2
#
# def is_even(item):
#     return item % 2 == 0
#
# def is_negative(item):
#     return item < 0
#
#
# def my_filter(func, numbers):
#     res = []
#     for number in numbers:
#         if func(number):
#             res.append(number)
#     return res


# x = [1, 2, -4, 5, 7, 89, -34, 123, -4556, 32]
# y = my_filter(is_odd, x)
# print(y)
#
# y = my_filter(is_even, x)
# print(y)
#
# y = my_filter(is_negative, x)
# print(y)


# def add(a, b):
#     return a + b
#
# def sub(a, b):
#     return a - b
#
# def mul(a, b):
#     return a * b
#
# def truediv(a, b):
#     return a / b


# operations = {
#     '+': add,
#     '-': sub,
#     '*': mul,
#     '/': truediv
# }
#
# a, b = 23, 12
# operator = '-'
#
#
# res = operations[operator](a, b)
# print(res)


# functions = (add, sub, mul, truediv)
# numbers = [(1, 2), (3, 4), (5, 6), (7, 8)]
#
# for a, b in numbers:
#     for f in functions:
#         print(f'{f.__name__}({a}, {b}) = {f(a, b)}')

# def my_filter(func, numbers):
#     res = []
#     for number in numbers:
#         if func(number):
#             res.append(number)
#     return res
#
# x = [1, 2, -4, 5, 7, 89, -34, 123, -4556, 32]
# y = my_filter(lambda item: item % 2, x)
# print(y)
#
# y = my_filter(lambda item: item % 2 == 0, x)
# print(y)
#
# y = my_filter(lambda item: item < 0, x)
# print(y)
#
#
# x = ['apple', 'banana', 'orange', 'kiwi']
# res = max(x, key=lambda word: word.lower().count('a'))
# print(res)
#
# l = lambda word : (
#     print(word) or word.lower()
# )
# print(l("AAA"))

# import operator
#
# def get_operations(op):
#     if op == '+':
#         return operator.add
#
#     if op == '*':
#         return operator.mul
#
#     if op == '-':
#         return operator.sub
#
#     if op == '/':
#         return operator.truediv
#
#
#
# print(get_operations('*')(3, 4))


# x = ['a', 'aa', 'aaa', 'aaaa', 'aaaaa', 'aaaaaa', 'aaaaaaa']
# y = list(map(len, x))
# print(y)


# x = tuple(map(int, input('numbers>>').replace(',', ' ').split()))
# print(x)

numbers = [1, 2, 3, 4, 5]
x1 = sum(map(lambda item: item ** 2, numbers))

x2 = sum([item ** 2 for item in numbers])

print(x1)
print(x2)





