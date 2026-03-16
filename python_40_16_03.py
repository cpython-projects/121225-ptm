# def is_number_simple(n):
#     if n == 1:
#         return False
#
#     for div in range(2, n):
#         if not n % div:
#             return False
#
#     return True
#
# print(f"Число является простым? {is_number_simple(17)}")

# import time
# print('Start')
# time.sleep(2) # Задержка на 2 секунды
# print("2 секунды спустя...")



# import time
# start_time = time.time()
# # Создание объекта range
# range_million = range(1000000)
# end_time = time.time()
# print(f"Время создания range: {end_time - start_time:.10f} секунд")
# start_time = time.time()
# # Создание объекта списка
# lst = [x for x in range(1000000)]
# end_time = time.time()
# print(f"Время создания list: {end_time - start_time:.10f} секунд")


# # Импорт класса из модуля collections
# from collections import OrderedDict
# # Создание пустого OrderedDict
# od = OrderedDict()
# # Добавление элементов аналогично работе со словарем
# od["a"] = 1
# od["b"] = 2
# od["c"] = 3
# print(od)
#
# # x = {1: 'one', 2: 'two', 3: 'three'}
# # print(x.popitem())
# # print(x)
#
# print(od.popitem(last=False))
# print(od)


# from collections import OrderedDict
# queue = OrderedDict()
# queue["task1"] = "low priority"
# queue["task2"] = "medium priority"
# queue["task3"] = "low priority"
# queue["task4"] = "high priority"
# queue["task5"] = "medium priority"
# # Собираем ключи для перемещения
# keys_to_end = [key for key, value in queue.items() if "low" in value]
# keys_to_start = [key for key, value in queue.items() if "high" in value]
# # Перемещаем задачи с низким приоритетом в конец
# for key in keys_to_end:
#     queue.move_to_end(key)
# # Перемещаем задачи с высоким приоритетом в начало
# for key in keys_to_start:
#     queue.move_to_end(key, last=False)
#
#
# while queue:
#     print(queue.popitem(last=False))
#
# from time import time, sleep
# from functools import lru_cache
#
# @lru_cache(maxsize=2)
# def compute_square(n):
#     print(f"Вычисляю квадрат числа {n}...")
#     sleep(5) # Имитация долгой операции
#     return n * n# Измерение времени выполнения
#
#
#
# start_time = time()
# print(f"Результат: {compute_square(2)}")
# print(f"Время: {time() - start_time:.2f} секунд\n")
#
# start_time = time()
# print(f"Результат: {compute_square(3)}")
# print(f"Время: {time() - start_time:.2f} секунд\n")
#
# start_time = time()
# print(f"Результат: {compute_square(2)}")
# print(f"Время: {time() - start_time:.2f} секунд\n")\
#
# start_time = time()
# print(f"Результат: {compute_square(4)}")
# print(f"Время: {time() - start_time:.2f} секунд\n")
#
# start_time = time()
# print(f"Результат: {compute_square(3)}")
# print(f"Время: {time() - start_time:.2f} секунд\n")


from collections import defaultdict

# x = defaultdict(int)
# x['a'] += 1
# print(x)

# x = defaultdict(list)
# x['Anna'].append(15)
# print(x)


# x = defaultdict(str)
# x['a'] += '1'
# print(x)


# from collections import defaultdict
# # Пользовательская функция для значения по умолчанию
# def default_value():
#     return "default"
#
# dd = defaultdict(default_value)
# print(dd['missing_key'])
# print(dd)


#
# # Обычный словарь
# my_dict = {}
# if 'a' not in my_dict:
#     my_dict['a'] = []
# my_dict['a'].append(1)
# print(my_dict)
#
# from collections import defaultdict
# my_dict = defaultdict(list)
# my_dict['a'].append(1)
# print(my_dict)

# from collections import defaultdict
# data = [
#     ("class1", "Alice"),
#     ("class2", "Bob"),
#     ("class1", "Charlie")
# ]
# grouped = defaultdict(list)
#
# for group, name in data:
#     grouped[group].append(name)
#
# print(grouped["class1"])

# 1. Подсчёт символов в строке:
from collections import Counter
# text = "hello world"
# counter = Counter(text)
# print(counter)



# data = {"apple": 3, "banana": 2, "cherry": 1}
# counter = Counter(data)
# print(counter)

words = ["cherry", "cherry", "cherry", "cherry", "cherry", "apple", "apple", "apple", "banana", "apple",  "banana", "apple"]
counter = Counter(words)
print(counter)


print(counter.most_common(1))