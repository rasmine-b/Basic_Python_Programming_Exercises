#Create a program that ask user to input 10 numbers. Display all numbers. For numbers with duplicate, display only the first entry.

#take 10 numbers as input
num_list = []
for i in range (1,11):
    num = float(input(f"Enter a number {i}: "))
    num_list.append(num)

#display unique and duplicate numbers
duplicate_numbers = set()
unique_numbers = []
for num in num_list:
    if num not in duplicate_numbers:
        unique_numbers.append(num)
        duplicate_numbers.add(num)

#display all numbers
print("The numbers are {unique_numbers:.0f}")
