#Create a program that ask user to input 10 numbers. Print the result of the first number minus all remaining numbers.

#set a loop to repeat 10 times
num_list = []
while True:
    try:
        for i in range (1,11):

#take 10 numbers as input
            num = float(input(f"Enter a number {i}: "))
            num_list.append(num)

#subtract the remaining numbers to the first number
        result = num_list [0]
        for num in num_list [1: ]:
            result -= num
        print(f"The difference of the first number minus to all remaining numbers is {result}")
        break
    except ValueError:
        print("Error. Enter a valid number.")