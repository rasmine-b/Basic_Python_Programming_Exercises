#Create a program that ask user to input 2 numbers. Print the product of the two numbers.

#take two numbers as input
while True:
    try:
        num_1 = float(input("Enter a number: "))
        num_2 = float(input("Enter a number: "))

#take the product of the two numbers
        num_product = num_1 * num_2
        print(f"The product of the two numbers is {num_product:.0f}")
        break
    except ValueError:
        print("Error. Enter a valid number.")
