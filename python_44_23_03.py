# # Example of comment
# # This function returns sum of two numbers.
# # a - number 1
# # b - number 2
# def add(a: int, b: int) -> int:
#     """
#     Returns the sum of two numbers.
#
#     Full text.
#
#     :param a: First number.
#     :param b: Second number.
#     :return: Sum of two numbers.
#     """
#     return a + b
#
#
# x1: str = '5'
# x1 = 5
# print(x1)
#
# res = add('3', '4') + 'hjj'
# print(res)
#
#
# def process_numbers(numbers: list[int]) -> list[int]:
#     return [n ** 2 for n in numbers]
#
#
# x = [2, 3, 4, '5', 6]
# print(process_numbers(x))
#
#
# from typing import Any
#
# def process_data(data: Any) -> str:
#     return f"Данные: {data}"


from typing import Optional

def get_user_name(user_id: int) -> Optional[str]:
    users = {1: "Alice", 2: "Bob"}
    return users.get(user_id)

x = get_user_name(1)
print(x)

x = get_user_name(20)
print(x)


def add(a: int | float, b: int | float) -> int | float:
    return a + b


print(add(1, 2))
print(add(1., .2))



from typing import Union

def add(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    return a + b


from typing import Callable, Iterable
def my_filter(sequence: Iterable, predicat: Callable[[int], bool]) -> list:
    pass












