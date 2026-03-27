# Реализуйте функцию, которая поддерживает механизм LRU-кэша для очереди задач.
# Функция должна принимать:
# Текущую очередь задач.
# Новые задачи для добавления.
# Максимальный размер очереди.
# Если лимит очереди превышен, удаляйте задачи, которые не использовались дольше всех.
# Данные:
# tasks = ["task1", "task2", "task3", "task4", "task5", "task6"]
# new1 = "task4"
# new2 = "task1"
# new3 = "task7"
# new4 = "task2"
#
# Пример вывода:
# Очередь из 4 новых задач: ['task4', 'task1', 'task7', 'task2']

from collections import OrderedDict


# def lru_cache(queue: list[str], *new_tasks, limit: int = 4):
#     queue = OrderedDict([(task, None) for task in queue[-limit:]])
#     for task in new_tasks:
#         if task in queue:
#             queue.move_to_end(task)
#         else:
#             queue[task] = None
#
#         if len(queue) > limit:
#             queue.popitem(last=False)
#
#     return list(queue)


# def lru_cache(queue: list[str], *new_tasks, limit: int = 4):
#     queue = queue[-limit:]
#     for task in new_tasks:
#         if task in queue:
#             queue.remove(task)
#
#         queue.append(task)
#
#         if len(queue) > limit:
#             queue.pop(0)
#
#     return queue


# from collections import deque
# def lru_cacher(lst: list[str], *new_tasks, max_limit: int = 4) -> list[str]:
#     new = deque(lst[-max_limit:])
#     for new_task in new_tasks:
#         new.append(new_task)
#         if len(new) > max_limit:
#             new.popleft()
#     return new

# print(lru_cacher(tasks, new1, new2, new3, new4, max_limit=4))
#
# print(lru_cache(['task4', 'task1', 'task7', 'task2', 'task8'], 'task2', 'task3'))



# Реализуйте функции:
# Преобразуйте все буквы в предложении в верхний регистр.
# Зашифруйте строку, сдвинув символы на 5 элементов вправо.
# Переверните строку.
# Реализуйте функцию шифрования, которая последовательно применит каждую из списка переданных функций к переданной строке.
# Данные:
# sentence = "Functional programming is powerful"
# functions = [to_uppercase, shift_encrypt, reverse_string]
# Пример вывода:
# QZKWJ\TU%XN%LSNRRFWLTWU%QFSTNYHSZK


# def text_to_uppercase(text: str) -> str:
#     return text.upper()
#
#
# def shift_to_5(text: str) -> str:
#     return ''.join(map(lambda char: chr(ord(char) + 5), text))
#
#
# def reverse_text(text: str) -> str:
#     return text[::-1]
#

# operations = [text_to_uppercase, shift_to_5, reverse_text]

# sentence = "Functional programming is powerful"

# for operation in operations:
#     sentence = operation(sentence)
#
# print(sentence)


# operations = [str.upper, shift_to_5, reverse_text]
#
# sentence = "Functional programming is powerful"

# for operation in operations:
#     sentence = operation(sentence)
#
# print(sentence)

# from functools import reduce
#
# res = reduce(lambda acc, operator: operator(acc), operations, sentence)
# print(res)


# fs = {
#     "projects": {
#         "bot":  {
#             "main.py": 12,
#             "config.py": 4
#         },
#         "site": {
#             "index.html": 8,
#             "style.css": 3
#         }
#     },
#     "readme.txt": 2
# }
#
#
# def folder_size(node):
#     if isinstance(node, dict):
#         total = 0
#         for v in node.values():
#             total += folder_size(v)
#         return total
#     return node
#
#
# print(folder_size(fs))



# data = [1, [2, 3], [4, [5, [6, 7]]]]
#
# def flat_list(lst):
#     result = []
#     for item in lst:
#         if isinstance(item, list):
#             result.extend(flat_list(item))
#         else:
#             result.append(item)
#     return result
#
# print(flat_list(data))



# Реализуйте аналог deepcopy() с помощью рекурсии. Не забудьте проверить, чтобы изменения в копии не затронули оригинал.
# Данные:
# original_data = [
#     [1, 2, 3],                 # Вложенный список
#     (4, [5, 6], {7, 8}),       # Кортеж с вложенными структурами
#     {"a": 9, "b": [10, 11]},   # Словарь со списком
#     "Hello",                   # Строка
#     [12, (13, 14)],            # Список с кортежем
#     15.5,                      # Число с плавающей точкой
#     5                          # Целое число
# ]
# Пример вывода:
# Исходный: [[1, 2, 3], (4, [0, 6], {8, 7}), {'a': 9, 'b': [10, 11]}, 'Hello', [12, (13, 14)], 15.5, 5]
# Копия:    [[1, 2, 3], (4, [5, 6], {8, 7}), {'a': 9, 'b': [10, 11]}, 'Hello', [12, (13, 14)], 15.5, 5]



def deep_copy(obj):
    if isinstance(obj, list):
        return [deep_copy(item) for item in obj]
    elif isinstance(obj, dict):
        return {k: deep_copy(v) for k, v in obj.items()}
    elif isinstance(obj, tuple):
        return tuple(deep_copy(item) for item in obj)
    elif isinstance(obj, set):
        return {deep_copy(item) for item in obj}
    return obj


original_data = [
    [1, 2, 3],                 # Вложенный список
    (4, [5, 6], {7, 8}),       # Кортеж с вложенными структурами
    {"a": 9, "b": [10, 11]},   # Словарь со списком
    "Hello",                   # Строка
    [12, (13, 14)],            # Список с кортежем
    15.5,                      # Число с плавающей точкой
    5                          # Целое число
]


print(deep_copy(original_data))