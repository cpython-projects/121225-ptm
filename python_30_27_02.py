# x = [1, 2, 3, 4]

# # Копирование ссылки на объект
# y = x
# y[0] = 100
#
# print(y)
# print(x)


# # View Copy
# y = x.copy()
# y[0] = 100
# print(y)
# print(x)
# print(id(x))
# print(id(y))
#
# y = x[:]
# y[0] = 100
# print(y)
# print(x)
# print(id(x))
# print(id(y))


# # Deep copy
# x = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# import copy
#
# y = copy.deepcopy(x)
# y[0][0] = 100
# print(y)
# print(x)
# x = 'Python'
# y = [x, x]
#
# y.remove(x)
#
# print(y)
# print(x)
#
#
# del y[0]
# print(x)
# print(y)
# del x

# salaries = [1000, 4000, 50000, 4000, 3444, 23333]
# taxes = []
# rate = 0.45
#
# for salary in salaries:
#     taxes.append(salary * rate)
#
# print(salaries)
# print(taxes)
#
#
# rate = 0.45
# salaries = [1000, 4000, 50000, 4000, 3444, 23333]
# taxes = [salary * rate for salary in salaries]
# print(salaries)
# print(taxes)


# numbers = [1, 4, 6, 7, 9]
# # Возведение каждого элемента numbers в квадрат
# squares = [n ** 2 for n in numbers]
# print(squares)
# print(numbers) # Изначальный список останется без изменений



# text = 'Python'
# stars = [f'*{item}*' for item in text]
# print(text)
# print(stars)


# import random
#
# res = []
# for i in range(20):
#     tmp = random.randint(1, 100)
#     res.append(tmp)
#
# print(res)
#
#
#
# res = [random.randint(1, 100) for _ in range(20)]
# print(res)




# # List comprehension
# words = ["hello", "world", "python"]
# uppercase_words = '\n'.join([word.upper() for word in words])
# print(uppercase_words)
#
# words = ["hello", "world", "python"]
# uppercase_words = []
# for word in words:
#     uppercase_words.append(word.upper())
# print(uppercase_words)


# words = ["Apple", "banana", "cherry", "date"]
# words_with_a = [word for word in words if 'a' in word or 'A' in word]
# print(words_with_a)



# salaries = [1000, 4000, 50000, 4000, 3444, 23333]
# taxes = [item * 0.1 if item < 4000 else item * 0.45 for item in salaries]
# print(taxes)
#
# print(f'{taxes[4]:.2f}')

# numbers = [2, 7, 5, 4, 1, 1, 7, 8]
# res = [-1 if item % 2 else item for item in numbers]
# print(res)

# words = ["hi", "apple", "banana", "cat", "blueberry", "on"]
# modified_words = []
# for word in words:
#     if len(word) > 5:
#         modified_words.append('long')
#     elif len(word) >= 3:
#         modified_words.append('medium')
#     else:
#         modified_words.append('short')
# print(modified_words)
#
#
# modified_words = ['long' if len(word) > 5 else ('medium' if len(word) >= 3 else 'short')
#                   for word in words]
# print(modified_words)

# Эквивалент с циклом for
# pairs = []
# for x in range(3):
#     for y in range(2):
#         pairs.append((x, y))
# print(pairs)
#
# pairs = [(x, y) for x in range(3) for y in range(2)]
# print(pairs)

# quantities = [2, 4, 1, 3, 1]
# prices = [20, 40, 11, 13, 21]

# x = list(zip(quantities, prices))
# print(x)

#
# total_cart = 0
#
# for price, quantity in zip(prices, quantities):
#     total_cart += quantity * price
#
# print(total_cart)

# names = ["Alice", "Bob", "Charlie"]
# ages = [25, 30, 35]
# cities = ['Hamburg', 'Berlin', 'Munich']
# combined = zip(names, ages, cities)
# print(list(combined))


# x = 'abcd'
# y = '1234'
#
# print(*zip(x, y))


# list1 = [1, 2, 3]
# list2 = ['a', 'b']
# result = zip(list1[1:], list2)
# print(list(result))




# stack = []
# # Добавление элементов в стек
# stack.append(1)
# stack.append(2)
# stack.append(3)
# stack.append(4)
# # Удаление последних элементов из стека
# print(stack.pop(0))
# print(stack.pop(0))
#
# print(stack)


# from collections import deque
# queue = deque()
# # Добавление элементов в очередь
# queue.append(1)
# queue.append(2)
# queue.append(3)
# queue.append(4)
# queue.append(5)
# # Удаление первых элементов из очереди
# print(queue.popleft())
# print(queue.popleft())
# print(queue.pop())
# # Текущая очередь
# print(queue)

#
# # Список строк
# words = ["orange", "mango", "apple", "banana", "kiwi", "cherry"]
# # Сортировка списка по длине строк
# sorted_words = sorted(words, key=len)
# for word in sorted_words:
#     print(f"{len(word)}: {word}")
# # слова с одинаковой длиной сохранят свой исходный порядок
#
# import string
#
# text = "My number is 1211-1111-1111 hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh"
#
# for digit in string.digits: # '0123456789'
#     text = text.replace(digit, '*')
#     print(id(text))


# data_list = [
#         "John 23 12345.678",
#         "Alice 30 200.50",
#         "Bob 35 15000.3",
#         "Charlie 40 500.75"
# ]
#
# for item in data_list:
#     name, age, balance = item.split()
#     text = f"""Имя: {name.ljust(10)}| Возраст: {age.ljust(3)}| Баланс: {float(balance):>10.2f}"""
#     print(text)
#
#
# numbers = [1245.4435, -302.1403, 87459.99, -520.8265, 1450.001]
# print(numbers)
# summa = 0
# for num in numbers:
#     if num > 0:
#         summa += num
#
# print("${:,.2f}".format(summa))


x = [1, -2, -3, -4, 5, 6, 7, 8, 9]

# i = 0
# while i < len(x):
#     if x[i] < 0:
#         x.remove(x[i])
#     else:
#         i += 1
# print(x)


# for item in x:
#     if item < 0:
#         x.remove(item)

# y = x[:]
# for item in y:
#     if item < 0:
#         x.remove(item)


# y = [item for item in x if item >= 0]
# print(y)


# x = [1, -2, -3, -4, 5, 6, 7, 8, 9]
# for item in reversed(x):
#     if item < 0:
#         x.remove(item)
# print(x)

# # Число в конце
# strings = ["apple23", "ban1ana45", "12cherry", "grape3", "blue23berry"]
# dig_string = []
# for item in strings:
#     item = item.rstrip('0123456789')
#     if item.isalpha():
#         dig_string.append(item)
#
# print("Строки с цифрами только в конце: ", dig_string)



weights = [23, 3, 4, 9, 8, 2, 5]
box_weight = 10

weights.sort(reverse=True)
boxes = []

while weights[0] > box_weight:
    del weights[0]

while weights:
    current_box = []

    for item in weights[:]:
        if sum(current_box) + item <= box_weight:
            current_box.append(item)
            weights.remove(item)
    boxes.append(current_box)
print(boxes)





