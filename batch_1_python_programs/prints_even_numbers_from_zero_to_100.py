#Create a program that print all even numbers starting from 0 to 100 (use for loop)

#Set a loop from 0 to 100 (inclusive)
#increasing by 2 each step

even_num_list = []
for i in range (0,101):
    if i % 2 == 0:
        even_num_list.append(i)
print(even_num_list)
