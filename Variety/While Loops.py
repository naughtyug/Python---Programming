#Number 1
my = 10
while my > 0:
    print(my)
    my -= 1

#Number 2
total = 0
number = 1
while number <= 20:
    print(total)
    total += 1
    number += 1

#Number 3
even = 2
while even <= 50:
    print(even)
    even += 2

#Number 4
correct_passcode = "passcode"
#Evaluate
attempts = 0
while attempts < 3:
    Passcode = input("Please Enter Your Password")
    if Passcode == correct_passcode:
        print("Access granted")
        break
    attempts += 1
    if attempts < 3:
        print("Password doesn't match. Please Try again")
    else:
        print("Access denied. Too many attempts, please try again after 30 Days")


#Number 5
prime_number = 2
while prime_number < 20:
    i = 2
    while i*i <= prime_number:
        if prime_number % i == 0:
            break
        i += 1
    else:
            print(prime_number)
            prime_number += 1

#Number 6
total = 0
number = int(input("Enter a value (0 to stop):"))
while number != 0:
    total += number
    number = int(input("Enter a value (0 to stop):"))
    print("The sum of the numbers is:",total)

#Number 7
number = int(input("Enter a value"))
i = 1
while i <= 10:
    print(f"{number} x {i} = {number*i}")
    i += 1