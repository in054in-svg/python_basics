# תרגיל 1
i = 1
while i <= 10:
    print(i)
    i = i + 1


# תרגיל 2
i = 10
while i >= 1:
    print(i)
    i = i - 1
print('START!')


# תרגיל 3
i = 1
while i <= 50:
    if i % 2 == 0:
        print(i)
    i = i + 1


# תרגיל 4
num = int(input('Enter a number: '))
i = 1
while i <= 5:
    print(num * i)
    i = i + 1


# תרגיל 5
i = 1
total = 0
while i <= 100:
    total = total + i
    i = i + 1
print(total)


# תרגיל 6
password = input('Enter password: ')
while password != 'Python123':
    password = input('Enter password: ')
print('Welcome!')


# תרגיל 7
secret_number = 27
guess = int(input('Guess the number: '))
while guess != secret_number:
    guess = int(input('Guess the number: '))
print('Correct!')


# תרגיל 8
total = 0
num = int(input('Enter a number (0 to stop): '))
while num != 0:
    total = total + num
    num = int(input('Enter a number (0 to stop): '))
print(total)


# תרגיל 9
count = 0
total = 0
grade = float(input('Enter grade (999 to stop): '))
while grade != 999:
    count = count + 1
    total = total + grade
    grade = float(input('Enter grade (999 to stop): '))
print('Count:', count)
print('Sum:', total)
if count > 0:
    print('Average:', total / count)
else:
    print('Average:', 0)


# תרגיל 10
positive_sum = 0
count = 0
num = int(input('Enter a number (negative to stop): '))
while num >= 0:
    count = count + 1
    if num > 0:
        positive_sum = positive_sum + num
    num = int(input('Enter a number (negative to stop): '))
print('Sum of positive numbers:', positive_sum)
print('Total numbers entered:', count)


# תרגיל 11
num = int(input('Enter number: '))
i = 1
while i <= 10:
    print(num, 'x', i, '=', num * i)
    i = i + 1


# תרגיל 12
num = int(input('Enter a positive integer: '))
digits = 0
while num > 0:
    digits = digits + 1
    num = num // 10
print(digits, 'digits')


# תרגיל 13
num = int(input('Enter a positive integer: '))
reversed_num = 0
while num > 0:
    reversed_num = reversed_num * 10 + (num % 10)
    num = num // 10
print(reversed_num)


# תרגיל 14
num = int(input('Enter an integer: '))
if num <= 1:
    print('Not prime')
else:
    divisor = 2
    while divisor < num:
        if num % divisor == 0:
            print('Not prime')
            break
        divisor = divisor + 1
    else:
        print('Prime')


# תרגיל 15
balance = 5000
choice = ''
while choice != '4':
    print('1. Check balance')
    print('2. Deposit')
    print('3. Withdraw')
    print('4. Exit')
    choice = input('Choose action: ')
    if choice == '1':
        print('Balance:', balance)
    elif choice == '2':
        amount = float(input('Enter deposit amount: '))
        if amount <= 0:
            print('Amount must be positive')
        else:
            balance = balance + amount
            print('New balance:', balance)
    elif choice == '3':
        amount = float(input('Enter withdrawal amount: '))
        if amount <= 0:
            print('Amount must be positive')
        elif amount > balance:
            print('Insufficient balance')
        else:
            balance = balance - amount
            print('New balance:', balance)
    elif choice == '4':
        print('Goodbye')
    else:
        print('Invalid choice')


# תרגיל 16
i = 1
while i <= 100:
    if i == 15:
        break
    print(i)
    i = i + 1


# תרגיל 17
i = 1
while i <= 30:
    if i % 3 == 0:
        i = i + 1
        continue
    print(i)
    i = i + 1


# תרגיל 18
while True:
    num = int(input('Enter a number: '))
    if num == 100:
        print('Success! Found 100.')
        break


# תרגיל 19
for i in range(1, 21):
    print(i)


# תרגיל 20
for i in range(0, 101, 5):
    print(i)


# תרגיל 21
total = 0
for i in range(1, 101):
    total = total + i
print(total)


# תרגיל 22
num = int(input('Enter number: '))
for i in range(1, 11):
    print(num, 'x', i, '=', num * i)


# תרגיל 23
start = int(input('Start: '))
end = int(input('End: '))
total = 0
for i in range(start, end + 1):
    total = total + i
print('Result:', total)


# תרגיל 24
for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print(i)


# תרגיל 25
rows = int(input('Enter rows: '))
cols = int(input('Enter columns: '))
for r in range(rows):
    for c in range(cols):
        print('*', end='')
    print()


# תרגיל 26
for r in range(1, 7):
    for c in range(r):
        print('*', end='')
    print()


# תרגיל 27
for i in range(1, 11):
    for j in range(1, 11):
        print(i, 'x', j, '=', i * j)
    print()


# תרגיל 28
for i in range(1, 6):
    for j in range(1, 6):
        print(i, ',', j)


# תרגיל 29
choice = ''
while choice != '3':
    print('===== MATH GAME =====')
    print('1. Start Game')
    print('2. View Instructions')
    print('3. Exit')
    choice = input('Choose: ')
    if choice == '1':
        score = 0

        if float(input('2 + 3 = ')) == 5:
            score = score + 1

        if float(input('8 - 4 = ')) == 4:
            score = score + 1

        if float(input('6 * 7 = ')) == 42:
            score = score + 1

        if float(input('20 / 4 = ')) == 5:
            score = score + 1

        if float(input('15 + 9 = ')) == 24:
            score = score + 1

        if float(input('12 - 7 = ')) == 5:
            score = score + 1

        if float(input('9 * 3 = ')) == 27:
            score = score + 1

        if float(input('36 / 6 = ')) == 6:
            score = score + 1

        if float(input('14 + 16 = ')) == 30:
            score = score + 1

        if float(input('50 - 18 = ')) == 32:
            score = score + 1

        print('Final score:', score, '/ 10')
    elif choice == '2':
        print('Answer 10 math questions. Each correct answer gives 1 point.')
    elif choice == '3':
        print('Exiting game.')
    else:
        print('Invalid choice.')