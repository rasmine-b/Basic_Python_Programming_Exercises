#Create a program that ask user to input 10 numbers. Print how many even numbers.

#set a loop to repeat 10 times
even_num_list = []
while True:
    try:
        for i in range (1,11):

#take 10 numbers as input 
#If the number is even, increment even_count by 1
            num = float(input(f"Enter a number {i}: "))
            if num % 2 == 0:
                even_num_list.append(num)
        print(f"The number of even numbers is {len(even_num_list)}")
        break
    except ValueError:
        print("Error. Enter a valid number.")
