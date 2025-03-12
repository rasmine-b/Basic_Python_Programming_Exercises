#Create a program that ask user to input a number, continue asking until the user input is invalid. Display the number with the most number of duplicate.

#start a loop that ask user to input a number until it's invalid
num_list = []
while True:
    try:
        num = float(input("Enter a number: "))
        num_list.append(num)
    except ValueError:
        break #end the loop if the input is invalid

#display the number with the most number of duplicate
if num_list:
    frequent_number = max(set(num_list), key=num_list.count)
    print(f"The most number of duplicate {frequent_number}")
else:
    print("Error. Enter a valid number.")
