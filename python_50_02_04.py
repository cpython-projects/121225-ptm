import logging

#
# logging.basicConfig(
#     filename='app.log',
#     format="%(asctime)s - %(filename)s - %(lineno)d - %(levelname)s - %(message)s",
#     level=logging.DEBUG
# )
#
# logging.debug("Отладочное сообщение")
# logging.info("Информационное сообщение")
# logging.warning("Предупреждение!")
# logging.error("Ошибка!")
# logging.critical("Критическая ошибка!")



# def truediv(x: int, y: int) -> float:
#     try:
#         return x / y
#     except Exception as e:
#         logging.error(f"Error: {e}")
#         raise e
#
# try:
#     print(truediv(7, 2))
# except Exception as e:
#     pass


# def truediv(x: int, y: int) -> float:
#     if not isinstance(x, int | float):
#         logging.error('x must be int or float')
#         raise ValueError
#     if not isinstance(y, int | float):
#         logging.error('y must be int or float')
#         raise ValueError
#     if y == 0:
#         logging.debug('zero division')
#         raise ZeroDivisionError
#
#     return x / y
#
#
# try:
#     print(truediv('7', 2))
# except Exception as e:
#     pass



# def truediv(x, y):
#     try:
#         return x / y
#     except Exception as e:
#         print('Error')
#
#
#
# res = truediv(1, 0)
# print('Hello world')
# x = res ** 2

# print(x)


# import logging
#
# # create logger
# logger = logging.getLogger('simple_example')
# logger.setLevel(logging.DEBUG)
#
#
# file_hd = logging.FileHandler('app1.log')
# file_hd.setLevel(logging.ERROR)
#
# formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
#
# file_hd.setFormatter(formatter)
#
#
# stream_hd = logging.StreamHandler()
# stream_hd.setLevel(logging.DEBUG)
#
# formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
# stream_hd.setFormatter(formatter)
#
# logger.addHandler(stream_hd)
# logger.addHandler(file_hd)
#
#
# logger.debug('debug message')
# logger.info('info message')
# logger.warning('warn message')
# logger.error('error message')
# logger.critical('critical message')


import os

# print(os.getcwd())
#
# os.chdir('.venv')
#
# print(os.getcwd())
#
# file_name = 'app.log'
#
# print(os.path.exists(file_name))

# res = os.listdir('.')
# print(*res, sep='\n')


# os.mkdir('python_50')

# os.makedirs("parent_folder/child_folder/1/2")

# f = open('apple.txt', 'w')
# f.close()

my_cwd = os.getcwd()

my_path = os.path.join(my_cwd, 'python_50_02_04.py')
print(my_cwd)
print(my_path)
print(os.path.split(my_cwd))
print(os.path.dirname(my_path))
print(os.path.basename(my_path))

# SLIDE 53

