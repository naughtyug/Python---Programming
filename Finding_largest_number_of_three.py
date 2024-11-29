def find_largest_number(number_1, number_2, number_3):

    if number_1 > number_2 and number_1 > number_3:
        return number_1
    elif number_2 > number_1 and number_2 > number_3:
        return number_2
    elif number_3 > number_1 and number_3 > number_2:
        return number_3
    elif number_1 == number_2 and number_1 > number_3:
        return "Two numbers are equal and largest."
    elif number_1 == number_3 and number_1 > number_2:
        return "Two numbers are equal and largest."
    elif number_2 == number_3 and number_2 > number_1:
        return "Two numbers are equal and largest."
    else:  # All three numbers are equal
        return "Two numbers are equal and largest."  # Or could return num1 (or any of them)


# Get input from the user
number_1 = int(input("Enter the first number: "))
number_2 = int(input("Enter the second number: "))
number_3 = int(input("Enter the third number: "))

# Find and print the largest number
result = find_largest_number(number_1, number_2, number_3)
print(f"{result} is the largest number.")


