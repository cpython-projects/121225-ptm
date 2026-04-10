# import os
#
# relative_path = "example.txt"
#
# res = os.path.join(os.getcwd(), relative_path)
#
# absolute_path = os.path.abspath(relative_path)
# print(f"Абсолютный путь: {absolute_path}")


# import os
# # Рекурсивный обход директории
# for root, dirs, files in os.walk("."):
#     print(f"Текущая директория: {root}")
#     print(f"Поддиректории: {dirs}")
#     print(f"Файлы: {files}")
#     print("-" * 50)

# name = input()
# age = int(input())
#
# print(f'Hello, {name}. Your age is {age}')


# import sys
#
# # print(sys.argv)
# # print(type(sys.argv))
#
# # if len(sys.argv) == 3:
# #     _, name, age = sys.argv
# #     print(f'Hello, {name}. Your age is {age}')
#
#
# for arg in sys.argv[1:]:
#     print(arg)


#
# import argparse
#
# parser = argparse.ArgumentParser(description="Обработка файлов")
#
# parser.add_argument("input",                   # позиционный
#     help="Входной файл")
#
# parser.add_argument("--output", "-o",          # опциональный
#     default="result.txt",
#     metavar="FILE",
#     help="Выходной файл (по умолч.: result.txt)")
#
# parser.add_argument("--count", "-n",
#     type=int,
#     default=10,
#     help="Количество строк")
#
# parser.add_argument("--verbose", "-v",
#     action="store_true",                       # True/False флаг
#     help="Подробный вывод")
#
# parser.add_argument("--mode",
#     choices=["fast", "slow", "auto"],
#     default="auto",
#     help="Режим работы")
#
# args = parser.parse_args()
#
# # Использование:
# print(args.input)    # "data.csv"
# print(args.output)   # "result.txt"
# print(args.count)    # 10
# print(args.verbose)  # False
# print(args.mode)     # "auto"

from collections import Counter

# # BAD
# def count_letters():
#     text = "Hello world"
#     return Counter(text)
#
#
# print(count_letters())
# print(count_letters())
# print(count_letters())
#
#
#
# # BAD
# def count_letters():
#     text = input("Enter a string: ")
#     res = Counter(text)
#     print(res)
#
# count_letters()
# count_letters()
# count_letters()
#
#
# with open('test_1.txt', 'r') as file_input:
#     for line in file_input:
#         res = count_letters(line)


# def count_letters(line):
#      res = Counter(line)
#      print(res) # BAD
#      return res
#
#
# with open('test.txt', 'r') as file_input:
#     for line in file_input:
#         res = count_letters(line)
#         for k, v in res.items():
#             print(k, v)


# def count_letters(line):
#     return Counter(line)
#
#
# with open('test.txt', 'r') as file_input:
#     for line in file_input:
#         res = count_letters(line)
#         for k, v in res.items():
#             print(k, v)


# BAD
# def salary_netto(salary, rate=0.2):
#     try:
#         res = salary * (1 - rate)
#     except Exception:
#         res = 'Ошибка'
#     return res
#
#
# print(f'Netto: {salary_netto(1000) + 1000}')
# try:
#     res = salary_netto('1000')
#     print(res)
# except Exception:
#     print('Error')

import logging


logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')


def salary_netto(salary, rate=0.2):
    if not isinstance(salary, int | float):
        raise TypeError('Salary must be a Number')
    if not isinstance(rate, int | float):
        raise TypeError('Rate must be a Number')

    if salary < 0:
        raise ValueError('Salary cannot be negative')
    if not 0 <= rate <= 1:
        raise ValueError('Rate must be between 0 and 1')

    netto = salary * (1 - rate)
    return netto


try:
    salary = 1000
    rate = 1.2
    res = salary_netto(salary, rate)
    logging.info(f'Salary: {salary:.2f}; rate: {rate:.2f}; netto: {res:.2f}')
    print(res)
except Exception as e:
    logging.error(e)