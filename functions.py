# # 1
# def say_hello():
#     print('Hello World')

# say_hello()
# say_hello()
# say_hello()


# # 2
# def show_welcome():
#     print('Welcome to the system')


# # 3
# def show_menu():
#     print('''===== Main Menu =====
# 1. Start
# 2. Settings
# 3. Exit
# ''')


# # 4
# def show_numbers():
#     for i in range(1, 11):
#         print(i)


# # 5
# def show_even_numbers():
#     for i in range(1, 101):
#         if i % 2 == 0:
#             print(i)


# # 6
# def show_stars():
#     print('*' * 10)

# show_stars()


# def show_stars():
#     for _ in range(5):
#         print('*' * 10)


# # 7
# def greet(name):
#     print('Hello', name)


# # 8
# def show_age(age):
#     print('your age', age)


# # 9
# def calculate_sum(num1, num2):
#     print(num1 + num2)
    

# # 10
# def calculate_average(g1, g2, g3):
#     print((g1 + g2 + g3) / 3)
    

# # 11
# def check_even(num):
#     if num % 2 == 0:
#         print('even')
#     else:
#         print('odd')


# # 12
# def check_password(password):
#     if password == '123456':
#         print('Access Granted')
#     else:
#         print('Access Denied')


# # 13
# def calculate_discount(price, discount):
#     print(price - (price * discount / 100))


# # 14
# def show_range(num1, num2):
#     for i in range(num1, num2 + 1):
#         print(i)


# # 15
# def print_rectangle(width, height):
#     for _ in range(height):
#         print('*' * width)


# # 16
# def multiply(num1, num2):
#     return num1 * num2


# # 17
# def get_full_name(first_name, last_name):
#     return f'{first_name} {last_name}'


# # 18
# def get_max(num1, num2):
#     if num1 > num2:
#         return num1
#     return num2


# # 19
# def is_positive(num):
#     if num > 0:
#         return True
#     return False


# # 20
# def calculate_tax(price, vat):
#     return price * (1 + vat / 100)


# # 21
# def get_grade_status(grade):
#     if grade >= 90:
#         return 'Excellent'
#     elif grade >= 75:
#         return 'Good'
#     elif grade >= 60:
#         return 'Average'
#     else:
#         return 'Failed'


# # 22
# def count_digits(num):
#     count = 0
#     while num > 0:
#         num //= 10
#         count += 1
#     return count


# # 23
# def calculate_power(num, power):
#     result = 1
#     for _ in range(power):
#         result *= num
#     return result


# # 24
# def print_list(items):
#     for item in items:
#         print(item)


# # 25
# def get_list_sum(numbers):
#     total = 0
#     for num in numbers:
#         total += num
#     return total


# # 26
# def get_list_average(numbers):
#     if len(numbers) == 0:
#         return 0
#     total = 0
#     for num in numbers:
#         total += num
#     return total / len(numbers)


# # 27
# def find_number(numbers, num):
#     for num in numbers:
#         if num == num:
#             return True
#     return False


# # 28
# def find_max(numbers):
#     biggest = numbers[0]
#     for num in numbers:
#         if num > biggest:
#             biggest = num
#     return biggest


# 29
# def get_even_numbers(numbers):
#     return [num for num in numbers if num % 2 == 0]


# # 30
# def get_long_names(names):
#     return [name for name in names if len(name) > 4]


# # 31
# def reverse_list(items):
#     return items[::-1]


# # 32
# def count_occurrences(items, num):
#     count = 0
#     for item in items:
#         if item == num:
#             count += 1
#     return count


# # 33
# def remove_duplicates(items):
#     new_items = [items[0]]
#     check_item = items[0]
#     for item in items:
#         if item != check_item:
#             new_items.append(item)
#         check_item = item
#     return new_items


# # 34
# def calculate_final_price(price, discount):
#     after_discount = price * (1 - discount / 100)
#     if after_discount > 500:
#         after_discount = after_discount * 0.95
#     return after_discount


# # 35
# def check_list(numbers):
#     even = 0
#     odd = 0
#     total = 0
#     for num in numbers:
#         total += num
#         if num % 2 == 0:
#             even += 1
#         else:
#             odd += 1
#     return even, odd, total


# # 36
# def analyze_grades(grades):
#     total = 0
#     highest = grades[0]
#     lowest = grades[0]
#     passed = 0
#     for grade in grades:
#         total += grade
#         if grade > highest:
#             highest = grade
#         if grade < lowest:
#             lowest = grade
#         if grade >= 60:
#             passed += 1
#     average = total / len(grades)
#     return average, highest, lowest, passed


# # 37
# def validate_user(username, password):
#     if username and len(password) >= 6:
#         return True
#     return False


# # 38
# def search_students(students, name):
#     for student in students:
#         if student['name'] == name:
#             return student
#     return None


# # 39
# def calculate_cart_total(cart):
#     total = sum(list(map(lambda p: p['price'] * p['quantity'], cart)))
#     return total


# 40
# def get_fibonacci(n):
#     fibonacci_list = []
#     a = 0
#     b = 1
#     for _ in range(n):
#         fibonacci_list.append(a)
#         a, b = b, b + a
#     return fibonacci_list

# print(get_fibonacci(7))


# # 41
# name = "David"
# def show_name():
# 	name = "Moshe"
# print(name)
# show_name()
# print(name)
# david יודפס פעמיים


# # 42
# counter = 10

# def increase():
#     counter = 20
#     print(counter)

# increase()
# print(counter)
# המשתנה של הפונקציה לא משנה משתמש גלובלי


# # 43
# def add_ten(num):
#     return num + 10

# x = 5
# print(add_ten(x), x)
# לא משתנה


# # 44
# def add_to_list(items, new_item):
#     items.append(new_item)

# my_list = [1, 2, 3]
# add_to_list(my_list, 4)
# print(my_list)
# השתנתה


# # 45
# def copy_and_add(items, new_item):
#     new_list = items[:]
#     new_list.append(new_item)
#     return new_list

# list_ = [1, 2, 3]
# new_list = copy_and_add(list_, 4)
# print(list_, new_list)
# הרשימה הישנה לא השתנתה


# # final mission
# students = [
#     {'name': 'David', 'age': 20, 'grade': 90},
#     {'name': 'Moshe', 'age': 22, 'grade': 75},
#     {'name': 'Dana', 'age': 21, 'grade': 100},
#     {'name': 'Noa', 'age': 19, 'grade': 55},
#     {'name': 'Avi', 'age': 23, 'grade': 82}
# ]

# def show_menu():
#     print('''===== Student Management =====

# 1. Show all students
# 2. Add student
# 3. Search student
# 4. Update student grade
# 5. Remove student
# 6. Show passing students
# 7. Show class statistics
# 8. Show students above average
# 0. Exit
# ''')

# def show_students(students):
#     print(students)

# def add_student(students):
#     name = input('Enter name:')
#     age = int(input('Enter age:'))
#     grade = int(input('Enter grade:'))
#     students.append({'name': name, 'age': age, 'grade': grade})

# def search_student(students, name):
#     for student in students:
#         if student['name'] == name:
#             return student
#     return None

# def update_grade(students, name, grade):
#     for student in students:
#         if student['name'] == name:
#             student['grade'] = grade
#             return True
#     return False

# def remove_student(students, name):
#     for i in range(len(students)):
#         if students[i]['name'] == name:
#             students.pop(i)
#             return True
#     return False

# def get_passing_students(students):
#     return [student for student in students if student['grade'] >= 60]

# def get_average(students):
#     total = 0
#     for student in students:
#         total += student['grade']
#     return total / len(students)

# def get_highest_grade(students):
#     highest = students[0]['grade']
#     for student in students:
#         if student['grade'] > highest:
#             highest = student['grade']
#     return highest

# def show_statistics(students):
#     avg = get_average(students)
#     highest = get_highest_grade(students)
#     print(avg, highest)

# while True:
#     show_menu()
#     choice = input('Choose option: ')

#     if choice == '1':
#         show_students(students)

#     elif choice == '2':
#         add_student(students)

#     elif choice == '3':
#         target = input('Enter name: ')
#         found = search_student(students, target)
#         if found is None:
#             print('Not found')
#         else:
#             print(found['name'], found['age'], found['grade'])

#     elif choice == '4':
#         target = input('Enter name: ')
#         new_grade = int(input('Enter new grade: '))
#         if update_grade(students, target, new_grade):
#             print('grade updated')
#         else:
#             print('student not found')

#     elif choice == '5':
#         target = input('Enter name: ')
#         if remove_student(students, target):
#             print('student removed')
#         else:
#             print('student not found')

#     elif choice == '6':
#         passing = get_passing_students(students)
#         show_students(passing)

#     elif choice == '7':
#         show_statistics(students)

#     elif choice == '8':
#         avg = get_average(students)
#         for student in students:
#             if student['grade'] > avg:
#                 print(student['name'], student['grade'])

#     elif choice == '0':
#         break