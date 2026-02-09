# x = [0] * 10
# print(x)
#
# x[0] = 100
# print(x)
#
# x = [[1, 2, 3]] * 10
# print(x)
#
# x[0][0] = 100
# print(x)

# # проверяет, состоит ли строка только из букв (без пробелов и других символов)
# print("Hello".isalpha())
# # проверяет, состоит ли строка только из цифр
# print("12345.1".isdigit())
# print("1.2".isnumeric())
#
# # проверяет, состоит ли строка только из букв и цифр (без пробелов и специальных символов)
# print("Hello123".isalnum())
# # проверяет, состоит ли строка только из пробельных символов (пробелы, табуляция и т.д.)
# print(" \t\n".isspace())
# # проверяет, находятся ли все символы строки в нижнем регистре
# print("Hello".islower())
# # проверяет, состоит ли строка только из символов ASCII
# print("Привет".isascii())
# # проверяет, все ли символы в строке являются печатаемыми, например без символа перевода строки
# print("Hello\nWorld".isprintable())
# # проверяет, является ли строка допустимым идентификатором (названием переменной)
# print("1variable".isidentifier())

# # проверяет, находятся ли все символы строки в верхнем регистре
# print("HELLO".isupper())
# # проверяет, начинается ли каждое слово в строке с заглавной буквы
# print("Hello world".istitle())
# # проверяет, начинается ли строка с указанной подстроки
# print("Hello world".startswith("Hello"))
# # проверяет, заканчивается ли строка указанной подстрокой
# print("Hello world!".endswith("world"))


# x = 'http://example.com'
# print(x[:4] == 'http') # BAD
# print(x.startswith('http'))
#
#
# print(x[-4:] == '.com') # BAD
# print(x.endswith('.com'))


# x = 'banananana'
#
# index_start = x.find('na', 3)
# print(index_start)
#
# index_start = x.rfind('na')
# print(index_start)

# index_end = index_start + len('na')
# print(index_end)
#
# print(x[index_start:index_end])
#
# x = x.replace(x[index_start:index_end], '*', count=1)
# print(x)


# x = 'bananananana'
#
# start = 0
# sub = 'nana'
# while True:
#     index = x.find(sub, start)
#     if index == -1:
#         break
#
#     print(index)
#     start = index + len(sub)



# x = 'Hello World'
# print(x.lower())
# print(x.casefold())
#
#
# x = "Straße"
# print(x.lower())
# print(x.casefold())
#
# print(x.lower() == x.casefold())
#
#
# text = 'Yes'.lower()
# if 'yes' == text.casefold():
#     print('Yes')


# text = "apple apple apple"
# new_text = text.replace("apple", "orange", 1)
# new_text = new_text.replace("apple", "banana", 1)
# print(new_text)


# text = 'Hello                       world!                       Python is'
# while '  ' in text:
#     text = text.replace('  ', ' ')
#
# print(text)

# import string
# text = "apple, banana: cherry"
#
# for item in string.punctuation:
#     text = text.replace(item, " ")
# res = text.split(' ')
# print(res)
#
# res = text.split()
# print(res)

#
# x = 'Hello,,,,,world'
# res = x.split(',')
# print(res)
#
#
# x = x.replace(',', ' ')
# res = x.split()
# print(res)

# x = ['aaa', 'bbb', 'ccc']
#
# res = ' '.join(x)
# print(res)


# number = input("Enter a number: ")
# res = '***'.join(number)
# print(res)

text = 'Hello                       world!                       Python is'
words = text.split()
text = ' '.join(words)
print(text)