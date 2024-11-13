grading = input("Enter a grade (A, B, C, D, F): ").upper()

if grading == "A":
    gpa = 5.0
elif grading == "B":
    gpa = 4.5
elif grading == "C":
    gpa = 4.0
elif grading == "D":
    gpa = 3.5
elif grading == "F":
    gpa = 0.0
else:
    gpa = "Invalid grade"

print(f"The GPA for grade {grading} is {gpa}")
