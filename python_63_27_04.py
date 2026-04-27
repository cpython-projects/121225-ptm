# a = 5
# def outer_function():
#     print("Внутри внешней функции")
#     message = "Внешняя функция\n"
#     def inner_function(a=3):
#         nonlocal message
#         message = "Внутрення функция\n"
#         print(message * a)
#
#     inner_function() # Вызов вложенной функции
#     print(message)
#
#
#
# outer_function()
# # inner_function()
# print(a, True)


# def outer_function():
#     message = "Внешняя функция"
#     def middle_function():
#         nonlocal message
#         message = "Средняя функция"
#         def inner_function():
#             nonlocal message
#             message = "Изменено во вложенной функции"
#         inner_function()
#     middle_function()
#     print(message)
#
# outer_function()


# def process_data(data):
#     def clean_text(text):
#         return text.strip().lower()
#
#
#     cleaned_data = [clean_text(item) for item in data]
#     return cleaned_data
# data = [" Apple ", " BaNaNa ", " CHERRY "]
# print(process_data(data))

# def analyze_text(text):
#     def count_words():
#         return len(text.split())
#     def count_letters():
#         return sum(1 for char in text if char.isalpha())
#
#     return {
#         "words": count_words(),
#         "letters": count_letters()
#     }
#
# print(analyze_text("Пример текста!")['words'] ** 2)


# def outer_function(text):
#     def inner_function():
#         return text.upper()
#
#     return inner_function # Возвращаем незапущенную функцию
#
#
# f = outer_function('Hello')
# print(f)
#
# print(f())


# def counter():
#     count = 0
#
#     def inner_function():
#         nonlocal count
#         count = count + 1
#         return count
#
#     return inner_function
#
#
# res = counter()
# for i in range(10):
#     print(res())

# def exp(b=3):
#     def inner(a):
#         return a ** b
#
#     return inner
#
#
# exp_func = exp()
# for i in range(10):
#     print(exp_func(i))


# def create_filter(border):
#     def filter_value(value):
#         return value > border # Использует сохранённый border
#
#     return filter_value
#
# greater_than_five = create_filter(5) # Объект замыкания
# print(greater_than_five)
# print(greater_than_five(7))
# print(greater_than_five(3))


# def factorial(n):
#     result = 1
#     for i in range(2, n + 1):
#         result *= i
#     return result
#
#
# print(factorial(5))
# print(factorial(15))
# print(factorial(10))
# print(factorial(6))



# def factorial():
#     results = [1, 1]
#
#     def inner(n):
#         if n < len(results):
#             return results[n]
#         result = results[-1]
#         for i in range(len(results), n + 1):
#             result *= i
#             results.append(result)
#         return result
#
#     return inner
#
#
# f = factorial()
# print(f(5))
# print(f(6))
# print(f(15))
#

# import time
# def long_function(num):
#     time.sleep(num)
#     return list(range(num))
#
# def memoize():
#     cache = {}
#     def get_or_compute(key, compute_function):
#         if key not in cache:
#             cache[key] = compute_function(key)
#         return cache[key]
#
#     return get_or_compute
#
#
# cached_computation = memoize()
# start = time.time()
# print(cached_computation(10, long_function))
# print("Время расчёта:", time.time() - start)
#
# start = time.time()
# print(cached_computation(10, long_function))
# print("Время получения из кэша:", time.time() - start)


# def get_taxes(salary: float | int, rate: float=0.3) -> float:
#     """
#     Returns tax value.
#     :param salary: Employee salary.
#     :param rate: Tax rate.
#     :return: Tax value.
#     """
#     return salary * rate
#
#
# print(get_taxes.__name__)
# print(get_taxes.__doc__)
#

#
# def outer():
#     def inner():
#         """Вложенная функция"""
#         pass
#     return inner
#
# func = outer()
# print("Имя функции:", func.__name__)
# print("Документация:", func.__doc__)
#

# def outer():
#     def inner():
#         print("Hi")
#     return inner()
#
# result = outer()
# result()
#
#
# def decorator(func):
#     def wrapper(*args, **kwargs):
#         print('Обработка перед вызовом')
#         res = func(*args, **kwargs)
#         print('Обработка после вызова')
#         return res
#
#
#     return wrapper
#
# print()
#
# @decorator
# def greetings(name):
#     return f'Hello, {name}'
#
# @decorator
# def full_greetings(first_name, last_name):
#     return f'Hello, {last_name} {first_name[0]}.'
#
# @decorator
# def common_greetings():
#     return 'Hello, User'
#
#
# print(greetings('John'))
#
# name = input('name>>')
#
# name = name.split()
#
# if len(name) == 1:
#     print(greetings(name))
# elif len(name) == 2:
#     print(full_greetings(name[0], name[1]))
# else:
#     print(common_greetings())


#
# if len(name) == 2:
#     func = full_greetings
# elif len(name) == 1:
#     func = greetings
# else:
#     func = common_greetings
#
# f = decorator(func)
# print(f(*name))

#
# f = decorator(full_greetings)
# print(f('Oleh', 'Tymchuk'))
#

# def tag_b(func):
#     def wrapper(*args, **kwargs):
#         return f"<b>{func(*args, **kwargs)}</b>"
#
#     return wrapper
#
#
# def tag_i(func):
#     def wrapper(*args, **kwargs):
#         return f"<i>{func(*args, **kwargs)}</i>"
#
#     return wrapper



# def greetings(name):
#     return f'Hello, {name}'
#
#
# name = input('name>>').strip().title()
#
# if ' ' in name:
#     f = tag_i(greetings)
# else:
#     f = tag_b(greetings)
#
# print(f(name))

# @tag_b
# @tag_i
# def greetings(name):
#     return f'Hello, {name}'
#
# name = input('name>>').strip().title()
# print(greetings(name))
#


# import time
#
# def timing(func):
#     def wrapper(*args, **kwargs):
#         start = time.time()
#         res = func(*args, **kwargs)
#         end = time.time()
#         print(f'start: {start}, end: {end}, d: {end - start}')
#         return res
#
#     return wrapper
#
#
# @timing
# def test_func():
#     time.sleep(2)
#     return 'finish'
#
#
# print(test_func())
# print(test_func())



#
# def tag_b(func):
#     def wrapper(*args, **kwargs):
#         return f"<b>{func(*args, **kwargs)}</b>"
#
#     return wrapper
#
#
# def tag_i(func):
#     def wrapper(*args, **kwargs):
#         return f"<i>{func(*args, **kwargs)}</i>"
#
#     return wrapper


# def html_tag(tag: str):
#     def decorator(func):
#         def wrapper(*args, **kwargs):
#             return f"<{tag}>{func(*args, **kwargs)}</{tag}>"
#         return wrapper
#     return decorator
#
#
# @html_tag('p')
# @html_tag('i')
# @html_tag('b')
# def greetings(name: str):
#     return f'Hello, {name}'
#
#
# print(greetings('John'))


# import time
#
#
# def retry(k):
#     def decorator(func):
#         def wrapper(*args, **kwargs):
#             for delay in k:
#                 try:
#                     res = func(*args, **kwargs)
#                     return res
#                 except Exception as e:
#                     pass
#                 time.sleep(delay)
#         return wrapper
#     return decorator
#
#
# @retry([1, 5, 25, 50])
# def read_data(filename):
#     with open(filename, 'r') as f:
#         return sum(int(line) for line in f)
#
#
# print(read_data('python_63.txt'))

#
# import logging
# import functools
#
# logging.basicConfig(
#     level=logging.DEBUG,
#     format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
#     filename='python_63.log',
#     filemode='a'
# )
#
#
# def log_decorator(func):
#     @functools.wraps(func)
#     def wrapper(*args, **kwargs):
#         try:
#             res = func(*args, **kwargs)
#             logging.info(f'Success calling {func.__name__}; Result is {res}')
#             return res
#         except Exception as e:
#             logging.error(e)
#             raise e
#     return wrapper
#
#
#
# @log_decorator
# def read_data(filename):
#     """
#     Reads data from file.
#     """
#     with open(filename, 'r') as f:
#         return sum(int(line) for line in f)
#
# print()
#
# @log_decorator
# def get_taxes(salary: int | float, rate: float) -> int | float:
#     """
#     Return the taxes given a salary and a rate.
#     """
#     return salary * rate
#
#
# # res = read_data('python_63.txt')
#
#
# print(get_taxes.__annotations__)
# print(get_taxes.__doc__)
# print(get_taxes.__name__)
#
#
# print(read_data.__annotations__)
# print(read_data.__doc__)
# print(read_data.__name__)




def user_role(role):
    def decorator(func):
        def wrapper(*args, **kwargs):
            data = func(*args, **kwargs)
            result = [line for line in data if line.startswith(role)]
            return result
        return wrapper
    return decorator


@user_role('admin')
def read_data_file(filename):
    with open(filename, 'r') as f:
        for line in f:
            yield line.strip()


for item in read_data_file('python_63.txt'):
    print(item)












