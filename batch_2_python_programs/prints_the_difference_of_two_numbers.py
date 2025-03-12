#Create a program that ask user to input 2 numbers. Print the difference of the 2 numbers.

#take 2 numbers as input
while True:
    try:
        num_1 = float(input("Enter a number: "))
        num_2 = float(input("Enter a number: "))

#take the difference of the two numbers
        num_difference = num_1 - num_2
        print(f"The difference of the two numbers is {num_difference}")
        break
    except ValueError:
        print("Error. Enter a valid number.")