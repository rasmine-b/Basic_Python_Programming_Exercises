#Create a program that ask user to input 2 numbers. Print "Equal" when the numbers are the same.

#take two numbers as input 
while True:
    try:
        num_1 = float(input("Enter a number: "))
        num_2 = float(input("Enter a number: "))
#checks if the two numbers are the same
        if num_1 == num_2:
            print("Equal")
    except ValueError:
        print("Error. Enter a valid number.")