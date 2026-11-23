# # 1
# first_name = 'David'
# last_name = 'cohen'
# age = 25
# city = 'Tel Aviv'
# email = 'david@gmail.com'
# print(f"""===== User Details =====
# First Name: {first_name}
# Last Name: {last_name}
# Age: {age}
# City: {city}
# Email: {email}
# ========================
# """)


# # 2
# birth_year = 2002
# current_year = 2026
# my_age = current_year - birth_year
# print(f'You are approximately {my_age} years old.')


# # 3
# width = 2
# height = 4
# s = width * height
# p = (width + height) * 2
# print(f"""The area of the triangle is {s}
# The perimeter of the triangle is {p}""")

# # 4
# name = "David"
# age = 25
# height = 1.78
# is_student = True
# salary = 8500

# print(f"""{name} {type(name)}
# {age} {type(age)}
# {height} {type(height)}
# {is_student} {type(is_student)}
# {salary} {type(salary)}""")


# # 5
# f_name = input('Enter your first name:')
# l_name = input('Enter your last name:')
# city = input('Enter your city:')
# print(f'hello {f_name} {l_name} from {city}')


# # 6
# num_1 = int(input('Enter number:'))
# num_2 = int(input('Enter number:'))

# print(num_1 + num_2, num_1 - num_2, num_1 * num_2, num_1 / num_2, sep='\n')


# # 7
# product_name = input('Enter product name:')
# product_price = int(input('Enter product price:'))
# products_amount = int(input('Enter products amount:'))
# total_price = product_price * products_amount
# print(f'''====== Purchase Receipt ======
# Product: {product_name}
# Price: {product_price}
# Quantity: {products_amount}
# Total: {total_price}
# ==============================
# ''')


# # 9
# employee_name = input('Enter product name:')
# month_hours = int(input('Enter month hours:'))
# hour_salary = int(input('Enter hour salary:'))
# print(f'''====== Monthly Report ======
# Name: {employee_name}
# hours: {month_hours}
# salary per hours: {hour_salary}
# total salary: {month_hours * hour_salary}
# ==============================
# ''')


# # 10
# bill = int(input('Enter the bill:'))
# tip_percentage = int(input('Enter the tip:'))
# diners = int(input('Enter diners amount:'))

# tip = bill * (100 - tip_percentage)
# total_bill = bill + tip
# bill_per_diner = total_price / diners

# print(f"""Tip: {tip}
# Final bill: {total_bill}
# price per diner: {bill_per_diner}""")


# # 12
# a = 10
# b = 20

# c = a
# a = b
# b = c

# print(a, b, sep=' ')


# # final mission
# first_name = input('Enter your first name:')
# last_name = input('Enter your last name:')
# age = int(input('Enter your age:'))
# college = input('Enter college name:')
# course_name = input('Enter course name:')
# duration = int(input('Enter number of study months:'))
# monthly_price = float(input('Enter monthly price:'))

# print(f'''================================
#        STUDENT REGISTRATION
# ================================

# Student: {first_name} {last_name}
# Age: {age}
# Institution: {college}
# Course: {course_name}
# Duration: {duration}
# Monthly Price: {monthly_price}

# Total Course Price: {duration * monthly_price}

# ================================
# Registration completed!
# ================================
# ''')