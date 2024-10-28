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