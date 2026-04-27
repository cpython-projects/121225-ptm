import re

# text = "Python 3.9, Java 17, C++ 14, 56 _6"

#
# for i in '.,:':
#     text = text.replace(i, ' ')
# text = text.split()
# res = []
#
# for word in text:
#     try:
#         res.append(int(word))
#     except Exception as e:
#         pass
#
# print(res)

# numbers = re.findall(r"\d+", text)
# print(numbers)

# numbers = re.findall(r"\d\w\s\w\d", text)
# print(numbers)


# text = "\tPython 3.12, Java 17, C++ 14!\n1234"

# print("Цифры:", re.findall(r"\d", text))

# print("Двузначные цифры:", re.findall(r"\d", text))
# print("НЕ цифры:", ''.join(re.findall(r"\D", text)))
# print("Буквы, цифры, _:", re.findall(r"\w", text))
# print("НЕ буквы, цифры, _:", re.findall(r"\W", text))
# print("Пробелы:", re.findall(r"\s", text))
# print("НЕ пробелы:", re.findall(r"\S", text))
# print("Все символы (кроме \\n):", re.findall(r".", text))

# import re
# pattern = r"\d" # ОШИБКА: \d будет воспринято как управляющий символ
# print(re.findall(pattern, "Price: 123"))

# text = 'Current time is 12:74'
#
# print(re.findall(r':[0-5][0-9]', text))


# text = "Report, report, report2, report10"

# print("Буквы r или R в слове:", re.findall(r"[rR]eport", text))
# print("Все цифры:", re.findall(r"[0-9]", text))
# print("Заглавные буквы:", re.findall(r"[A-Z]", text))
# print("Строчные буквы:", re.findall(r"[a-z]", text))
# print("Все буквы:", re.findall(r"[a-zA-Z]", text))
# print("Все, кроме цифр:", ''.join(re.findall(r"[^0-9]", text)))

# text = 'My credit card number is 1234-5678-1234-5678'
#
# pattern = r'\d{4}-\d{4}-\d{4}-\d{4}'
#
# print(re.search(pattern, text).group(0))


# text = """
# Orders: ID123, ID4567, ID89
# Numbers: 123-45-67, 321-45-67
# Prices: 100$, 199.50$, 99.99€, 0.49€, .99€
# File names: report.txt, report2.txt, report10.txt
# """

# print("Одна или более цифр:", re.findall(r"\d+", text))
# print("Телефонные номера (формата xxx-xx-xx):", re.findall(r"\d{3}-\d{2}-\d{2}", text))
# print("Цены (числа с десятичной точкой):", re.findall(r"\d*\.\d+", text))
# print("ID-коды:", re.findall(r"ID\d{2,}", text))
# print("Имена файлов 0+ цифр:", re.findall(r"report\d*.txt", text))
# print("Имена файлов 0/1 цифр:", re.findall(r"report\d?.txt", text))
# print("Имена файлов 1/2 цифр:", re.findall(r"report\d{1,2}.txt", text))

# text = "<div>Hello</div><div>World</div>"
# greedy = re.findall(r"<.*>", text) # Жадный

# lazy = re.findall(r"<.*?>", text) # Ленивый

# print(greedy)
# print(lazy)


# text = "Hello world! Welcome to world"

# print("Слово в начале строки:", re.findall(r"\w+", text))
# print("Слово в конце строки:", re.findall(r"\w+$", text))

# text = '1234-1234-1234-1234'
# print(re.findall(r"^\d{4}-\d{4}-\d{4}-\d{4}$", text))

# print(int('0000000011111111'))


# text2 = "category wildcat education _cat_ catalog"
# print("Слова с 'cat' внутри:", re.findall(r"\w+cat\w+", text2))
# print("Слова с 'cat' в начале слов:", re.findall(r"\bcat\w*", text2))
# print("Слова с 'cat' в конце слов:", re.findall(r"\w*cat\b", text2))
# text3 = "X123X 234 4567X X999"
# print("Числа внутри строк:", re.findall(r"\B\d+\B", text3))


# text = "Meeting on 2024-05-10 or 10/05/2024 at 14:30"
# # Найдём даты в формате YYYY-MM-DD или DD/MM/YYYY
# print("Даты:", re.findall(r"(\d{4}-\d{2}-\d{2}|\d{2}/\d{2}/\d{4})", text))

# text = "Order ID: 1234, Invoice No: 67890"
#
# match = re.search(r"Order ID: (\d+), Invoice No: (\d+)", text)
#
# print(type(match))
#
# if match:
#     id_order, invoice_no = match.groups()
#
#     print("ID заказа:", match.group(1))
#     print("Номер счёта:", match.group(2))


# def get_taxes(salary, rate=0.4):
#     return salary * rate


# x = [1, 2, 3, 4, 5]
# y = [23, 4, 5, 6, 7]
#
# import itertools
#
#
# for item in itertools.chain(x, y):
#     print(item)

import json
from datetime import datetime

with open("grades.json", "r", encoding="utf-8") as file:
    json_into_dict = json.load(file)
    print(json_into_dict)

students = {}

for student in json_into_dict:
    student_date = datetime.strptime(student["date"], "%d-%m-%Y")
    if 1 <= student_date.month <= 3:
        quartal = "q2"
    if 4 <= student_date.month <= 5:
        quartal = "q3"
    if 6 <= student_date.month <= 8:
        continue
    if 9 <= student_date.month <= 12:
        quartal = "q1"
    stud_name = students.setdefault(student["name"], {})
    stud_subj = stud_name.setdefault(student["subject"], {})
    stud_subj[quartal] = student["grade"]

with open("stud_res.json", "w", encoding="utf-8") as res:
    json.dump(students, res, indent=4)
