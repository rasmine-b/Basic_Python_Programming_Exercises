#Create a program that ask user to input a number, continue asking until the user input is invalid. Display "Unique" after input when the inputted number don't have duplicate. Display "Duplicate" after input when the inputted number have duplicate.

#start a loop that ask user to input number until it's invalid
num_list = []
while True:
    try:
        num = float(input("Enter a number: "))
        if num not in num_list:
            print("Unique.")
        else:
            print("Duplicate.")
        num_list.append(num)
    except ValueError:
        break #end the loop if the input is invalid

#display all entered numbers 
print(f"All the numbers are {num_list}")