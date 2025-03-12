#Create a program that ask user to input 10 numbers. Display all numbers that have duplicate.

#Ask user to input 10 numbers
num_list = []
for i in range (1,11):
    num = float(input(f"Enter a number {i}: "))
    num_list.append(num)

#Find numbers that have duplicate
duplicates = list(set(num for num in num_list if num_list.count(num) > 1))

#Display numbers that have duplicate
