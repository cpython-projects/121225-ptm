# numbers = [4, 7, 3, 7, 8, 3, 4, 2, 7, 3, 8, 4]
# result = {number for number in set(numbers) if numbers.count(number) > 1}
# print(sorted(result, reverse=True))

# x = [1, 2, 3] * 10
# print(x)
# x = [[0] for _ in range(10)]
# print(x)
#
# keys = [1, 2, 3]
# default_value = "default"
# my_dict = dict.fromkeys(keys, default_value)
# print(my_dict)
#
#
# my_dict = dict.fromkeys(keys)
# print(my_dict)
#
# emp = ['Ivan', 'Petr']
# salaries = dict.fromkeys(emp, 0)
# print(salaries)

# emp = ['Ivan', 'Petr']
# salaries = dict.fromkeys(emp, [1, 2, 3])
# print(salaries)
#
#
# salaries['Ivan'].append(20)
# print(salaries)

# x = {1: 'one', 2: 'two', 3: 'three'}
# print(x[1])
# print(x.get(1))
#
#
# # print(x[4])
# print(x.get(4, 'Error'))



# # Получение значения по существующему ключу
# my_dict = {"age": 30}
# # print(my_dict.get("name")) # Alice
# print(my_dict.get("name", "Anonim")) # Alice


#
# x = [1, 200, -3, 4, 5, 6, 67, 43, 2, 2,4, 6, 7, 84,90]
#
# params = {
#     # 'min': 10,
#     # 'max': 100,
# }
# min_value = params.get('min', 0)
# max_value = params.get('max', max(x))
#
# res = [item for item in x if min_value <= item <= max_value]
# print(res)


# for key in params:
#     print(key, params[key])


# my_dict = {"name": "Alice", "age": 30}
# keys = my_dict.keys()
# print(type(keys))
# print(keys)
# # Изменение словаря
# my_dict["city"] = "New York"
# print(keys) # Значения обновляются
# # Преобразование представления в список
# keys_list = list(keys)
# my_dict["country"] = "USA"
# print(keys_list) # На списке изменения не отображаются

#
# my_dict = {"name": "Alice", "age": 30}
# values = my_dict.values()
# print(type(values))
# print(values)
# # Изменение словаря
# my_dict["age"] = 31
# print(values) # Значение обновляется
# # Преобразование представления в список
# values_list = list(values)
# my_dict["age"] = 32
# print(values_list) # Изменения на списке не отображаются


# my_dict = {"name": "Alice", "age": 30, "city": "New York"}
# i = 0
# for key, value in my_dict.items():
#     print(f"{key}: {value}")
#     my_dict[f'{key}{i}'] = f'{value}{i}'

#
# x = [1, 2, 3, 4, 5]
# for item in x:
#     print(item)
#     x.append(item)

# my_dict = {"name": "Alice", "age": 30, "city": "New York"}
# i = 0
# for key in my_dict:
#     value = my_dict[key]
#     print(f"{key}: {value}")
#     my_dict[f'{key}{i}'] = f'{value}{i}'


# x = 'aaaaaaaabbbbbbbb'
# buff = {}
# for item in set(x):
#     buff[item] = x.count(item)
#
# print(buff)


# students = [
#     {
#         'id': 1,
#         'first_name': 'Anton',
#         'last_name': 'Trofimov',
#         'address': {
#             'city': 'Berlin',
#             'street': 'Strret1',
#             'postal_code': '1111',
#         }
#     },
#     {
#         'id': 2,
#         'first_name': 'Vladymyr',
#         'last_name': 'Kolev',
#         'address': {
#             'city': 'Hamburg',
#             'street': 'Strret1',
#             'postal_code': '1111',
#         }
#     }
# ]
#
#
# for student in students:
#     id, first_name, last_name, address = student.values()
#     city, street, postal_code = address.values()
#     print()


# x = {1: 'one', 2: 'two', 3: 'three', 4: [1, 2, 3, 4]}

# y = x
#
# x[1] = 'bir'
# print(x)
# print(y)

# y = x.copy()
# x[1] = 'bir'
# x[4].append(100)
# print(x)
# print(y)

# import copy
# y = copy.deepcopy(x)
# x[1] = 'bir'
# x[4].append(100)
# print(x)
# print(y)


numbers = [1, 2, 3, 4]
squared_dict = {num: num ** 2 for num in numbers}
print(squared_dict)

original_dict = {"a": 5, "b": 2, "c": 0, "d": 3, "e": 0, "f": 3}
filtered_dict = {key: value for key, value in original_dict.items() if value > 0}
print(filtered_dict)

# [] - list, {item for ...} - set, {key: value for } - dict


numbers = [16, 18, 1, 6, 3, 2, 6, 2, 14, 3, 20, 15, 19, 4, 18, 15, 15, 4, 20, 18]

print({number for number in numbers if number % 3 == 0 or number % 5 == 0}) #20 не выводит

recipes = {
    ("flour", "egg", "milk"): "Pancakes",
    ("egg", "milk", "butter"): "Omelette",
    ("flour", "sugar", "butter"): "Cookies",
    ("flour", "egg", "butter", "sugar"): "Cake",
    ("milk", "flour", "egg"): "Waffles",
    ("butter", "milk", "egg"): "Scrambled Eggs",
    ("flour", "milk", "sugar", "butter"): "Sweet Bread"
}
_ingredients = "milk egg butter flour"   # input("Введите ингредиенты: ")
_ingredients = set(_ingredients.split())

new_recipes = []

for ingredients, name in recipes.items():
    if set(ingredients) <= _ingredients:
        new_recipes.append(name)

res = ', '.join(new_recipes) if new_recipes else 'No receipts'
print(res)