# 1
num1 = 25
num2 = 7

print(num1 + num2, num1 - num2, num1 * num2, num1 / num2, num1 // num2, num1 % num2, num1 ** num2)


#2
balance = 1000
balance += 250
print(balance)
balance -= 100
print(balance)
balance *= 2
print(balance)
balance /= 4
print(balance)


# 3
price = float(input('Enter price:'))
discount = float(input('Enter discount:'))
discount_amount = price * (discount / 100)
print(f'discount_amount {discount_amount}')
print(f'total price {price - discount_amount}')


# 4
amount = float(input('Enter the amount:'))
interest_rates = float(input('Enter the interest rates:'))
interest = amount * (interest_rates / 100)
total_amount = amount + interest
print(f'interest {interest}, total: {total_amount}')


# 5
score_1 = float(input('Enter score:'))
score_2 = float(input('Enter score:'))
score_3 = float(input('Enter score:'))
average = (score_1 + score_2 + score_3) / 3
print(f'The average: {average}')


# 6
first_name = "David"
last_name = "Cohen"
city = "Tel Aviv"

sentence = 'Hello, my name is' +first_name + last_name + 'and I live in' + city
f_sentence = f'Hello, my name is {first_name} {last_name} and I live in {city}.'


# 7
name = input('Enter your name:')
print(name, len(name), name.upper(), name.lower())


# 8
sentence = input('Enter a sentence:')
print(sentence.upper(), sentence.lower(), sentence.capitalize(), sentence.title())


# 9
name = input('Enter your name:')
print(name, name.strip(), len(name), len(name.strip()))


# 10
sentence = "I love Java programming"
print(sentence.replace('Java', 'Python'), sentence.count('love'), sentence.startswith('I'), sentence.endswith('programming'))


# 11
word = "Programming"
print(word[0], word[-1], word[2], word[:3], word[-4:], word[::-1])


# 12
a = "100"
b = "25"
c = 10
d = 5.5

print(int(a), float(b), str(c), int(d))


# 13
age = input("Enter your age: ")
# אי אפשר לחבר סטרינג ומספר

print(int(age) + 10)


# 14
price_excluding_vat = float(input('Enter a price excluding vat:'))
price_including_vat = price_excluding_vat * 1.18
print(price_including_vat)


# 15
first_name = input('Enter your first name:')
last_name = input('Enter your last name:')
age = float(input('Enter your age:'))
monthly_salary = float(input('Enter your monthly salary:'))
seniority_years = float(input('Enter your years of seniority:'))

print(f"""===== Employee Details =====
First Name: {first_name}
Last Name: {last_name}
Age: {age}
monthly_salary: {monthly_salary}
years of seniority: {seniority_years}
years salary: {monthly_salary * 12}
salary + bonus: {monthly_salary * 1.05} 
length of full name: {len(first_name) + len(last_name)}
========================
""")


# 16
usd_rate = 3.25

shekels = float(input('Enter shekels amount:'))
print(f'dollars: {shekels / usd_rate}, euro: {shekels / 3.75}, with commission: {shekels * 0.98}')


# 17
first_name = input('Enter your first name:')
last_name = input('Enter your last name:')
year_of_birth = int(input('Enter date of birth:'))
email = f'{first_name}.{last_name}.{year_of_birth}@gmail.com'.lower()
print(email)


# 18
sentence = input('Enter a sentence:')
print(sentence, len(sentence), sentence.upper(), sentence.lower(), sentence[::-1], sentence.count('a'), sentence.replace(' ', '-'))


# final mission
name = input('Enter your name:')
product_name = input('Enter your name:')
product_price = float(input('Enter the price:'))
products_amount = int(input('Enter the price:'))
discount = int(input('Enter the discount:'))
vat = int(input('Enter the vat:'))
after_discount = products_amount * product_price * ((100 - discount) / 100)
vat_amount = product_price * (vat / 100)

print(f'''================================
          PURCHASE INVOICE
================================

Customer: {name}
Product: {product_name}

Unit Price: {product_price}
Quantity: {products_amount}

Subtotal: {products_amount * product_price}
Discount: {discount}
After Discount: {after_discount}

VAT: {vat}
VAT Amount: {vat_amount}

TOTAL: {after_discount - vat_amount}

================================
       THANK YOU FOR SHOPPING
================================
''')