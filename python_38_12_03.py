# def greet(name):
#     return f"Hello, {name}!"
#
#
#
# res = greet("Oleh")
# print(res)
#
# res = greet("Alice")
# print(res)
#
#
# def action1():
#     return "Hello"
#
#
# def action2():
#     return 'world'
#
#
# def action3():
#     pass
#
#
#
# res = f'{action1()} {action2()} {action3()}'
# print(res)


# def calc(a, b, c=40, d=20):
#     return a * b + c * d
#
#
# res = calc(1, 1)
# print(res)


# def calc_sum(*args, **kwargs):
#     total = 0
#     for arg in args:
#         if isinstance(arg, int | float):
#             total += arg
#
#
#     for key, value in kwargs.items():
#         if key == 'a':
#             return total * value
#
#     return total
#
#
#
# # print(1, 2, 3, 4, 5)
# # print(1, 2, 3, 4, 5, 1, 2, 3, 4, 5)
#
# print(calc_sum(1, '2', 3, '4', 5, a=6))



# def calc(a, b, *args, c=10, **kwargs):
#     if not args:
#         return a + b * c
#
#     return sum(args) + a + b * c
#
#
# print(calc(1, 2, 5, 6, 7, 8, 9, f=40, r=30, c=50))


# def show_full_info(name, *args, age=25, **kwargs):
#     print(f"Name: {name}")
#     print(f"Other details: {args}")
#     print(f"Age: {age}")
#     print(f"Additional info: {kwargs}")
#
# show_full_info("Alice", "Developer", age=30, city="New York", hobby="Reading")

#
# points = 4
#
# if points < 4:
#     grade = 'F'
# elif points < 3:
#     grade = 'S'
# elif points < 2:
#     grade = 'G'
# else:
#     grade = 'E'
#
#
# def student_grade(points):
#     if points < 4:
#         return 'F'
#     if points < 3:
#         return 'S'
#     if points < 2:
#         return 'G'
#     return 'E'
#
# print(student_grade(points))


def f1():
    return


res = f1()
print(res)