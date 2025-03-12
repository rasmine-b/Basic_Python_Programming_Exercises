#Create a program that print all the numbers starting from 0 to 100 except numbers ending in zero or ending in five.

#set a loop from 0 to 100, increasing by 1 each step
num_list = []
for i in range (0,101):

#if number does not end in 0 and does not end in 5 append to num_list
    if i % 10 != 0 and i % 10 != 5:
        num_list.append(i)
print(num_list)



