#Create a program that ask user to input a number, continue asking until the user input is invalid. Display the highest number.

#start a loop that ask user a valid number until it's invalid
num_list = []
while True:
    try:
        num = float(input("Enter a number: "))
        num_list.append(num)
    except ValueError:
        break #end the loop if the input is invalid

#display the highest number
if num_list:
    print(f"The highest number is {max(num_list)}")
else:
    print("Error. Enter a valid number.")

