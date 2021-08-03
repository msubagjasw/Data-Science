steps = 0
c0 = int(input())
while c0 !=1 :
    if c0 % 2 == 0 :
        c0 = c0 / 2
        print(int(c0))
        steps = steps + 1
    else :
        c0 = c0 * 3 + 1
        print(int(c0))
        steps = steps + 1
        
print('Steps = ', steps)