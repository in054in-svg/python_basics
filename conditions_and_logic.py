# # 1
# age = int(input('Enter your age:'))
# if age >= 18:
#     print('adult')
# else:
#     print('minor')
    

# # 2   
# num = int(input('Enter num:'))
# if num > 0:
#     print('Positive')
# elif num < 0:
#     print('Negative')
# else:
#     print('Zero')
    
    
 
# # 3
# num = int(input('Enter num:'))
# if num % 2 == 0:
#     print('Even')
# else:
#     print('Odd') 


# # 4
# num1 = int(input('Enter num:'))
# num2 = int(input('Enter num:'))
# if num1 == num2:
#     print('The numbers are equal')
# else:
#     print('The numbers are not equal')


# # 5
# password = "Python123"
# user_password = input('Enter the password:')
# if password == user_password:
#     print('Access Granted')
# else:
#     print('Access Denied')


# # 6
# num = int(input('Enter num:'))
# if num in [n for n in range(1,11)]:
#     print('1-10')
# elif num in [n for n in range(11,51)]:
#     print('11-50')
# elif num in [n for n in range(51,101)]:
#     print('51-100')
# else:
#     print('Out of range')


# # 7
# grade = int(input('Enter grade:'))
# if 0 <= grade <= 59:
#     print('Failed')
# if 60 <= grade <= 69:
#     print('Passed')
# if 70 <= grade <= 79:
#     print('Good')
# if 80 <= grade <= 89:
#     print('Very Good')
# if 90 <= grade <= 100:
#     print('Excellent')


# # 8
# correct_username = "admin"
# correct_password = "123456"


# user_username = input('Enter your username:')
# user_password = input('Enter the password:')

# if user_username == correct_username and user_password == correct_password:
#     print('Login Successful')
# if user_username == correct_username and user_password != correct_password:
#     print('Wrong Password')
# if user_username != correct_username:
#     print('Unknown User')


# # 9
# age = int(input('Enter your age:'))
# product_price = float(input('Enter the price::'))

# if age > 60:
#     product_price *= 0.80
# elif age < 18:
#     product_price *= 0.90

# print(product_price)


# # 10
# num = int(input('Enter num:'))
# if num % 3 == 0:
#     print('The number is divisible by 3')
# if num % 5 == 0:
#     print('The number is divisible by 5')
# if num % 3 == 0 and num % 5 == 0:
#     print('The number is divisible by 3 and 5')
# else:
#     print('The number is not divisible by 3 and 5')


# 11
# average = float(input('Enter grade:'))
# monthly_salary = int(input('Enter monthly_salary:'))
# if average > 90:
#     print('entitled to')
# elif average > 85 and monthly_salary < 5000:
#     print('entitled to')
# else:
#     print('not entitled to')


# # 13
# correct_username = "admin"
# correct_password = "123456"


# user_username = input('Enter your username:')
# user_password = input('Enter the password:')
# account_status = input('Enter account status')

# if user_username == correct_username and user_password == correct_password and account_status == 'active':
#     print('Login Successful')
# else:
#     print('Access Denied')


# # 14
# num = int(input('Enter num:'))
# if 20 <= num <= 80:
#     print(True)
# if not num < 20 and not num > 80:
#     print(True)


# # 15
# balance = 5000
# withdraw = int(input('Enter withdraw amount:'))

# if withdraw > 0:
#     if withdraw <= balance:
#         balance -= withdraw
#         print(balance)
#     else:
#         print('The balance is too low')
# else:
#     print('The withdrawal amount must be positive')


# # 16
# age = int(input('Enter your age:'))
# club_card = input('Do you have a club card?')

# if age <= 12:
#     if club_card == 'yes':
#         price = 22.5
#     else:
#         price = 25
# elif 12 < age < 18:
#     if club_card == 'yes':
#         price = 31.5
#     else:
#         price = 35
# elif 18 <= age:
#     if club_card == 'yes':
#         price = 45
#     else:
#         price = 50

# print(f'The price is {price}')


# # 17
# age = int(input('Enter your age:'))
# monthly_salary = int(input('Enter monthly_salary:'))
# seniority_years = int(input('Enter Years of seniority:'))

# if age >= 21 and monthly_salary >= 7000 and seniority_years >= 1:
#     print('entitled to')
# elif age < 21:
#     print('Minimum age is 21')
# elif monthly_salary < 7000:
#     print('Minimum monthly salary 7,000')
# elif seniority_years < 1:
#     print('Minimum one year seniority')
    
# # 18
# vehicle_type = input('Enter vehicle type:')
# hours = float(input('Enter parking hours: '))

# if vehicle_type == 'motorcycle':
#     discount = 10
# elif vehicle_type == 'private':
#     discount = 20
# elif vehicle_type == 'commercial':
#     discount = 30

# print(discount * hours)

    

# # 19
# num1 = float(input('Enter number: '))
# num2 = float(input('Enter number: '))
# action = input('Enter operation: ')

# if action == "+":
#     print(num1 + num2)
# elif action == "-":
#     print(num1 - num2)
# elif action == "*":
#     print(num1 * num2)
# elif action == "/":
#     if num2 == 0:
#         print('Cannot be divided by 0')
#     else:
#         print(num1 / num2)
# else:
#     print('invalid operation')
    
    
# 20
# year = int(input("Enter year: "))

# if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
#     print("Leap year")
# else:
#     print("Not a leap year")
    
    
# # 21
# hours = float(input("Enter hours: "))
# if hours <= 182:
#     print(hours * 50)
# elif hours <= 184:
#     print(182 * 50 + (hours - 182) * 50 * 1.25)
# else:
#     print(182 * 50 + 2 * 50 * 1.25 + (hours - 184) * 50 * 1.5)

    
# final part
# age = int(input('Enter your age:'))
# amount = float(input('Enter amount:'))
# member = input(' are you club member:')
# opened = input('The product opened?:')
# invoice = input('there is invoice:')
# days = int(input('Enter how many days passed:'))

# if amount <= 0 or not (invoice == 'yes') or opened == 'yes':
#     print('Not entitled to')
#     if amount <= 0:
#         print('invalid amount')
#     elif invoice != 'yes':
#         print('You cannot return an item without an invoice')
#     else:
#         print('A product that has been opened cannot be returned.')
# else:
#     if member == 'yes' and days <= 30:
#         print('Entitled to')
#         print('Refund:', amount)
#     elif member != 'yes' and days <= 14:
#         print('Entitled to')
#         print('Refund:', amount)
#     else:
#         print('Not entitled to, The return period has passed')