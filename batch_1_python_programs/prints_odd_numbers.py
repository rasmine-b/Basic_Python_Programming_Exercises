#Create a program that ask user to input 10 numbers. Print how many are odd numbers.

#set a loop to repeat 10 times
odd_num_list = []
while True:
    try:
        for i in range (1,11):

#take 10 numbers as input, If the number is odd, increment odd_count by 1
            num = float(input("Enter a number {i}: "))
            if num % 2 != 0:
                odd_num_list.append(num)
        print(f"The number of odd numbers is {len(odd_num_list)}")
        break
    except ValueError:
        print("Error. Enter a valid number.")
