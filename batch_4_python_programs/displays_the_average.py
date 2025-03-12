#Create a program that ask user to input a number, continue asking until the user input is invalid. Display the average.

#start a loop that ask user to input a valid number until it's invalid
num_list = []
while True:
    try:
        num = float(input("Enter a number: "))
        num_list.append(num)
    except ValueError:
        break #end the loop if the input is invalid

#display the average
if num_list:
    average = sum(num_list) / len(num_list)
    print(f"The average is {average}")
else:
    print("Error. Enter a valid number.")
