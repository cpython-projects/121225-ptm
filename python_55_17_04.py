# def div(a, b):
#     return a / b
#
#
# def netto_salary(salary: int | float, rate: int | float) -> float:
#     """
#     Returns ....
#
#     :param salary:
#     :param rate:
#     :return:
#     """
#     if not isinstance(salary, float | int):
#         raise TypeError('Salary must be a float or int.')
#     if not isinstance(rate, float | int):
#         raise TypeError('Rate must be a float or int.')
#     if not 0 <= rate <= 1:
#         raise ValueError('Rate must be between 0 and 1.')
#
#     return salary * (1 - rate)
#
#
# try:
#     print(netto_salary('1000', -4))
# except Exception as e:
#     print(e)
# import os
#
# def total_profit(url):
#     try:
#         import pandas as pd
#     except ImportError:
#         os.system('pip install pandas')
#     import pandas as pd
#     df = pd.read_csv(url)
#     res = df['Quantity'] * df['UnitPrice']
#     return res.sum()
#
#
# print(total_profit('https://raw.githubusercontent.com/cpython-projects/python_da_06_11_25/refs/heads/main/orders_project_01.csv'))


# import sys
# import os
# import argparse
# print(sys.argv)
#
# print(os.getcwd(), sys.argv[0])

# import argparse
#
# # создаём парсер
# parser = argparse.ArgumentParser()
#
# # добавляем аргумент
# parser.add_argument("--name", help="Ваше имя")
#
# # читаем аргументы
# args = parser.parse_args()
#
# # используем аргумент
# if args.name:
#     print(f"Привет, {args.name}!")
# else:
#     print("Привет, незнакомец!")

# import sys
# sys.exit(0)
# sys.exit(1)


import itertools

# # db_1
# products = ['banana', 'apple', 'orange', 'pear']
# counter = itertools.count(10, 10)
# products_db_1 = {next(counter): product for product in products }
# print(products_db_1)
#
#
# # db_2
# products = ['tomatos', 'potates', 'kukumbers', 'cabage']
# # counter = itertools.count(1000, 10)
# products_db_2 = {next(counter): product for product in products }
# print(products_db_2)


#
# log_app = open('app_server.log', 'r', encoding='utf-8')
# log_web = open('web_server.log', 'r', encoding='utf-8')
#
#
# log_app_gen = (line.strip() for line in log_app if 'ERROR' in line)
# log_app_web = (line.strip() for line in log_web if 'ERROR' in line)
#
#
# chain = itertools.chain(log_app_gen, log_app_web)
#
# for line in chain:
#     print(line)



# logs = ['app_server.log', 'web_server.log']
# logs_files = (open(name, 'r', encoding='utf-8') for name in logs)
# log_gen = (line.strip() for log in logs_files for line in log if 'ERROR' in line)
#
# for line in log_gen:
#     print(line)


# db_users    = [{"id": 1, "name": "Alice"}, {"id": 2, "name": "Kate"}]
# cache_users = [{"id": 101, "name": "Bob"}, {"id": 102, "name": "Davit"}]
# api_users   = [{"id": 1001, "name": "Carol"}, {"id": 1002, "name": "Tom"}]
#
#
# # for item in db_users:
# #     print(item)
# #
# # for item in api_users:
# #     print(item)
# #
# # for item in cache_users:
# #     print(item)
#
#
# chain = itertools.chain(db_users, cache_users, api_users)
# for user in chain:
#     print(user)

#
# nested = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
# flat = list(itertools.chain.from_iterable(nested))
# print(flat)

# pip install colorama
# from colorama import Fore, Back, Style, init
#
# init(autoreset=True)
#
# rows = ["Alice 25", "Bob 30", "Carol 22", "Dan 28"]
#
# styles = itertools.cycle([
#     (Back.YELLOW, Fore.BLACK),
#     (Back.BLACK, Fore.WHITE)
# ])
#
# for user, (bg, fn) in zip(rows, styles):
#     print(f'{bg}{fn} {user:^15} {Style.RESET_ALL}')


# digits = '0123456789'
# pins = itertools.product(digits, repeat=4)
# pins_20 = (pin for pin in pins if sum(map(int, pin)) == 20)
# print(*pins_20, sep='\n')
# print('-' * 20)
# print(*pins_20, sep='\n')

# pins = []
# for i in range(10000):
#     pin = str(i)
#     if sum(map(int, pin)) == 20:
#         pins.append(pin)
#
# print(pins)


# x = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# y = itertools.cycle(['even', 'odd'])
#
# print(*zip(x, y), sep='\n')