# # 1
# numbers = (10, 20, 30, 40, 50)
# print(numbers, numbers[0], numbers[-1], len(numbers), numbers[2])


# # 2
# students = ('Moshe', 'David', 'Dana', 'Noa', 'Michael')
# counter = 0
# for student in students:
#     print(student)
#     if student == 'Noa':
#         print('noa is in the list')
#     counter += 1

# print(counter)


# # 3
# numbers = (10, 20, 30, 40, 50)
# print(numbers[:3], numbers[2:], numbers[::-1])


# # 4
# product = ('apple', 30, 5, 'Fruits')
# print(product[0], product[1], product[2])


# # 6
# numbers = (10, 20, 30, 40, 50)
# total = 0
# biggest = numbers[0]
# evens = 0
# for num in numbers:
#     total += num
#     if num > biggest:
#         biggest = num
#     if num % 2 == 0:
#         evens += 1
# print(total, biggest, evens)


# # 7
# products = ("Laptop", "Mouse", "Keyboard", "Screen", "Printer")
# new_products1 = products[:3]
# new_products2 = products[-2:]
# new_products1 += new_products2
# print(new_products1, new_products2)


# # 7
# student = {    "name": "David",    "age": 22,    "grade": 95, "city": "Tel Aviv"}
# print(student["name"])
# student["age"] = 23
# student["city"] = "Tel Aviv"
# print(student)


# # 8
# car = {'brand': 'toyota',  'model': 'corola', 'year': 2020, 'price':90000}
# car['price'] = 80000
# car['year'] = 2021
# car['color'] = 'blue'
# print(car)


# # 9
# salaries = {    "David": 12000,    "Moshe": 15000,    "Dana": 13500}
# for salary in salaries.values():
#     print(salary)

# salaries["Dana"] = 9000
# salaries['avi'] = 8000
# for salary in salaries.values():
#     print(salary)


# # 10
# products = {'car': 70000, 'plane': 700000, 'ship': 300000, 'truck': 500000}
# search_product = input('Enter product:')
# if products.get(search_product):
#     print(products[search_product])
# else:
#     print('product not found')


# # 11
# grades = {"David": 100, "Moshe": 90, "Dana": 80, 'noa': 70, 'avi': 60}
# for grade in grades.items():
#     print(f'Student: {grade[0]} | Grade: {grade[1]}')


# # 12
# grades = {    "David": 90,    "Moshe": 75,    "Dana": 100,    "Noa": 55,    "Avi": 82}
# total = 0
# highest = 0
# counter = 0
# for grade in grades.items():
#     if grade[1] >= 80:
#         print(grade[0])
#     total += grade[1]
    
#     if grade[1] > highest:
#         highest = grade[0]

#     if grade[1] < 60:
#         counter += 1
# print(total / len(grades), highest, counter)


# # 13
# products = {"Laptop": 5000.0, "Mouse": 300.0, "Keyboard": 600.0, "Screen": 1000.0, "Printer": 400.0}
# product_name = input('Enter name')
# price = float(input('Enter price:'))
# products[product_name] = price


# # 14 15
# students = [    {"name": "David", "age": 20, "grade": 90},    {"name": "Moshe", "age": 22, "grade": 75},    {"name": "Dana", "age": 21, "grade": 100},    {"name": "Noa", "age": 19, "grade": 55},    {"name": "Avi", "age": 23, "grade": 82}]
# total = 0
# highest = 0
# for student in students:
#     print(student['name'])
#     print(student['grade'])

# for student in students:
#     if student['grade'] >= 80:
#         print(student)
#     total += student['grade']
#     if student['grade'] > highest:
#         highest = student['grade']
# print(total/len(students), highest)

# students.append({"name": "oren", "age": 26, "grade": 98})
# students[0]['grade'] = 50
# for student in students:
#     if student['name'] == 'oren':
#         students.remove(student)

# print(students)


# # 16
# classroom = {    "Class A": ["David", "Moshe", "Dana"],    "Class B": ["Noa", "Avi", "Michael"],    "Class C": ["Daniel", "Shir", "Yossi"]}
# for c in classroom:
#     print(c)

# print(classroom["Class A"])
# classroom["Class B"].append('ari')
# classroom["Class C"].remove('Yossi')

# for c in classroom.values():
#     print(len(c))


# # 17
# products = {    "Laptop": {        "price": 4500,        "stock": 10    },    "Mouse": {        "price": 80,        "stock": 50    },    "Keyboard": {        "price": 150,        "stock": 20    }}
# for product in products.values():
#     print(product['price'], product['stock'])

# products['Laptop']['stock'] = 20

# products['Screen'] = {        "price": 1000,        "stock": 30    }

# high_price_product = {k: v for k, v in products.items() if v["price"] > 100}
# print(high_price_product)


# # 18
# employees = [    ("David", "Development", 15000),    ("Moshe", "Marketing", 12000),    ("Dana", "Development", 18000),    ("Noa", "HR", 11000)]
# for employee in employees:
#     print(employee[0])

# high_salary = employees[0]
# total = 0
# for employee in employees:
#     if employee[1] == 'Development':
#         print(employee)

#     if employee[2] > high_salary[2]:
#         high_salary = employee

#     total += employee[2]

# print(high_salary, total/len(employees))


# # 19
# inventory = {    "Laptop": 10,    "Mouse": 50,    "Keyboard": 20}
# product_name = input('Enter name:')
# amount = int(input('Enter amount:'))
# print(inventory.get(product_name))
# if not inventory.get(product_name):
#     print(f'{product_name} not found')
# elif inventory[product_name] < amount:
#     print('amount out of stock')
# else:
#     inventory[product_name] -= amount

# print(inventory)


# # 20
# votes = {    "David": 0,    "Moshe": 0,    "Dana": 0}
# highest = ('', 0)
# choice = input('Enter your vote:')
# while choice != 'stop':
#     votes[choice] += 1
#     choice = input('Enter your vote:')
# for vote in votes.items():
#     if vote[1] > highest[1]:
#         highest = vote
#     print(vote)
# print(highest)


# # 21
# Contacts = {"David": '0508796675', "Moshe": '0548976587', "Dana": '0534765898'}

# while True:
#     choice = input('''1. add contact
# 2. search contact
# 3. update phone number
# 4. delete contact
# 5. display contact
# 6. exit
# ''')

#     if choice == '1':
#         name = input('Enter contact name:')
#         phone = input('Enter contact phone:')

#         Contacts[name] = phone

#     elif choice == '2':
#         name = input('Enter contact name:')
#         if Contacts.get(name):
#             print(Contacts[name])
#         else:
#             print('not found')

#     elif choice == '3':
#         name = input('Enter contact name:')
#         phone = input('Enter contact phone:')

#         if Contacts.get(name):
#             Contacts[name] = phone
#         else:
#             print('not found')

#     elif choice == '4':
#         name = input('Enter contact name:')

#         if Contacts.get(name):
#             Contacts.pop(name)
#         else:
#             print('not found')

#     elif choice == '5':
#         print(Contacts)

#     elif choice == '6':
#         break


# # final mission
# products = [    {"name": "Laptop", "price": 4500, "stock": 10},    {"name": "Mouse", "price": 80, "stock": 50},    {"name": "Keyboard", "price": 150, "stock": 20},    {"name": "Screen", "price": 900, "stock": 15}]

# while True:
#     print('''===== Store Management =====

# 1. Show all products
# 2. Add product
# 3. Search product
# 4. Update product price
# 5. Update product stock
# 6. Sell product
# 7. Show products by price
# 8. Show products with low stock
# 9. Show total inventory value
# 0. Exit
# ''')

#     choice = input('Choose option:')

#     if choice == '1':
#         print(products)

#     elif choice == '2':
#         name = input('Enter name:')
#         amount = float(input('Enter price:'))
#         amount = int(input('Enter stock:'))
        
#         products.append({"name": name, "price": amount, "stock": amount})

#     elif choice == '3':
#         name = input('Enter name:')
#         product = [product for product in products if product['name'] == name]
#         if product:
#             print(product)
#         else:
#             print('not found')


#     elif choice == '4':
#         name = input('Enter name:')
#         product = [product for product in products if product['name'] == name]
#         if product:
#             amount = float(input('Enter price:'))
#             product[0]['price'] = amount
#         else:
#             print('not found')

#     elif choice == '5':
#         name = input('Enter name:')
#         product = [product for product in products if product['name'] == name]
#         if product:
#             amount = float(input('Enter price:'))
#             product[0]['stock'] = amount
#         else:
#             print('not found')

#     elif choice == '6':
#         name = input('Enter name:')
#         product = [product for product in products if product['name'] == name]
#         if product:
#             amount = float(input('Enter price:'))
#             if product[0]['stock'] < amount:
#                 print('Not enough in stock')
#             else:
#                 product[0]['stock'] -= amount
#         else:
#             print('not found')

#     elif choice == '7':
#         minimum_stock = int(input('Enter minimum price:'))
#         print([product for product in products if product['price'] > minimum_stock])

#     elif choice == '8':
#         minimum_stock = int(input('Enter minimum stock:'))
#         print([product for product in products if product['price'] > minimum_stock])

#     elif choice == '9':
#         print(sum(list(map(lambda p: p['stock'] * p['price'], products))))

#     elif choice == '0':
#         break