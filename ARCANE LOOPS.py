
#countdown
limit = 10
while limit > 0:
    print(limit)
    limit -= 1

#sum of the first 20 natural numbers
total = 0
number = 1
while number <= 20:
    print(number)
    number += 1
    total += 1

#all even numbers between 1 and 50
highest_number = 50
even = 2
while even <= 50:
    if even%2 == 0:
        print(even)
        even +=2

#password attempts
password = "arcanewildcrd_21"
attempts = 0
while attempts < 3:
    Password = input("Please enter password")
    if Password == password:
        print("Access Granted")
        break
    attempts += 1
    if attempts < 3:
        print("Incorrect password. Please try again")
    else:
        print("Too many attempts. Please try again later")

#prime numbers less than 20
prime = 2
while prime <= 20:
    d = 2
    while d*d <= prime:
        if prime % d == 0:
            break
        d += 1
    else:
           print(prime)
           prime += 1

#user input sum
total_sum = 0
number = int(input("Please enter number(0 to stop):"))
while number != 0:
    total_sum += number
    number = int(input("Please enter number(0 to stop):"))
    print("The sum of the numbers is", number)

#multiplication table
number = int(input("Please enter a value"))
g = 1
while g <= 10:
    print(f"{number} x {g} = {number*g}")
    g += 1






































































