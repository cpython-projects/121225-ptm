# x = {'one': 1, 'bir': 1, 'один': 1}


#
# print(x[1])
# print(x['one'])

# for key in x:
#     print(key, x[key])
#
#
# print(x.items())
#
# for key, value in x.items():
#     print(key, value)

# my_dict = {"name": "Alice", "age": 30}
# my_dict.update({"age": 32, "country": "USA"})
# print(my_dict)
#
#
# my_dict.update([("name", "Bob"), ("email", "bob@example.com")])
# print(my_dict)
#
#
# x = [1, 2, 3, 4, 5]
# y = [6, 7, 8, 9, 10]
#
# my_dict.update(zip(x, y))
# print(my_dict)
#
#
# del my_dict[1]
# print(my_dict)
#
# if 100 in my_dict:
#     del my_dict[100]
#     print(my_dict)
#
#
# my_dict.clear()
# print(my_dict)

# my_dict = {"name": "Alice", "age": 30}
# print(my_dict.pop('name'))
# print(my_dict)

# print(my_dict.popitem())
# print(my_dict)

# test = input("text>>")
# stack = []

# brackets_valid = {
#     '(': ')',
#     '[': ']',
#     '{': '}'
# }
#
# is_valid = True
# for char in test:
#     if char in brackets_valid.keys():
#         stack.append(char)
#
#     elif char in brackets_valid.values():
#         if stack:
#             last_open_char = stack.pop()
#             if brackets_valid[last_open_char] != char:
#                 is_valid = False
#                 break
#
# if stack:
#     is_valid = False
#
# print(f'Is valid: {is_valid}')

x = {"a": 1, "b": 2, "c": 3}
y = {}

# for key in x:
#     y[x[key]] = key
# print(y)


# while x:
#     key, value = x.popitem()
#     y[value] = key
#
# print(y)
#
# for key, value in x.items():
#     y[value] = key

# print(*zip(x.values(), x.keys()))
# y = dict(zip(x.values(), x.keys()))
# print(y)


# Словарь сопоставлений
number_to_word = {1: "один", 2: "два", 3: "три"}
# Исходные данные
data = {"x": 1, "y": 2, "z": 3}


for key in data:
    data[key] = number_to_word[data[key]]


print(data)











