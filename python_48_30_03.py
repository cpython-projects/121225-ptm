# while True:
#     try:
#         a = int(input('a>>'))
#         b = int(input('b>>'))
#         res = a / b
#         print(res)
#         break
#     except ZeroDivisionError as error:
#         print('Делить на ноль нельзя')
#     except ValueError as error:
#         print('Вы ввели некорректное число!', error)
#     except Exception as error:
#         print(error)


# while True:
#     try:
#         a = int(input('a>>'))
#         b = int(input('b>>'))
#         res = a / b
#         print(res)
#         break
#     except (ZeroDivisionError, ValueError) as error:
#         print(error)

# while True:
#     try:
#         a = int(input('a>>'))
#         b = int(input('b>>'))
#         res = a / b
#     except (ZeroDivisionError, ValueError) as error:
#         print(error)
#     else:
#         print(res)
#         break

#
# try:
#     # Проверка числа на чётность
#     number = int(input("Введите число: "))
# except ValueError:
#     # Обработка некорректного ввода
#     print("Ошибка! Введите корректное число.")
# else:
#     # Выполняется только если число успешно введено
#     if number % 2 == 0:
#         print(f"{number} – чётное число.")
#     else:
#         print(f"{number} – нечётное число.")


def netto_salary(salary: int | float, tax_rate: int | float = 0.01) -> int | float:
    """

    :param salary:
    :param tax_rate:
    :return:
    """
    if not isinstance(tax_rate, int | float):
        raise TypeError('Tax rate must be an integer or float')
    if not 0 <= tax_rate <= 1:
        raise ValueError('Tax rate must be between 0 and 1')

    return salary * (1 - tax_rate)


try:
    print(netto_salary(100, '50'))
except Exception as e:
    print(e)





