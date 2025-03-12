#Create a program that ask user to input 2 numbers. Print the quotient of the two numbers with the decimal.

#take two numbers as input
while True:
    try:
        num_1 = float(input("Enter a number: "))
        num_2 = float(input("Enter a number: "))

#take the quotient of the two numbers with decimal
        num_quotient = num_1 / num_2
        print(f"The quotient of the two numbers is {num_quotient}")
        break
    except ValueError:
        print("Error. Enter a valid number.")