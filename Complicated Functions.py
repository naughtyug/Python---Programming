#Number 2
def character_frequency(enter_string):
    frequency = {}
    for her in enter_string:
        if her in frequency:
            frequency[her] += 1
        else:
            frequency[her] = 1
    return frequency

#Get input from the user
user_text = input("Enter a text")
result = character_frequency(user_text)
print("Character Frequency:", result)

#Number 4
def swap_concatenate(str1, str2):

#Swap characters
    new_str1 = str2[:2] + str1[2:]
    new_str2 = str1[:2] + str2[2:]

#Concatenate characters
    result = new_str1 + " " + new_str2
    return result

#Get input from user
string_one = input("Enter your first string")
string_two = input("Enter your second string")

format_strings = swap_concatenate(string_one, string_two)
print("Modified string:", format_strings)

#Number 7
def elimination(the_string):
    result = ""
    for us, sexy in enumerate(the_string):
        if us % 2 == 0:
            result += sexy
    return result

#Get user unput
enter_text = input("Enter your text")

modify = elimination(enter_text)
print("Modified string:", modify)

#Number 10
def the_reverse(string):
    return string[::-1]

#User input
user_input = input("Enter text")
reversed_input = the_reverse(user_input)
print("Reversed string:", reversed_input)

#Number 12
def lets_reverse(s):
    words = s.split()
    reverse_words = words[::-1]
    return "".join(reverse_words)

#Let user enter data
entering_text = input("Enter text")
text_reverse = lets_reverse(entering_text)
print("Reversed words:", text_reverse)

#Number 16
#def digit_sum(input):
 #   sum_of_digits = 0
  #  for some in input:
   #     if some .isdigit():
       #     sum_of_digits += int(some)
    #return sum_of_digits
#Involve User Input
#enter_str = input("Enter your string")
#result = digit_sum(enter_str)
#print(f"Sum of digits:", result)

#Number 18
def char_count(text):
    char_type = {"uppercase": 0, "lowercase": 0, "numeric": 0, "special": 0}
    for real in text:
        if real.isupper():
            char_type["uppercase"] += 1
        elif real.islower():
            char_type["lowercase"] += 1
        elif real.isdigit():
            char_type["numeric"] += 1
        else:
            char_type["special"] += 1
    return char_type
#User Input
enter_string = input("Enter string")
outcome = char_count(enter_string)
print(f"String:{enter_string}")
for star, count in outcome.items():
    print(f"{star.capitalize()}:{count}")

#Number 47
def remove_duplicates(input_str):
    outcome = []
    for sticks in input_str:
        if not outcome or sticks != outcome[-1]:
            outcome.append(sticks)
    return ''.join(outcome)
#User input
enter_text = input("Enter text")
modify = remove_duplicates(enter_text)
print(f"String:", modify)
