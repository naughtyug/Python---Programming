#THEM
my_number = int(input("Enter a number"))
for i in range(1,my_number +1):
    for n in range(1,my_number +1):
        print(i*n, end="\t")
    print()