#Create a program that ask user to input 10 numbers. Display all numbers that have duplicate.

#Ask user to input 10 numbers
num_list = []
for i in range (1,11):
    num = float(input(f"Enter a number {i}: "))
    num_list.append(num)

#Find numbers that have duplicates
duplicates = list(set(num for num in num_list if num_list.count(num) > 1))

#Display numbers that have duplicates
if duplicates:
    print(f"The numbers that have duplicates are {duplicates}")
else:
    print("Error. Enter a valid number.")