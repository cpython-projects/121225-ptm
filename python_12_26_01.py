# i = 1
#
# while i <= 5:
#     print(i)
#     i += 1
#
# while i <= 5:
#     i += 1
#     print(i)
#
# i = 1
# while i <= 5:
#     i += 1
#     print(i)


# i = 1
# while i <= 5:
#     print(i)


# i = 0
# while i < 5:
#     i += 1
#     print(i)


# i = 10
# while i > 7:
#     i -= 1
#
# print(i)


# i = 0
# while i < 5:
#     pass
# i += 1
# print(i)

# i = 1
# while i <= 10:
#     print(i)
#     if i == 5:
#         break
#     i += 1

# total = 0
# while True:
#     number = int(input('Enter a number: '))
#     if total + number > 100:
#         break
#     total += number
#
# print(total)

# while True:
#     pass

# i = 0
# while i < 5:
#     i += 1
#     if i % 2 == 0:
#         continue
#     print(i)
#
#
# i = 0
# while i < 5:
#     if i % 2 == 0:
#         continue
#     i += 1
#     print(i)

# i = 2
# while i <= 31:
#     print(i)
#     i += 2

# print(*range(2, 31, 2), sep='\n')
# i = 1
# while i <= 5:
#     if i == 3:
#         break
#     print(i)
#     i += 1


# i = 0
# while i < 5:
#     if i == 3:
#         continue
#     i += 1
#     print(i)




# n = int(input("Enter a number: "))
# i = 2
# flag = True
# while i < n:
#     if n % i == 0:
#         flag = False
#         break
#     i += 1
#
# if flag:
#     print("The number is prime")
# else:
#     print("The number is not prime")



# n = int(input("Enter a number: "))
# if n > 1:
#     i = 2
#     while i < n:
#         if n % i == 0:
#             print("The number is not prime")
#             break
#         i += 1
#     else:
#         print("The number is prime")


import random
x = random.randint(1, 10)

while True:
    ans = int(input("Enter a number: "))
    if ans == x:
        print("Congratulations!")
        break








