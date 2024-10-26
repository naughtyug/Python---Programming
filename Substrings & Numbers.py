#Sub_String
substring_1 = input("Enter substring")
substring_2 = input("Enter other substring")
substring_1 = sorted(substring_1)
substring_2 = sorted(substring_2)
if substring_1 == substring_2:
    print("This is a substring")
else:
    print("This is no string")

#Multiples"FIZZBUZZ"
for numbers in range(1,101):
    if numbers % 3 == 0 and numbers % 5 == 0:
        print("FizzBuzz")
    if numbers % 3 == 0:
        print("Fizz")
    else:
        print(numbers)
    if numbers % 5 == 0:
        print("Buzz")
    else:
        print(numbers)

#OtherNumber
def myevens(upper_limit):
    even_sum = 0
    for num in range(2, upper_limit + 1, 2):
        even_sum += num
    return even_sum

try:
    user_input = int(input("Enter the upper limit: "))
    if user_input < 1:
        print("Please enter a positive integer greater than 0.")
    else:
        result = myevens(user_input)
        print(f"Sum of even numbers between 1 and {user_input}: {result}")
except ValueError:
    print("Invalid input. Please enter a valid positive integer.")


