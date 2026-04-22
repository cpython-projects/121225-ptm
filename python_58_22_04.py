# import json
#
#
# with open('data.json') as file:
#     try:
#         data = json.load(file)
#     except json.decoder.JSONDecodeError:
#         print('Error in JSON')

# Генерация безопасных паролей"
# Программа должна сгенерировать все возможные пароли длиной 4 символа, соблюдая следующие условия:
# ● Пароль должен содержать хотя бы одну заглавную букву, одну строчную букву и одну цифру. +
# ● Символы не должны повторяться. +
# ● Соседние символы не могут быть расположены подряд в таблице символов.
# ● Все подходящие пароли записываются в файл valid_passwords.txt
#
# Данные:
# from string import ascii_lowercase,
# ascii_uppercase, digits
#
# Пример данных в файле:
# acA0
# acA1
# acA2
# acA3
# acA4
# acA5
# acA6
# acA7
# acA8

# import itertools
# import string
#
#
# def is_valid_4(password):
#     has_lower = any(char in string.ascii_lowercase for char in password)
#     has_upper = any(char in string.ascii_uppercase for char in password)
#     has_digit = any(char in string.digits for char in password)
#
#     if not (has_lower and has_upper and has_digit):
#         return False
#
#     if len(set(password)) != len(password):
#         return False
#
#     for i in range(len(password) - 1):
#         current_char = password[i]
#         next_char = password[i+1]
#
#         if abs(ord(current_char) - ord(next_char)) == 1:
#             return False
#
#     return True
#
#
# def write_passwords_to_file(file_name, alphabet, is_valid, k=4):
#     with open(file_name, 'w') as f:
#         for password in itertools.permutations(alphabet, k):
#             if is_valid(password):
#                 password = "".join(password)
#                 f.write(f'{password}\n')
#
#
# if __name__ == '__main__':
#     all_chars = string.ascii_letters + string.digits
#     write_passwords_to_file('all_passwords.txt', all_chars, is_valid_4)


# import time
# import itertools
#
# def add_tasks(file_name):
#     with open(file_name, 'a', encoding='utf-8') as f:
#         while True:
#             ans = input('Enter a task: ').strip()
#
#             if ans.lower() == 'exit':
#                 break
#
#             f.write(f'{ans}\n')
#
#
# def task_generator(file_name, attempts=3):
#     for i in range(attempts):
#         try:
#             with open(file_name, 'r', encoding='utf-8') as f:
#                 for line in f:
#                     yield line.strip()
#
#                 while True:
#                     line = f.readline()
#                     if not line:
#                         time.sleep(1)
#                         continue
#
#                     yield line.strip()
#             break
#         except FileNotFoundError:
#             time.sleep(3)
#
#
#
# def add_task_to_employee(employees, file_name):
#     employees_cycle = itertools.cycle(employees)
#     tasks = task_generator(file_name)
#
#     for task in tasks:
#         user = next(employees_cycle)
#         yield (user, task)
#
#
# if __name__ == '__main__':
#     # add_tasks('tasks.txt')
#
#     employees = ["Alice", "Bob", "Charlie"]
#     for employee, task in add_task_to_employee(employees, "tasks.txt"):
#         print(f'{employee}: {task}')
#


# with open('tasks.txt') as f:
#     f.seek(0, 2)
#     while True:
#         line = f.readline()
#         if not line:
#             continue
#         print(line)
#


from datetime import datetime

# date1 = datetime(2024, 2, 28)
# date2 = datetime(2024, 3, 5)
# difference = date2 - date1
#
# print(type(difference))
#
# print(difference.days)
#
# if difference.days == 5:
#     print("YES")
#
# print(difference.total_seconds())

# from datetime import timedelta
#
# start_date = datetime(2026, 4, 22)
# end_date = start_date + timedelta(weeks=2, days=2, hours=2)
#
# print(start_date, end_date, sep='\n')


import dateutil
dates = [
    '2026-04-22',
    '2026/04/22',
    '22 Apr 2026',
    '22 April 2026',
    'April 22, 2026',
    'trulala',
    'april 22, 26',
]

for date in dates:
    try:
        res = dateutil.parser.parse(date)
        print(type(res))
        print(res)
        print('*' * 20)
    except Exception as e:
        print(e)



