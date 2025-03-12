#Create a program that ask user to input 10 numbers. Display all numbers that don't have duplicate.

#Ask user to input 10 numbers
duplicate_num_list = []
for i in range (1,11):
    num = float(input("Enter a number {i}: "))
    duplicate_num_list.append(num)
    
#Find numbers that don't have duplicate
duplicate_numbers = [num for num in duplicate_num_list if duplicate_num_list.count(num) == 1]

#Display numbers that don't have duplicate
