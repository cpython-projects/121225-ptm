# def add(a, b):
#     return a + b
#
#
#
# res = 23 + add(1, 2)
# print(res)
#
# res = 45 + add(1, 2)
# print(res)


# n = 6
#
# factorial = 1
# for i in range(2, n + 1):
#     factorial = factorial * i
#
# print(factorial)



# n! = (n - 1) * n


# def factorial(n):
#     if n == 0:
#         return 1
#
#     return n * factorial(n - 1)
#
#
#
# res = factorial(5)
# print(res)

import sys


# def countdown(n: int) -> None:
#     if n <= 0:
#         print("Конец!")
#         return
#     print(n)
#     countdown(n - 1)
#     print(n)
#
#
# countdown(5000)


# from functools import lru_cache
#
# @lru_cache(maxsize=None)
# def fibonacci(n):
#     if n <= 1:
#         return n
#     return fibonacci(n - 1) + fibonacci(n - 2)
#
#
# for i in range(50):
#     print(i, fibonacci(i))
#
#
def fibonacci_iter(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b

    return a


for i in range(50):
    print(i, fibonacci_iter(i))



