#Create a program that print all the numbers starting from 0 to 100 except numbers end in zero.

#Set a loop from 1 to 100
non_zero_num_list = []
for i in range (1,101):

#If the number does not end in 0, append to num_list
    if i % 10 != 0:
        non_zero_num_list.append(i)
print(non_zero_num_list)


