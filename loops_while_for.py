# # 1
# i = 1
# while i <= 10:
    # print(i)
#     i += 1


# # 2
# for i in range(1,11):
#     print(i)
# print('START!')


# # 3
# i = 1
# while i <= 50:
#     if i % 2 == 0:
#         print(i)
#     i += 1


# # 4
# num = int(input('Enter a number: '))
# i = 1
# while i <= 5:
#     print(num * i)
#     i += 1


# # 5
# i = 1
# total = 0
# while i <= 100:
#     total += i
#     i += 1
# print(total)


# # 6
# password = input('Enter password: ')
# while password != 'Python123':
#     password = input('Enter password: ')
# print('Welcome!')


# # 7
# number = 27
# guess = int(input('Guess the number: '))
# while guess != number:
#     guess = int(input('Guess the number: '))
# print('Correct guess')


# # 8
# total = 0
# num = int(input('Enter a number:'))
# while num != 0:
#     total += num
#     num = int(input('Enter a number:'))
# print(total)


# # 9
# count = 0
# total = 0
# grade = float(input('Enter grade or 999 to stop:'))
# while grade != 999:
#     count += 1
#     total += grade
#     grade = float(input('Enter grade or 999 to stop:'))
# print(f'Were inserted: {count} grades')
# print(f'Sum of grades: {total}')
# print(f'The average: {total / count}')


# # 10
# the_sum = 0
# count = 0
# num = int(input('Enter a number:'))
# while num >= 0:
#     count += 1
#     if num > 0:
#         the_sum = the_sum + num
#     num = int(input('Enter a number:'))
# print(f'Sum of positive numbers:{the_sum}')
# print(f'{count} numbers entered')


# # 11
# num = int(input('Enter number:'))
# i = 1
# while i <= 10:
#     print(num, 'x', i, '=', num * i)
#     i += 1


# # 12
# num = int(input('Enter a number:'))
# digits = 0
# while num > 0:
#     digits += 1
#     num = num // 10
# print(digits)


# # 13
# num = int(input('Enter a number: '))
# reverse_num = 0
# while num > 0:
#     reverse_num = reverse_num * 10 + (num % 10)
#     num = num // 10
# print(reverse_num)


# # 14
# num = int(input('Enter a number:'))
# if num <= 1:
#     print('not prime')
# else:
#     div_num = 2
#     while div_num < num:
#         if num % div_num == 0:
#             print('not prime')
#             break
#         div_num += 1
#     else:
#         print('Prime')


# # 15
# balance = 5000
# choice = ''
# while choice != '4':
#     choice = input('Enter your choice: (1. check balance, 2. deposit, 3. withdrow, 4. exit)')
#     if choice == '1':
#         print(balance)
#     elif choice == '2' or choice == '3':
#         amount = int(input('Enter the amount:'))
#         if amount < 0:
#             print('It is not possible to perform an action with a negative amount')
#         elif amount > balance:
#             print('The balance is too low')
#         else:
#             balance += amount if choice == '2' else -amount
#             print(balance)
#     elif choice == '4':
#         break


# # 16
# num = 1
# while True:
#     print(num)
#     num += 1
#     if num == 15:
#         break
        

# # 17
# for i in range(30):
#     if i % 3 == 0:
#         continue
#     print(i)
     
        
# # 18
# num = ''
# while True:
#     num = input('Enter num:')
#     if num == '100':
#         print('success')
#         break


# # 19
# for i in range(1, 21):
#     print(i)


# # 20
# for i in range(0, 101, 5):
#     print(i)


# # 21
# total = 0
# for i in range(1, 101):
#     total += i
# print(total)


# # 22
# num = int(input('Enter num'))
# for i in range(1,11):
#     print(num, 'x', i, '=', num * i)


# # 23
# start = int(input('Enter start:'))
# end = int(input('Enter end:'))
# total = 0
# for i in range(start, end + 1):
#     total = += i
# print(total)


# # 24
# for i in range(1, 101):
#     if i % 3 == 0 and i % 5 == 0:
#         print(i)


# # 25
# rows = int(input('Enter rows:'))
# cols = int(input('Enter columns:'))
# for r in range(rows):
#     for c in range(cols):
#         print('*', end='')
#     print()


# # 26
# for r in range(1, 7):
#     for c in range(r):
#         print('*', end='')
#     print()


# # 27
# for i in range(1, 11):
#     for j in range(1, 11):
#         print(i, 'x', j, '=', i * j)
#     print()


# # 28
# for i in range(1, 6):
#     for j in range(1, 6):
#         print(i, ',', j)


# # 29
# choice = ''
# while choice != '3':
#     print('''===== MATH GAME =====

# 1. Start Game
# 2. View Instructions
# 3. Exit

# ''')
#     choice = input('Choose: ')
#     if choice == '1':
#         counter = 0

#         for i in range(1,11):
#             print(i, '+', 3, '=')
#             answer = int(input('Enter your answer:'))
#             if answer == i + 3:
#                 counter += 1
#         print(counter)

#     elif choice == '2':
#         print('Enter the answers to the questions')

#     elif choice == '3':
#         break