#Number 2

import random

number = random.randint(1,20)
#Come up with a secret number
while True:
    try:
        guess_number = int(input("Please guess a number between 1 & 20"))
        if 1 <= guess_number <= 20:
            if guess_number <= number:
                print("Well guessed")
                break
            else:
               print("Try again ")
        else:
            print("Your guess must be between 1 & 20")
    except ValueError:
        print("Invalid input. Please enter a number")

#Number 4
word = input("Enter your word of choice")
word_reverse = word [:: -1 ]
print("word_revese:", word_reverse)

#Number 8
def multiplication_table(number):
    for i in range (1,11):
        print(f"{number} * {i} = {number * i}")
#Get user input
num = int(input("Enter a value:"))

#Call function
multiplication_table(num)
         

#Number 12
def count_letters(text):
    uppercaase_count = sum(1 for char in text if char.isupper())
    lowercase_count = sum(1 for char in text if char.islower())

    print("Uppercase letters:", uppercaase_count)
    print("Lowercase letters::", lowercase_count)


#Number 13
def check_password(password):
    if not 8 <= len(password) <= 16:
        return "Password must be 8-16 characters long."

    has_lower = False
    has_upper = False
    has_digit = False
    has_special = False

    for char in password:
        if char.islower():
            has_lower = True
        elif char.isupper():
            has_upper = True
        elif char.isdigit():
            has_digit = True
        elif char in "$%&":
            has_special = True

    if not (has_lower and has_upper and has_digit and has_special):
        return "Password must contain lowercase, uppercase, numbers, and special characters ($, %, &)."

    return "Valid password!"

# Get password from user
while True:
    password = input("Enter a password: ")
    message = check_password(password)
    print(message)
    if message == "Valid password!":
        break

#Number 39
my_number = int(input("Enter a number: "))

if my_number > 0:
  print(my_number, "is a positive number.")
elif my_number == 0:
  print(my_number, "is zero.")
else:
  print(my_number, "is a negative number.")


#Number 50
for i in range(10):
    for j in range(i, -1, -1):
        print(j, end="")
    print()

#Number 3
for i in range(6):
    for j in range(i + 1):
        print("#", end="")
    print()

for i in range(4, 0, -1):
    for j in range(i):
        print("#", end="")
    print()

#Number 42
def is_float(string):
    try:
        float(string)
        return True
    except ValueError:
        return False
enter_string = input("Enter a string")
if is_float(enter_string):
    print("The string is a float")
else:
    print("The string ain't/isn't a float")

#Number 23
for row in range(7):
    for col in range(7):
        if (col == 0 or col == 6) or (row > 2 and (col == row or col == 6 - row)):
            print("*", end="")
        else:
            print(" ", end="")
    print()

#Number 47
from datetime import datetime, timedelta

def find_previous_day(year, month, day):

    current_date = datetime(year, month, day)

    previous_date = current_date - timedelta(days=1)

    revamped_date = previous_date.strftime("%Y-%m-%d")

    return revamped_date

# Get input from the user
year = int(input("Enter a Year: "))
month = int(input("Enter a Month [1-12]: "))
day = int(input("Enter a Day [1-31]: "))

previous_day = find_previous_day(year, month, day)
print("The previous date is:", previous_day)




