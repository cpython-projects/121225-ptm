# Hello


# *H*
# *e*
# *l*
# *l*
# *o*

# text = input('Enter a string: ')
#
# # for letter in text:
# #     print('*', letter, '*', sep='')
#
# text = 'Hello'
# start, stop = 1, 3
# print(text[start:stop])
#
#
# while start < stop:
#     print(text[start], end='')
#     start += 1

#
# text = "Hello"
# for letter in text:
#     print(letter,  end="*")
# #
# # print(1, 2, 3)
# # print(4, 5, 6)


# x = 'Hello world'
#
# for i in range(len(x)):
#     print(x[i])


# for i in range(5):
#     print(i)


# for i in range(3, 10):
#     print(i)

# for i in range(3, 10, 3):
#     print(i)


# for i in range(13, 1, -2):
#     print(i)


# 0, P
# 1, y
# ...
# x = 'Python'
# i = 0
# for item in x:
#     print(i, item, sep=', ')
#     i += 1

# x = 'Python'
# for i in range(len(x)): # 0, 1, 2, 3, 4, 5
#     print(i, end=' ')
#
#     if x[i] == 'h':
#         break
#
#     print(x[i], sep=', ')


# i = 0
# while i < len(x):
#     print(i, x[i], sep=', ')
#     i += 1


# for i, item in enumerate(x):
#     print(i, item, sep=', ')

# for letter in "Python":
#     if letter == "h":
#     # Останавливаем цикл
#     # если найден символ "h"
#         break
#     print(letter)


# for letter in "Python":
#     if letter == "h":
#         # Пропускаем букву "h" и
#         # продолжаем цикл
#         continue
#     print(letter)
# else:
#     print('Finish')

# counter = 0
# for i in "AB":
#     print('-' * 20)
#
#     for j in "12":
#         print(i, j)
#         counter += 1
#
# print(counter)


for hour in range(24):
    for minute in range(60):
        if minute < 10:
            print("Время (часов:минут): ", hour, ':0', minute, sep='')
        else:
            print("Время (часов:минут): ", hour, ':', minute, sep='')












