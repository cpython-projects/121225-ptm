data = [
    "1 Bob Simson 19.58$ decorations",
    "2 Mary 66.7$ food",
    "3 Mary 98.91$ toys",
    "4 Aleksa 72.29$ drinks",
    "5 Maria Simson 84.48$ food",
    "6 Aleksa 100.41$ accessories",
    "7 Mary 19.9$ accessories",
    "8 Bob Simson 83.88$ drinks",
    "9 Bob Simson 58.21$ instruments",
    "10 Maria Simson 20.61$ accessories",
    "11 Aleksa 37.74$ drinks",
    "12 Mary 12.32$ drinks",
    "13 Maria Simson 32.11$ toys",
    "14 Maria Simson 94.73$ instruments",
    "15 Mary 52.48$ clothes",
    "16 Maria Simson 87.64$ drinks",
    "17 Jack 70.86$ clothes",
    "18 Bob Simson 134.5$ drinks",
    "19 Jack 4.23$ instruments",
    "20 Jack 62.59$ food"
]

# Посчитать общую сумму расходов семьи по каждой категории

# expenses = {}

# for row in data:
#     *_, amount, category = row.split()
#     amount = float(amount.replace('$', ''))
#     category = category.lower()
#
#     if category in expenses:
#         expenses[category] += amount
#     else:
#         expenses[category] = amount

# expenses = {}
#
# for row in data:
#     *_, amount, category = row.split()
#     amount = float(amount.replace('$', ''))
#     category = category.lower()
#
#     expenses[category] = expenses.get(category, 0) + amount


#
# categories = (
#     "decorations",
#     "food",
#     "toys",
#     "drinks",
#     "accessories",
#     "instruments",
#     "clothes"
# )
#
#
# expenses = dict.fromkeys(categories, 0)
#
# for row in data:
#     *_, amount, category = row.split()
#     amount = float(amount.replace('$', ''))
#     category = category.lower()
#
#     expenses[category] += amount


# Необходимо построить словарь, где:
# ключ — имя человека
# значение — список всех его расходов в долларах


# expenses = {}
#
# for row in data:
#     _, *name, amount, _ = row.split()
#     amount = float(amount.replace('$', ''))
#     name = ' '.join(name)
#
#     if name not in expenses:
#         expenses[name] = []
#
#     expenses[name].append(amount)


# expenses = {}
#
# for row in data:
#     _, *name, amount, _ = row.split()
#     amount = float(amount.replace('$', ''))
#     name = ' '.join(name)
#
#     expenses.setdefault(name, []).append(amount)


# "9 Bob Simson 58.21$ instruments"
# "9", "Bob", "Simson", "58.21$", "instruments"
# x[1] + ' ' + x[2]
# id, f_name, l_name, amount, category = x
# _, *name, amount, _ = x
# "10 Maria 20.61$ accessories",
# "10", "Maria", "20.61$", "accessories",
# x[1]
# id, f_name, amount, category = x


# dict1 = {"a": 1, "c": 1, "b": [2, 1, 5]}
# dict2 = {"b": [2, 1, 5], "a": 1, "c": 1}
# print(dict1 != dict2)


# a = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six'}
# b = {5: 'five', 6: 'six', 7: 'seven', 8: ['eight'], 9: 'nine'}
#
# print(a.keys() & b.keys())
# print(a.items() | b.items())



# def func(name):
#     name = name.upper()
#     x = 20
#     return name
#
#
#
# name = 'Oleh'
# res = func(name)
# print(res)
# print(name)
# print(func)


# def func():
#     # name = 'Alice'
#     res = name.upper()
#     return res
#
#
# name = 'Oleh'
# print(func())



# def func(salaries):
#     return [item * 0.8 for index, item in enumerate(salaries)]
#
#
# x = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]
# res = func(x)
# print(res)
# print(x)
#
#
# def func(name):
#     name = name.upper()
#     return name


# x = 'Oleh'
# res = func(x)
# print(x)
# print(res)




name = 'Oleh'
y = 789

def func():
    global name, y
    name = 5
    y = 100


print(func())
print(name)
print(y)

















