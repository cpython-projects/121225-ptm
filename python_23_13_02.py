text = "Python"

# ljust(): выравнивание по левому краю
# print(text.ljust(15))
# print(text.ljust(15, '-'))
#
# # rjust(): выравнивание по правому краю
# print(text.rjust(15))
# print(text.rjust(15, '-'))
#
# # center(): выравнивание по центру
# print(text.center(15))
#
# x = text.center(15).center(25, '\n')
# print(x)


# sym = input("Введите символ: ")
# code = ord(sym)
# print("Код Unicode:", code)
# print("ASCII символ:", code < 128)

# s = input("Введите строку: ")
# start = int(input("Введите начальный индекс: "))
# end = int(input("Введите конечный индекс: "))
#
# if start < 0 or end < 0 or start >= end:
#     print("Введите значения больше или равно 0 и start < end")
# else:
#     substring = s[start:end]
#     substring += '_' * (end - len(s))
#     print("Подстрока:", substring)
#


# a = ord('a')
# print('ASCII символ:', ord(a) <= 127)



# a = 12

# if a > 20:
#     res = True
# else:
#     res = False

# res = a > 20




# while len(x := input("Введите символ:").strip()) != 1:
#     print("Пришлите Один символ!")
#
# print(f"Код Unicode: {ord(x)}")
# print(f"ASCII символ: {ord(x) <= 127}")




# while not (name := input("Enter your name: ")):
#     print('Error')
#
# print(f"Hello {name}")


# text3 = input("Введите строку: ")
# x = text3[::-1]
# i = 0
# alltext = ""
# while i < len(x):
#     if x[i] not in "0123456789":
#         alltext += x[i]
#     i += 1
# print(f"Результат: {alltext}")

# print("\n4. Инвертирование строки без цифр")
# string = "n52uFs6Inoh67ty8P"
# i = len(string)
# parts = []
# while i > 0:
#     i -= 1
#     if not string[i].isdigit():
#         parts += string[i]
# print("".join(parts))


# user_input_str = input("Введите строку: ")
# user_input_char = input('Введите символ: ')
# counter = 0
# id_char = 0
# while id_char < len(user_input_str):
#    if user_input_str[id_char] == user_input_char:
#        counter += 1
#    id_char += 1
# print(f'Символ o встречается {counter} раз(а).')


# user_input = input('Введите строку: ')
# result = ''
# index_id = 0
#
# while len(user_input) > index_id:
#     if not user_input[index_id].isdigit():
#         result += user_input[index_id]
#     index_id += 1
#
# print(result[::-1])


# newstring = input("Введите строку: ")
# checksym = input("Введите символ: ")
#
# length = len(newstring)
# right = length - 1
# buffer = 0
#
# while length:
#     if newstring[right] == checksym:
#         buffer = buffer + 1
#     right = right - 1
#     length = length - 1
#
# is_checksym = buffer > 0
#
# print(f"Символ {checksym} встречается? {"Да" if is_checksym == True else "Нет"}")
# if buffer > 0:
#     print(f"Символ {checksym} встречается {buffer} раз{"(а)" if buffer > 1 else ""}.")


# num = int(input("Введите число: "))
# s = ''
# for i in range(1, num + 1):
#
#     # s += (i != 1) * ' ' + str(i)
#
#     if i != 1:
#         s += ' '
#     s += str(i)
#
#     # if i == 1:
#     #     s += str(i)
#     # else:
#     #     s += " " + str(i)
#     print(s)


# # Удаление всех повторяющихся символов
# text = input("Введите строку: ")
# new_s = ''
# for char in text:
#     if char not in new_s:
#         new_s += char
#
# print("Результат: ", new_s)



# text = input('Введите строку: ')
#
# for i in range(len(text)):
#     if text[i] not in text[:i]:
#         print(text[i], end ="")



# text = input("Введите строку:")
#
# for i in range(len(text)):
#     for j in range(i):
#         if text[i] == text[j]:
#             break
#     else:
#         print(text[i], end="")
#
# user_input = int(input("Введите число: "))
#
# for i in range(1,user_input + 1):
#     print()
#     for j in range(1,i + 1):
#         print(j, end ='  ')


# string = input("Введите строку: ")
# buffer = ""
#
# for i in range(len(string)):
#     if string[i] not in buffer:
#         print(string[i], end="")
#         buffer = buffer + string[i]


#
# x = [1, 2, 3, 4, 5]
#
# for i in range(len(x)):
#     del x[i]


# numbers = [1, 3, 6, 9, 10, 12, 15, 19, 20]
# print(numbers)
# num = 3
# for i in numbers:
#     if not i % num:
#         numbers.remove(i)
# print(numbers)

# num = int(input("give me your number >>> "))
# # o, O, l, I
# for i in range(1, num + 1):
#
#     for n in range(1, i + 1):
#         print(n, end=" ")
#
#     print()

# numbers = [4, 9, 1, 7, 2, 5, 0, 3, 7, 1, 3]
#
# for i in range(len(numbers)):
#     if numbers[i] % 2:
#         numbers[i] = numbers[i] ** 2
#
# print(numbers)



# input_value = int(input("Введите стоимость товара:"))
#
# face_value = [50,10,5,2,1]
# count = 0
#
# for i in range(len(face_value)):
#     # while input_value >= face_value[i]:
#     #     input_value -= face_value[i]
#     #     count += 1
#
#     # //, %
#     print(f"Внесите монеты номиналом {face_value[i]}: {count}")
#     count = 0
#

# print(len(range(10, 30)))
# print(len([1, 2, 3, 4]))
# print(len([1, 2, 3, 4]))

