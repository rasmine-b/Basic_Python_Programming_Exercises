#Create a program that ask user to input 10 numbers. Display all numbers. For numbers with duplicate, display only the first entry.

#take 10 numbers as input
num_list = []
for i in range (1,11):
    num = float(input(f"Enter a number {i}: "))
    num_list.append(num)

#display first occurence and duplicate numbers
#display all numbers
