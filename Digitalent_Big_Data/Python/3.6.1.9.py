﻿my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
new  = []

for x in my_list:
    if x not in new:
        new.append(x)


print("The list with unique elements only:")
print(new)
