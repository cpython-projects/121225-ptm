# numbers = [1, 2, 4, 5, 7, 9, 10, 11]
#
# numbers_even = list(filter(lambda item: item % 2 == 0, numbers))
# print(numbers_even)
#
#
# numbers_even = list(map(lambda item: item % 2, numbers))
# print(numbers_even)
#
#
# data = [0, 1, False, True, '', 'Python', [], [1, 2, 3]]
# numbers_even = list(filter(None, data))
# print(numbers_even)

# numbers = [1, 2, 3, 4]
# from functools import reduce
# res = reduce(lambda x, y: x * y, numbers)
# print(res)
#
#
# numbers = [1,]
# res = reduce(lambda x, y: x * y, numbers)
# print(res)
#
# numbers = []
# res = reduce(lambda x, y: x * y, numbers)
# print(res)

from functools import reduce

# cart = [
#     {"name": "laptop", "price": 1000, "discount": 0.1},
#     {"name": "mouse", "price": 50, "discount": 0.0},
#     {"name": "keyboard", "price": 100, "discount": 0.2},
# ]
#
# res = sum(item['price'] * (1 - item['discount']) for item in cart)
# print(res)
#
# res = reduce(lambda acc, item: acc + item['price'] * (1 - item['discount']), cart, 0)
# print(res)



# daily_sales = [
#     {"apple": 10, "banana": 5},
#     {"apple": 3, "banana": 7},
#     {"apple": 8, "banana": 2, 'tomatos': 30},
# ]
#
# res = reduce(lambda acc, day:
#              {
#                     key: acc.get(key, 0) + day.get(key, 0)
#                     for key in set(day) | set(acc)
#              },
#              daily_sales,
#              {}
#             )
#
# print(res)

#
# transactions = [
#     {"type": "deposit", "amount": 1000},
#     {"type": "withdraw", "amount": 200},
#     {"type": "withdraw", "amount": 150},
#     {"type": "deposit", "amount": 500},
# ]
#
# res = reduce(lambda acc, detail: acc + detail['amount'] if detail['type'] == 'deposit' else acc - detail['amount'],
#              transactions,
#              0)
# print(res)
#
# res =sum(map(lambda detail: detail['amount'] if detail['type'] == 'deposit' else -detail['amount'], transactions))
# print(res)
#
# total = 0
# for transaction in transactions:
#     if transaction['type'] == 'deposit':
#         total += transaction['amount']
#     else:
#         total -= transaction['amount']
# print(total)


# conditions = [x > 10 for x in [15, 20, 8]]
# print(any(conditions))
# print(all(conditions))
# print(sum(conditions))

# words = ['mango', 'grape', 'apple', 'strawberry', 'banana', 'pineapple', 'kiwi', 'blueberry']
# words_sorted = sorted(words, key=lambda word: (word[0], len(word)))
# print(*words_sorted, sep='\n')
#
# print('*' * 20)
#
# words_sorted = sorted(words, key=lambda word: (len(word), word[0]))
# print(*words_sorted, sep='\n')

# students = [("Alice", 5), ("Alice", 35), ("Alice", 45), ("Bob", 20), ("Charlie", 23)]
# students_sorted = sorted(students, key=lambda student: student[1])
# print(students_sorted)


# cities = [('New York', 8419600), ('Los Angeles', 3980400), ('Chicago', 2716000)]
# city, _ = max(cities, key=lambda x: x[1])
# print(city)
#
# city, _ = min(cities, key=lambda x: x[1])
# print(city)



orders = [
    {"category": "electronics", "amount": 1200},
    {"category": "clothes", "amount": 200},
    {"category": "electronics", "amount": 800},
    {"category": "clothes", "amount": 150},
    {"category": "books", "amount": 100},
]

# {
#     'electronics': {'count': 2, 'total': 2000},
#     'clothes': {'count': 2, 'total': 350},
#     'books': {'count': 1, 'total': 100}
# }

from collections import defaultdict

res = defaultdict(lambda: {'count': 0, 'total': 0})
for order in orders:
    cat = order["category"]
    res[cat]['count'] += 1
    res[cat]['total'] += order["amount"]
print(*res.items(), sep='\n')

print('*' * 20)
res = {}
for order in orders:
    cat = order["category"]
    if cat in res:
        res[cat]['count'] += 1
        res[cat]['total'] += order["amount"]
    else:
        res[cat] = {'count': 1, 'total': order["amount"]}
print(*res.items(), sep='\n')
