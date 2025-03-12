#Create a program that ask user to input a number, continue asking until the user input is invalid. Display the number from highest to lowest. Clue: sort() function

#start a loop that ask user to a valid number until it's invalid
num_list = []
while True:
    try:
        num = float(input("Enter a number: "))
        num_list.append(num)
    except ValueError:
        break #end the loop if the input is invalid

#display numbers from highest to lowest
if num_list:
    num_list.sort(reverse=True)
    print(f"The numbers from highest to lowest are {num_list}")
else:
    print("Error. Enter a valid number.")
