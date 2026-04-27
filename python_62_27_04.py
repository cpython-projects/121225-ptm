import re
text = "UAH 400, GEL 200, GBP 300, EUR600"
# Найдём суммы, не выделяя валюту


# res = re.search(r'USD (\d+), EUR (\d+), GBP (\d+)', text)
# if res:
#     print(res.groups())
#
#
# res = re.search(r'(?:USD|EUR|GBP) (\d+)', text)
# if res:
#     print(res.groups())


# res = re.findall(r'(?:USD|EUR|GBP) (\d+)', text)
# if res:
#     print(res)


# res = re.findall(r'(USD|EUR|GBP) (\d+)', text)
# if res:
#     print(res)


# text = "ID12345 is confirmed. ID23456 is confirmed"
# # Проверяем, начинается ли строка с "ID" + цифры
# match = re.match(r"ID\d+|trulala", text)
# if match:
#     print("Объект Match:", match)
#     print("Само совпадение:", match.group())
#     print("Диапазон совпадения:", match.span())
# else:
#     print("Нет совпадения.")
#
#
# text = "Order ID: 12345, Invoice No: 67890, Ref: ABC9876"
# # Найдём первое число в тексте
# match = re.search(r"^\d+", text)
# if match:
#     print("Объект Match:", match)
#     print("Само совпадение:", match.group())
#     print("Индекс начала:", match.start())
#     print("Индекс конца:", match.end())
#     print("Диапазон совпадения:", match.span())
# else:
#     print("Нет совпадения.")

#
# text = "Order ID: 12345, Invoice No: 67890, Ref: ABC9876"
# # Найдём все числа в тексте
# # matches = re.findall(r"\d+", text)
# # print(matches)
# matches = re.finditer(r"\d+", text)
# print(matches)
# for match in matches:
#     print("Объект Match:", match)
#     print("Само совпадение:", match.group())
#     print("Диапазон совпадения:", match.span())
#     print()

# text = """Python is popular. It is used in web development, data science,
# and automation. Many developers choose Python for its simplicity."""
#
# res = re.split(r'[\s,.]+', text)
# print(res)


# text = "apple,    banana , orange  ,grape"
# new_text = re.sub(r"\s*,\s*", ", ", text)
# print(new_text)


texts = [
"Order ID: 12345, Invoice No: 67890, Ref: ABC9876",
"Shipment ID: 54321, Tracking No: 98765, Customer Ref: XYZ123",
"Invoice 22222 processed successfully."
]
# Компилируем регулярное выражение для поиска числовых идентификаторов
number_pattern = re.compile(r"\d+")
print(number_pattern)

# Применяем шаблон к разным текстам
for text in texts:
    match = number_pattern.findall(text) # re.findall(r"\d+", text)
    if match:
        print(f"Совпадение в тексте: {match}")


