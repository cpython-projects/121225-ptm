fruits = ["apple", "banana", "cherry"]

# print(enumerate(fruits))
#
# x = list(enumerate(fruits))
# print(x)
#
# x = tuple(enumerate(fruits))
# print(x)
#
# for index, fruit in enumerate(fruits):
#     print(f"{index}: {fruit}")


# numbers = [10, 20, 15, 30, 25, 35]
#
# for index, value in enumerate(numbers[:-1]):
#     if value > numbers[index + 1]:
#         print(f"{value} больше, чем {numbers[index + 1]}")
#
#
# for i in range(len(numbers) - 1):
#     if numbers[i] > numbers[i + 1]:
#         print(f"{numbers[i]} больше, чем {numbers[i + 1]}")




# languages = ("Python", "Java", "C++")
# for title, counter in enumerate(languages, start=1):
#     print(title, counter)


# x = (1, 2, 3, 4, 5, 2, 3, 4)
# if 2 in x:
#     print(x.index(2))



# for item in x:
#     if x.count(item) == 1:
#         print(item)


# x = (1, 2, 3, 4, 5, 2, 3, 4)
#
# start = 0
# while True:
#     try:
#         res = x.index(2, start)
#         print(res)
#         start = res + 1
#     except ValueError:
#         break



# x = (1, 2, 3, 4, 5, 2, 3, 4)
# counter = x.count(2)
# start = 0
# while counter > 0:
#     res = x.index(2, start)
#     print(res)
#     start = res + 1
#     counter -= 1


# numbers = [1, 2, 3]
# numbers.append(40)
# print(numbers)
#
# numbers.append([5, 6])
# print(numbers)


# numbers = [1, 2, 3]
# numbers.append('Python')
# print(numbers)

# numbers.extend('Python')
# print(numbers)


x = [10, 20, 30]
y = [30, 40, 50]

# for item in y:
#     x.append(item)

# x.extend(y)
# print(x)

# res = x + y
# print(res)
# print(x)
# print(y)


# fruits = ["apple", "banana"]
# fruits.insert(0, "blueberry")
# print(fruits)


# letters = ['a', 'b', 'c']
# letters.insert(-1, 'x')
# print(letters)


# letters = ['a', 'b', 'c']

# letters.insert(10, 'x')
# print(letters)

# # вставка элемента без указания индекса
# numbers = [1, 2, 3]
# numbers.insert(5)


# x = [10, 20, 30]
# print(id(x))
# x.clear()
# print(x)
# print(id(x))
# x = []
# print(x)
# print(id(x))

# x = [10, -3, -5, 60, 70, -100, 34.56, True, False]
#
# x.sort()
# print(x)
#
# x.sort(reverse=True)
# print(x)


# fruits = ['az', 'xz', "apple", "cherry", "banana"]
# fruits.sort()
# print(fruits)
#
# fruits.sort(key=len)
# print(fruits)

#
# tuples = [(3, 6), (1, 7, 9), (12, 5), (1, 3, 7)]
# tuples.sort(key=min)
# print(tuples)



# x = [12, -34, 23, 12, 23, 90, 12]
# y = sorted(x)
#
# print(y)
# print(x)

# x = 'Python'
# y = sorted(x)
#
# print(y)
# print(x)


# x = [1, 2, 3, 4, 5, 6]
# x.reverse()
# print(x)
# print(x[::-1])

# print(reversed(x))

# x = [1, 2, 3, 4, 5, 6]
# for item in reversed(x):
#     print(item)
#
# print(x)


# x = [1, 2, 3, 4, 5, 6, 7]
# print(min(x))
# print(max(x))
# print(sum(x))


# words = ["apple", "banana", "kiwi", "grape"]
#
# res = max(words, key=len)
# print(res)


# data = [[1, 2, 3, 4], [1, 2, 3, 4, 5, 6, 7, 8], [1, 2], []]
# res = max(data, key=len)
# print(res)


# x = [1, 2, 3, 4, 56]

# y = list(reversed(x)) # x[::-1]
# print(x)
# print(y)

#
# for i in range(-1, -len(x) - 1, -1): # reversed(x)
#     print(x[i])