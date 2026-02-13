# x = '     Pyt        hon          '
# x_strip = x.strip()
# x_lstrip = x.lstrip()
# x_rstrip = x.rstrip()
#
# print(x_strip)
# print(x_lstrip)
# print(x_rstrip)


# x = '****P*y*t*h*o*n****'
# res = x.strip('*')
# print(res)

# x = 'http://example.pt'
# res = x.lstrip('pth')
# print(res)


# x = 'http://example.pt'
# i = 0
# for item in x:
#     if item in 'pth':
#         i += 1
#     else:
#         break
#
# res = x[i:]




# x = 'Hellos Worlds'
# words = x.split()
# for item in words:
#     print(item.rstrip('s'))



x = ['aaa', 'bbb', 'ccc', 'ddd']
# VERY BAD
# y = ''
# for item in x:
#     y += item + ','
#
# print(y)
#
# y = ''
# for i in range(len(x) - 1):
#     y += x[i] + ','
# else:
#     y += x[-1]
# print(y)

# y = ''.join(x)
# print(y)
# 'http', 'https'
# 'htps'

# name = input('Enter your name: ')
# age = int(input('Enter your age: '))
# text = "My name is %s and I am %d years old." % (name, age)
# print(text)



# # Форматирование числа с плавающей точкой
# import math
# text = "The value of pi is approximately %.4f." % math.pi
# print(text)


# name = "Alice"
# age = 25
# text = f"My name is {name} and I am {age} years old."
# print(text)
#
# print(f"My name is {name} and I am {age} years old.")

# name, age = None, None
# pattern = f"My name is {name} and I am {age} years old."

# names = ['Alice', 'Bob', 'Carol']
# ages = [20, 24, 23]
#
# for i in range(len(names)):
#     name = names[i]
#     age = ages[i]
#     pattern = f"My name is {name} and I am {age} years old."
#     print(pattern)


# name, age = None, None
# pattern = "My name is {name} and I am {age} years old."
#
# names = ['Alice', 'Bob', 'Carol']
# ages = [20, 24, 23]
#
# for i in range(len(names)):
#     name = names[i]
#     age = ages[i]
#
#     print(pattern.format(name=name, age=age))


# name = "Charlie"
# age = 30
# text = f"""Info
# Name: {name}
# Age: {age}
# """
# print(text)


# large_number = 12356
#
# text_fstring = f"The number with thousand separators: {large_number:,}"
# print(text_fstring)

# f-строки
text_fstring = f"start_{'text':>10}_end"
print(text_fstring)


# f-строки
text_fstring = f"start_{'text':<10}_end"
print(text_fstring)

text = 'Bob'
# f-строки
text_fstring = f"start_{text:^9}_end{'hjghjg':>20}"
print(text_fstring)
