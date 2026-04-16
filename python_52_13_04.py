# Как писать не надо!!!!!!!!!
# def div(a, b) -> float | str:
#     try:
#         return a / b
#     except Exception:
#         return 'Error'
#
#
# res = div(1, '2')
# res = res * 5
#
# print(res)


# file = open('test.txt', 'w', encoding='utf-8')
# print(file)
# print(type(file))
# file.write('Hello world!')
# file.close()


# file = open('test.txt', 'w', encoding='utf-8')
# print('Hello', file=file)
# print('World', file=file)
# file.close()
#
#
# with open('test.txt', 'r', encoding='utf-8') as file:
#     for line in file:
#         print(line)

#
# with open('test.txt', 'r', encoding='utf-8') as file:
#     # Самый плохой вариант чтения файла
#     # data = file.read()
#     # print(data)
#
#     # Самый плохой вариант чтения файла
#     # data = file.readlines()
#     # print(data)
#
#     # while line := file.readline():
#     #     print(line)
#
#     # while data := file.read(5):
#     #     print(data)
#
#     # while True:
#     #     data = file.read(5)
#     #     if not data:
#     #         break
#     #     print(data)
#     #
#     # while data := file.read(5):
#     #     print(data)
#
#     for line in file:
#         print(line.strip())
#
#
# with open('test_1.txt', 'w', encoding='utf-8') as file:
#     file.write('1\n')
#     file.write('2\n')
#     file.write('3\n')
#
#     data = ['Hello\n', 'world\n']
#     file.writelines(data)
#     file.writelines('\n'.join('Hello'))



# with open("test_1.txt", "a", encoding="utf-8") as file:
#     file.write("\nДополнительная строка\n")

# with open("test_1.txt", "r+", encoding="utf-8") as file:
#     content = file.read() # Читаем текущие данные
#     print(content)
#     file.write("\nДобавленный текст") # Записываем новые данные
#
#
# f_input = open("test.txt", "r", encoding="utf-8")
# f_output = open("test_2.txt", "w", encoding="utf-8")
#
# for line in f_input:
#     f_output.write(line.upper())
#
# f_output.close()
# f_input.close()


with (open("test.txt", "r", encoding="utf-8") as f_input,
      open("test_2.txt", "w", encoding="utf-8") as f_output):
    for line in f_input:
        f_output.write(line.upper())