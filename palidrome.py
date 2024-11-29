def is_palindrome(s):
    # Remove any spaces and convert the string to lowercase
    s = s.replace(" ", "").lower()
    # Check if the string is equal to its reverse
    return s == s[::-1]

# Input from the user
input_string = input("Enter a string: ")

if is_palindrome(input_string):
    print(f'"{input_string}" is a palindrome.')
else:
    print(f'"{input_string}" is not a palindrome.')
