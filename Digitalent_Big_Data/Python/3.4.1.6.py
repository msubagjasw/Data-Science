﻿hat_list = [1, 2, 3, 4, 5]  # This is an existing list of numbers hidden in the hat.

# Step 1: write a line of code that prompts the user
x = int(input())
# to replace the middle number with an integer number entered by the user.
hat_list[(len(hat_list)//2)] = x
# Step 2: write a line of code that removes the last element from the list.
hat_list.pop()
# Step 3: write a line of code that prints the length of the existing list.
print(len(hat_list))
print(hat_list)
