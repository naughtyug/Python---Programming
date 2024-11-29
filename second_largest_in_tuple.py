def find_second_largest(numbers):
    first = second = float("-inf")
    second_largest_numbers = set()
    
    for us in numbers:
        if us > first:
            second = first
            first = us
        elif first > us > second:
            second = us
            
    for us in numbers:
        if us == second:
            second_largest_numbers.add(us)
    
    return list(second_largest_numbers)

# Input from the user
user_input = input("Enter numbers separated by spaces: ")
numbers = tuple(map(int, user_input.split()))

second_largest = find_second_largest(numbers)
print("The Second largest number(s) is/are:", second_largest)


