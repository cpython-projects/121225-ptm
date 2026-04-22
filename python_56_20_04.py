# def my_range(start, stop, step):
#     result = []
#
#     while start < stop:
#         result.append(start)
#         start += step
#
#     return result
#
#
# def my_range_gen(start, stop, step):
#     print('Hello')
#     while start < stop:
#         yield start
#         start += step
#     print('End')




# print(my_range(1, 10, 2))
# print(my_range(10, 100, 20))


# f = my_range_gen(1, 10, 2)
# res = next(f)
# print(res)
# res = next(f)
# print(res)
# res = next(f)
# print(res)

# f = range(1, 10, 2)
# f = f.__iter__()
# print(next(f))
# print(next(f))
# print(next(f))
#
# for i in f:
#     print(i)


# for i in range(10):
#     ...
#
#
# for i in range(20):
#     ...

# x = range(10)
# print(type(x))

# for i in my_range_gen(1, 10, 2):
#     print(i)

# def generate_values():
#     print("Начало работы")
#     yield 1 # Приостанавливаем выполнение и возвращаем 1
#     print("Продолжение работы")
#     yield 2 # Приостанавливаем выполнение и возвращаем 2
#     print("Продолжение работы")
#     yield 3  # Приостанавливаем выполнение и возвращаем 2
#     print("Завершение работы")



# for i in generate_values():
#     print(i)

# try:
#     gen_func = generate_values()
#     print(next(gen_func))
#     print(next(gen_func))
#     print(next(gen_func))
#     print(next(gen_func))
# except StopIteration:
#     pass
#



# def loop_inf():
#     i = 0
#     while True:
#         yield i
#         i += 1


#
# for i in loop_inf():
#     print(i)



# x = ['Alice', 'Bob', 'Charlie']
# res = list(zip(x, loop_inf()))
# print(res)


# def loop_inf():
#     i = 0
#     while True:
#         yield i
#         i += 1
#
#
# f = loop_inf()
# for i in f:
#     if i == 10:
#         break
#     print(i)
#
# print('-' * 20)
#
# for i in f:
#     if i == 20:
#         break
#     print(i)



# def loop_inf():
#     i = 0
#     while True:
#         yield i
#         i += 1
#
#
# f = loop_inf()
# for i in f:
#     print(i)
#     if i == 10:
#         f.close()
#
# print(f)
# for i in f:
#     print(i)
#     if i == 10:
#         f.close()


#
# def sensor_data(data):
#     for value in data:
#         yield value
#
# numbers = [10, 20, 30, 40, 50]
# gen = sensor_data(numbers)
#
# for element in gen:
#     print("Получено значение:", element)
#     # Завершаем генератор, когда получено нужное значение
#     if element >= 30:
#         print("Значение найдено, закрываем генератор.")
#         gen.close()
#
# # next(gen) # Вызовет ошибку




# def gen_letter(sentence):
#     # for letter in sentence:
#     #     yield letter
#
#     yield from sentence
#
#
# for i in gen_letter('Hello'):
#     print(i)

#
# # Умеет работать с одним объектом
# def process_values(data):
#     for value in data:
#         yield value * 2
#
#
# # Собирает несколько объектов
# def main_generator(*sequences):
#     # Делегирует обработку каждого объекта вспомогательному генератору
#     for seq in sequences:
#         # yield from process_values(seq)
#         for item in process_values(seq):
#             yield item
#
#
# # Используем несколько источников данных
# data1 = [1, 2, 3]
# data2 = [10, 15]
# for result in main_generator(data1, data2):
#     print(result)
#
# def get_users_gen(*users_list):
#     for users in users_list:
#         yield from users
#
#
# bd_users = ['user_001', 'user_002', 'user_003', 'user_004']
# tg_users = ['tg_001', 'tg_002', 'tg_003', 'tg_004']
#
#
# for user in get_users_gen(bd_users, tg_users):
#     print(user)



# def get_data_from_file(filename):
#     with open(filename, 'r') as f:
#         for line in f:
#             yield line.strip().lower()
#
#
# def get_data_from_all_sources(*files_list):
#     for filename in files_list:
#         yield from get_data_from_file(filename)
#
#
# for user in get_data_from_all_sources('users_db', 'users_tg'):
#     print(user)


# def numbers_5(data):
#     for i in data:
#         if i % 5 == 0:
#             yield i

def numbers_5(data):
    yield from (i for i in data if i % 5 == 0)



numbers = [12, 15, 33, 40, 55, 62, 75, 83, 90]
print(numbers_5)
# numbers_5 = list(numbers_5(numbers))

print(*numbers_5(numbers))

# numbers_5 = (i for i in numbers if i % 5 == 0)
# print(*numbers_5)
#
# numbers_5 = (i for i in numbers if i % 5 == 0)
# print(*numbers_5)










