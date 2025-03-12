#Create a program that ask user to input a number, continue asking until the user input is invalid. Display the lowest number

#start a loop that ask user to input number until it's invalid
num_list = []
while True:
    try:
        num = float(input("Enter a number: "))
        num_list.append(num)
    except ValueError:
        break #end the loops if the input is invalid

#display the lowest number
if num_list:
    print(f"The lowest number is {min(num_list)}")
else:
    print("Error. Enter a valid number.")

