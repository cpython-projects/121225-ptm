import json

# data = {
#     "name": "Alice",
#     "age": 25,
#     "is_student": False
# }
#
# json_str = json.dumps(data)
# print(json_str)
#
#
# with open('dump.json', 'w') as file:
#     json.dump(data, file)
#
#
# import requests
#
# response = requests.get('https://jsonplaceholder.typicode.com/users')
# data = response.text
# data = json.loads(data)
# print(data)


import json
# json_object = '{"name": "Alice", "age": 25, "is_student": false}'
# json_objects = '[{"name": "Alice", "age": 25, "is_student": false}, {"name": "Bob", "age": 20, "is_student": true}]'
#
#
# res = json.loads(json_object)
# print(res)
#
# res = json.loads(json_objects)
# print(res)

# with open('dump.json') as file:
#     res = json.load(file)
#     print(res)


# json_object = {"name": "Alice", "age": 25, "is_student": False}
# print(json.dumps(json_object))


import json
from json import JSONDecodeError

# data = {
#     "dict_example": {"key": "value"},
#     "list_example": ["apple", "banana"],
#     "tuple_example": ("apple", "banana"),
#     "string_example": "Hello",
#     "int_example": 42,
#     "float_example": 3.14,
#     "bool_example_true": True,
#     "bool_example_false": False,
#     "none_example": None
# }
# # Запись в файл data.json
# with open("data.json", "w", encoding="utf-8") as file:
#     json.dump(data, file)



# # Чтение данных обратно в Python
# with open("data.json", "r", encoding="utf-8") as file:
#     loaded_data = json.load(file)
#
#
# for i in loaded_data:
#     print(i, loaded_data[i])



# data = {
#     "dict_example": {"key": "value"},
#     "list_example": ["apple", "banana"],
#     "tuple_example": ("apple", "banana"),
#     "string_example": "Hello",
#     "int_example": 42,
#     "float_example": 3.14,
#     "bool_example_true": True,
#     "bool_example_false": False,
#     "none_example": None,
#     "город": "Берлин"
# }
# # Запись в файл data.json
# with open("data.json", "w", encoding="utf-8") as file:
#     json.dump(data, file, indent=4, ensure_ascii=True, sort_keys=True)


# with open('data.json', 'r') as f:
#     try:
#         res = json.load(f)
#     except JSONDecodeError:
#         res = {'name': 'Unonym', 'age': None}
#
#     print(res)


from datetime import datetime

curr_date = datetime.now()
print(type(curr_date))

print(curr_date.hour)
print(curr_date.minute)
print(curr_date.second)
print(curr_date.microsecond)


print(curr_date.year)
print(curr_date.month)
print(curr_date.day)


print(curr_date.weekday())

res = curr_date.strftime("%d/%m/%Y")
print(res)
print(type(res))

print(curr_date.strftime("%I:%M %p")) # 02:30 PM (12-часовой формат)
print(curr_date.strftime("%A, %B %d, %Y")) # Friday, February 28, 2025


date_string = "28|02|2025" # Дата в виде строки
date_obj = datetime.strptime(date_string, "%d|%m|%Y")
print(date_obj)








