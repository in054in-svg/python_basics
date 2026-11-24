# # 1
# numbers = [10, 20, 30, 40, 50]
# print(numbers, numbers[0], numbers[-1], numbers[2])


# # 2
# students = ['eli', 'moshe', 'itamar', 'yakov']
# print(len(students), students[0], students[-1])
# students[1] = 'ahron'
# print(students)


# 3
# grades = [69, 90, 75, 88, 100]
# grades.append(78)
# grades.insert(0, 70)
# grades[2] = 92
# print(grades)


# # 4
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# numbers.pop(0)
# print(numbers)
# numbers.pop()
# print(numbers)
# numbers.pop(3)
# print(numbers)


# # 5
# products = ['car', 'plane', 'ship', 'truck']
# if 'plane' in products:
#     print('plane is in the list')
# if 'motorcycle' not in products:
#     print('motorcycle is not in the list')


# # 6
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# for num in numbers:
#     print(num)


# # 7
# numbers = [12, 7, 24, 19, 8, 3, 10]
# for num in numbers:
#     if num % 2 == 0:
#         print(num)


# # 8
# grades = [80, 90, 70, 85, 95]
# total = 0
# for grade in grades:
#     total += grade
# print(total)


# # 9
# numbers = [15, 42, 8, 99, 23, 67]
# biggest = numbers[0]
# for num in numbers:
#     if num > biggest:
#         biggest = num
# print(biggest)


# # 10
# names = ['eli', 'moshe', 'itamar', 'yakov']
# search_name = input('Enter name: ')
# for name in names:
#     if name == search_name:
#         print('Found')
#         break
# else:
#     print('Not Found')


# 11
# numbers = [5, 10, 5, 20, 5, 30]
# num = int(input('Enter number: '))
# for i in range(len(numbers)):
#     if numbers[i] == num:
#         print(i)


# # 12
# numbers = [10, 55, 80, 23, 50, 120, 49]
# count = 0
# for num in numbers:
#     if num > 50:
#         count += 1
# print(count)


# # 13
# numbers = [1, 2, 3, 4, 5, 6, 7, 8]
# even_numbers = []
# for num in numbers:
#     if num % 2 == 0:
#         even_numbers.append(num)
# print(even_numbers)


# # 14
# names = ['eli', 'moshe', 'itamar', 'yakov']
# i = 0
# while i < len(names):
#     print(i, names[i])
#     i += 1


# # 15
# numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# print(numbers[:3], numbers[-3:], numbers[2:7], numbers[::-1])


# # 16
# names = ['eli', 'moshe', 'itamar', 'yakov', 'zvi', 'netanel', 'yosi', 'efraim', 'menachem', 'gad']
# print(names[::2], names[1::2], names[::-2])


# 17
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
# first10 = numbers[:10]
# last10 = numbers[-10:]
# middles = numbers[5:15]
# print(first10, last10, middles)


# # 18
# numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# first = numbers[:len(numbers) // 2]
# last = numbers[len(numbers) // 2:]
# print(first, last)


# # 19
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# doubled = [num * 2 for num in numbers]
# squared = [num ** 2 for num in numbers]
# evens = [num for num in numbers if num % 2 == 0]
# big_than_5 = [num for num in numbers if num > 5]
# print(doubled, squared, evens, big_than_5)


# # 20
# grades = [55, 90, 67, 100, 45, 82, 73, 30]
# pass_grades = [grade for grade in grades if grade > 60]
# fail_grades = [grade for grade in grades if grade < 60]
# plus5 = [grade + 5 for grade in grades]
# print(pass_grades, fail_grades, plus5)


# # 21
# names = ['Moshe', 'David', 'Dana', 'Noa', 'Michael', 'Avi']
# names_big_than_for = [name for name in names if len(name) > 4]
# upper_names = [name.upper() for name in names]
# names_start_D = [name for name in names if name.startswith('D')]
# print(names_big_than_for, upper_names, names_start_D)


# # 22
# numbers = [12, 7, 25, 30, 9, 44, 18, 3]
# filtered_numbers = [num for num in numbers if num % 3 == 0 and num > 10]
# print(filtered_numbers)


# # 23
# numbers = []
# for n in range(10):
#     numbers.append(int(input('Enter number:')))

# highest = numbers[0]
# lowest = numbers[0]
# total = 0
# for num in numbers:
#     if num > highest:
#         highest = num
#     if num < lowest:
#         lowest = num
#     total += num

# print(numbers, highest, lowest, total / len(numbers))


# # 24
# users = ['Moshe', 'David', 'Dana', 'Noa', 'Michael']
# name = input('Enter name to remove: ')
# for i in range(len(users)):
#     if users[i] == name:
#         users.pop(i)
#         print('Removed')
#         break
# else:
#     print('Not found')
# print(users)


# # 25
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# evens = [num for num in numbers if num % 2 == 0]
# odds = [num for num in numbers if num % 2 != 0]
# big_than_20 = [num for num in numbers if num > 20]
# print(evens, odds, big_than_20)


# # 26
# numbers = [3, 8, 3, 15, 8, 22, 3]
# name = int(input('Enter number: '))
# indexes = []
# for i in range(len(numbers)):
#     if numbers[i] == name:
#         indexes.append(i)

# if len(indexes) > 0:
#     print(indexes, len(indexes))
# else:
#     print('not found')


# # 27
# list1 = [1, 2, 3, 4]
# list2 = [5, 6, 7, 8, 9]
# lists = list1 + list2
# print(lists, lists[:5], lists[-5:], lists[::-1])


# # 28
# numbers = [10, 25, 30, 45, 60]
# new_num = int(input('Enter number: '))
# for name in numbers:
#     if name == new_num:
#         break
# else:
#     numbers.append(new_num)
# print(numbers)


# # final mission
# grades = [85, 72, 90, 55, 100, 63, 48, 77]

# while True:
#     print('''===== Grades Management =====

# 1. Show all grades
# 2. Add a grade
# 3. Search for a grade
# 4. Remove a grade
# 5. Show passing grades
# 6. Show failing grades
# 7. Show highest and lowest grade
# 8. Show average grade
# 9. Show first 3 grades
# 10. Show grades in reverse
# 0. Exit
# ''')

#     choice = input('Choose option: ')

#     if choice == '1':
#         for grade in grades:
#             print(grade)

#     elif choice == '2':
#         new_grade = int(input('Enter grade: '))
#         grades.append(new_grade)

#     elif choice == '3':
#         name = int(input('Enter grade to search: '))
#         indexes = []
#         for i in range(len(grades)):
#             if grades[i] == name:
#                 indexes.append(i)
#         if len(indexes) > 0:
#             print(indexes)
#         else:
#             print('Not found')

#     elif choice == '4':
#         name = int(input('Enter grade to remove: '))
#         for i in range(len(grades)):
#             if grades[i] == name:
#                 grades.pop(i)
#                 print('Removed')
#                 break
#         else:
#             print('grade not found')

#     elif choice == '5':
#         print([grade for grade in grades if grade >= 60])

#     elif choice == '6':
#         print([grade for grade in grades if grade < 60])

#     elif choice == '7':
#         if len(grades) == 0:
#             print('list is empty')
#         else:
#             highest = grades[0]
#             lowest = grades[0]
#             for grade in grades:
#                 if grade > highest:
#                     highest = grade
#                 if grade < lowest:
#                     lowest = grade
#             print(highest, lowest)

#     elif choice == '8':
#         if len(grades) == 0:
#             print('list is empty')
#         else:
#             total = 0
#             for grade in grades:
#                 total += grade
#             print(total / len(grades))

#     elif choice == '9':
#         print(grades[:3])

#     elif choice == '10':
#         print(grades[::-1])

#     elif choice == '0':
#         break

#     else:
#         print('invalid choice')